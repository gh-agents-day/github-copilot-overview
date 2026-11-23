import uuid
from datetime import date, timedelta
from typing import Dict, List, Optional
from models import LoanRecord, LoanStatus, MemberType
from services.database_service import DatabaseService
from services.catalog_service import CatalogService
from services.membership_service import MembershipService
from services.fine_calculator import FineCalculator
from services.notification_service import NotificationService


class LoanService:
    """
    Coordinates borrowing and returning of library books:
    Validates membership quotas, reserves book copies, creates loan records,
    and persists state into JSON database.
    """

    LOAN_PERIOD_DAYS = {
        MemberType.STUDENT: 14,
        MemberType.FACULTY: 30,
        MemberType.REGULAR: 14,
    }

    def __init__(
        self,
        catalog_service: CatalogService,
        membership_service: MembershipService,
        fine_calculator: FineCalculator,
        notification_service: NotificationService,
        db_service: Optional[DatabaseService] = None,
    ):
        self.catalog = catalog_service
        self.membership = membership_service
        self.fines = fine_calculator
        self.notifications = notification_service
        self.db = db_service or (catalog_service.db if hasattr(catalog_service, "db") else DatabaseService())

    def borrow_book(self, member_id: str, isbn: str) -> LoanRecord:
        """Issue a book loan to an active member and persist to JSON database."""
        member = self.membership.get_member(member_id)
        if not member:
            raise ValueError(f"Member '{member_id}' not found")

        book = self.catalog.get_book(isbn)
        if not book:
            raise ValueError(f"Book with ISBN '{isbn}' not found in catalog")

        if book.is_reference_only:
            raise ValueError(f"'{book.title}' is a reference copy and cannot be checked out")

        # Check and reserve copy in catalog database
        if not self.catalog.decrement_copy(isbn):
            raise ValueError(f"No available copies of '{book.title}' in stock")

        # Validate member quota and fine standing
        if not self.membership.register_loan(member_id):
            raise RuntimeError(
                f"Member '{member.name}' has exceeded borrow quota ({member.active_loans_count}/{member.max_borrow_limit}) or has outstanding fines."
            )

        loan_period = self.LOAN_PERIOD_DAYS.get(member.member_type, 14)
        borrow_date = date.today()
        due_date = borrow_date + timedelta(days=loan_period)

        loan_id = f"LN-{uuid.uuid4().hex[:8].upper()}"
        loan_record = LoanRecord(
            loan_id=loan_id,
            member_id=member_id,
            isbn=isbn,
            borrow_date=borrow_date,
            due_date=due_date,
            status=LoanStatus.ACTIVE,
        )

        # Persist loan to database
        self.db.insert_loan(loan_record)

        self.notifications.send_notice(
            member.email,
            f"Loan Confirmation: {book.title}",
            f"Due date: {due_date.isoformat()}",
        )

        return loan_record

    def return_book(self, loan_id: str) -> LoanRecord:
        """Process book return, update loan status, and increment catalog copies."""
        loan = self.db.get_loan(loan_id)
        if not loan:
            raise ValueError(f"Loan record '{loan_id}' not found")

        if loan.status == LoanStatus.RETURNED:
            raise ValueError(f"Loan '{loan_id}' has already been returned")

        self.db.update_loan_status(loan_id, LoanStatus.RETURNED)
        self.catalog.increment_copy(loan.isbn)
        self.membership.close_loan(loan.member_id)

        loan.status = LoanStatus.RETURNED
        loan.return_date = date.today()
        return loan
