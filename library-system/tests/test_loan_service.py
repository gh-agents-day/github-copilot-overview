import os
import shutil
import pytest
from services.database_service import DatabaseService
from services.catalog_service import CatalogService
from services.membership_service import MembershipService
from services.fine_calculator import FineCalculator
from services.notification_service import NotificationService
from services.loan_service import LoanService


@pytest.fixture
def setup_library(tmp_path):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    master_db = os.path.join(base_dir, "data", "library_db.json")
    test_db = str(tmp_path / "test_library_db.json")
    shutil.copyfile(master_db, test_db)

    db = DatabaseService(test_db)
    catalog = CatalogService(db)
    membership = MembershipService(db)
    fines = FineCalculator()
    notifications = NotificationService()
    loan_svc = LoanService(catalog, membership, fines, notifications, db)
    return catalog, membership, loan_svc


def test_successful_borrow(setup_library):
    catalog, membership, loan_svc = setup_library
    isbn = "978-0132350884"  # Clean Code
    initial_copies = catalog.get_book(isbn).available_copies

    loan = loan_svc.borrow_book("MEM-001", isbn)

    assert loan.status.value == "ACTIVE"
    assert catalog.get_book(isbn).available_copies == initial_copies - 1
    assert membership.get_member("MEM-001").active_loans_count == 1


def test_borrow_fails_restores_book_copy(setup_library):
    """Verify available book copies in catalog are preserved when checkout fails."""
    catalog, _, loan_svc = setup_library
    isbn = "978-0134685991"  # Effective Java
    initial_copies = catalog.get_book(isbn).available_copies

    with pytest.raises(RuntimeError, match="exceeded borrow quota|outstanding fines"):
        loan_svc.borrow_book("MEM-004", isbn)

    current_copies = catalog.get_book(isbn).available_copies
    assert current_copies == initial_copies, (
        f"Book copy leak! Expected {initial_copies} copies, but catalog has {current_copies}"
    )
