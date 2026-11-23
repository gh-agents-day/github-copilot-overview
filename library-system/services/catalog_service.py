from typing import List, Optional
from models import Book
from services.database_service import DatabaseService


class CatalogService:
    """Library book catalog management service backed by JSON database."""

    def __init__(self, db_service: Optional[DatabaseService] = None):
        self.db = db_service or DatabaseService()

    def get_book(self, isbn: str) -> Optional[Book]:
        """Fetch book by ISBN from database."""
        return self.db.get_book(isbn)

    def search_by_genre(self, genre: str) -> List[Book]:
        """Fetch all books matching genre from database."""
        return [b for b in self.db.list_books() if b.genre.lower() == genre.lower()]

    def list_all_books(self) -> List[Book]:
        """List all books in catalog database."""
        return self.db.list_books()

    def is_available(self, isbn: str) -> bool:
        """Check if at least one copy is available for lending."""
        book = self.get_book(isbn)
        return book is not None and book.available_copies > 0 and not book.is_reference_only

    def decrement_copy(self, isbn: str) -> bool:
        """Decrement available copy count in database on borrow."""
        book = self.get_book(isbn)
        if book and book.available_copies > 0 and not book.is_reference_only:
            return self.db.update_book_available_copies(isbn, -1)
        return False

    def increment_copy(self, isbn: str) -> bool:
        """Increment available copy count in database on return or rollback."""
        return self.db.update_book_available_copies(isbn, 1)
