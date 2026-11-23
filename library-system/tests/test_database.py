import os
import shutil
import pytest
from models import Book
from services.database_service import DatabaseService


@pytest.fixture
def test_db(tmp_path):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    master_db = os.path.join(base_dir, "data", "library_db.json")
    temp_db_path = str(tmp_path / "mock_db.json")
    shutil.copyfile(master_db, temp_db_path)
    return DatabaseService(temp_db_path)


def test_database_read_books(test_db):
    books = test_db.list_books()
    assert len(books) >= 5
    book = test_db.get_book("978-0132350884")
    assert book is not None
    assert book.title == "Clean Code"


def test_database_insert_and_delete_book(test_db):
    new_book = Book(
        isbn="978-1449355730",
        title="Learning Python",
        author="Mark Lutz",
        genre="Programming",
        total_copies=2,
        available_copies=2,
    )
    # Create (Insert)
    test_db.insert_book(new_book)
    retrieved = test_db.get_book("978-1449355730")
    assert retrieved is not None
    assert retrieved.title == "Learning Python"

    # Delete
    deleted = test_db.delete_book("978-1449355730")
    assert deleted is True
    assert test_db.get_book("978-1449355730") is None


def test_database_update_copies(test_db):
    isbn = "978-0134685991"
    initial_copies = test_db.get_book(isbn).available_copies

    # Decrement copy (Update)
    updated = test_db.update_book_available_copies(isbn, -1)
    assert updated is True
    assert test_db.get_book(isbn).available_copies == initial_copies - 1
