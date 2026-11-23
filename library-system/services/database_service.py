import json
import os
from dataclasses import asdict
from datetime import date
from typing import Dict, List, Optional, Any
from models import Book, Member, MemberType, LoanRecord, LoanStatus


class DatabaseService:
    """
    Mock JSON-file database service providing full CRUD operations
    for Books, Members, and Loans.
    """

    def __init__(self, db_path: Optional[str] = None):
        if db_path is None:
            # Default to data/library_db.json relative to this file's root
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            self.db_path = os.path.join(base_dir, "data", "library_db.json")
        else:
            self.db_path = db_path

        self._data: Dict[str, List[Dict[str, Any]]] = {"books": [], "members": [], "loans": []}
        self.load()

    # -------------------------------------------------------------------------
    # Core Persistence Helpers
    # -------------------------------------------------------------------------
    def load(self) -> None:
        """Load database records from JSON file."""
        if os.path.exists(self.db_path):
            with open(self.db_path, "r", encoding="utf-8") as f:
                self._data = json.load(f)
        else:
            self._data = {"books": [], "members": [], "loans": []}

    def save(self) -> None:
        """Persist current in-memory data to the JSON file."""
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        with open(self.db_path, "w", encoding="utf-8") as f:
            json.dump(self._data, f, indent=2, default=str)

    # -------------------------------------------------------------------------
    # Book CRUD Operations
    # -------------------------------------------------------------------------
    def get_book(self, isbn: str) -> Optional[Book]:
        """Read a single book by ISBN."""
        for item in self._data.get("books", []):
            if item["isbn"] == isbn:
                return Book(**item)
        return None

    def list_books(self) -> List[Book]:
        """Read all books in the catalog."""
        return [Book(**item) for item in self._data.get("books", [])]

    def insert_book(self, book: Book) -> None:
        """Create a new book record in the database."""
        if self.get_book(book.isbn):
            raise ValueError(f"Book with ISBN '{book.isbn}' already exists")
        self._data["books"].append(asdict(book))
        self.save()

    def update_book_available_copies(self, isbn: str, delta: int) -> bool:
        """Update available copies count for a book."""
        for item in self._data.get("books", []):
            if item["isbn"] == isbn:
                new_copies = item["available_copies"] + delta
                if 0 <= new_copies <= item["total_copies"]:
                    item["available_copies"] = new_copies
                    self.save()
                    return True
                return False
        return False

    def delete_book(self, isbn: str) -> bool:
        """Delete a book record by ISBN."""
        books = self._data.get("books", [])
        initial_len = len(books)
        self._data["books"] = [b for b in books if b["isbn"] != isbn]
        if len(self._data["books"]) < initial_len:
            self.save()
            return True
        return False

    # -------------------------------------------------------------------------
    # Member CRUD Operations
    # -------------------------------------------------------------------------
    def get_member(self, member_id: str) -> Optional[Member]:
        """Read a single member by member ID."""
        for item in self._data.get("members", []):
            if item["member_id"] == member_id:
                raw = dict(item)
                raw["member_type"] = MemberType(raw["member_type"])
                return Member(**raw)
        return None

    def list_members(self) -> List[Member]:
        """Read all registered members."""
        results = []
        for item in self._data.get("members", []):
            raw = dict(item)
            raw["member_type"] = MemberType(raw["member_type"])
            results.append(Member(**raw))
        return results

    def insert_member(self, member: Member) -> None:
        """Create a new member record."""
        if self.get_member(member.member_id):
            raise ValueError(f"Member '{member.member_id}' already exists")
        item = asdict(member)
        item["member_type"] = member.member_type.value
        self._data["members"].append(item)
        self.save()

    def update_member_loans(self, member_id: str, delta: int) -> bool:
        """Update active loan count for a member."""
        for item in self._data.get("members", []):
            if item["member_id"] == member_id:
                new_count = item["active_loans_count"] + delta
                if 0 <= new_count <= item["max_borrow_limit"]:
                    item["active_loans_count"] = new_count
                    self.save()
                    return True
                return False
        return False

    # -------------------------------------------------------------------------
    # Loan Record CRUD Operations
    # -------------------------------------------------------------------------
    def get_loan(self, loan_id: str) -> Optional[LoanRecord]:
        """Read a single loan record by ID."""
        for item in self._data.get("loans", []):
            if item["loan_id"] == loan_id:
                return self._deserialize_loan(item)
        return None

    def list_loans(self) -> List[LoanRecord]:
        """Read all loan records."""
        return [self._deserialize_loan(item) for item in self._data.get("loans", [])]

    def insert_loan(self, loan: LoanRecord) -> None:
        """Create a new loan record in the database."""
        loan_dict = {
            "loan_id": loan.loan_id,
            "member_id": loan.member_id,
            "isbn": loan.isbn,
            "borrow_date": loan.borrow_date.isoformat(),
            "due_date": loan.due_date.isoformat(),
            "return_date": loan.return_date.isoformat() if loan.return_date else None,
            "status": loan.status.value,
        }
        self._data["loans"].append(loan_dict)
        self.save()

    def update_loan_status(self, loan_id: str, status: LoanStatus) -> bool:
        """Update loan status and return date."""
        for item in self._data.get("loans", []):
            if item["loan_id"] == loan_id:
                item["status"] = status.value
                if status == LoanStatus.RETURNED:
                    item["return_date"] = date.today().isoformat()
                self.save()
                return True
        return False

    def delete_loan(self, loan_id: str) -> bool:
        """Delete a loan record by ID."""
        loans = self._data.get("loans", [])
        initial_len = len(loans)
        self._data["loans"] = [l for l in loans if l["loan_id"] != loan_id]
        if len(self._data["loans"]) < initial_len:
            self.save()
            return True
        return False

    def _deserialize_loan(self, item: Dict[str, Any]) -> LoanRecord:
        return LoanRecord(
            loan_id=item["loan_id"],
            member_id=item["member_id"],
            isbn=item["isbn"],
            borrow_date=date.fromisoformat(item["borrow_date"]),
            due_date=date.fromisoformat(item["due_date"]),
            return_date=date.fromisoformat(item["return_date"]) if item.get("return_date") else None,
            status=LoanStatus(item["status"]),
        )
