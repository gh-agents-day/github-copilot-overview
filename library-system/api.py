from typing import List, Optional
from fastapi import FastAPI, HTTPException, Query, status
from fastapi.responses import RedirectResponse

from models import Book, Member
from services.database_service import DatabaseService
from services.catalog_service import CatalogService
from services.membership_service import MembershipService
from services.fine_calculator import FineCalculator
from services.notification_service import NotificationService
from services.loan_service import LoanService
from schemas import (
    BookResponse,
    BookCreate,
    MemberResponse,
    MemberCreate,
    BorrowRequest,
    ReturnRequest,
    LoanResponse,
    ReturnResponse,
)

# -----------------------------------------------------------------------------
# Initialize Application & Services
# -----------------------------------------------------------------------------
app = FastAPI(
    title="Library Management System API",
    description="RESTful API for catalog management, member privileges, and book loans.",
    version="1.0.0",
)

db_service = DatabaseService()
catalog_service = CatalogService(db_service)
membership_service = MembershipService(db_service)
fine_calculator = FineCalculator()
notification_service = NotificationService()
loan_service = LoanService(
    catalog_service=catalog_service,
    membership_service=membership_service,
    fine_calculator=fine_calculator,
    notification_service=notification_service,
    db_service=db_service,
)


@app.get("/", include_in_schema=False)
def root():
    """Redirect root directly to Swagger UI documentation."""
    return RedirectResponse(url="/docs")


@app.get("/health", tags=["Health"])
def health_check():
    """Health and status endpoint."""
    return {"status": "ok", "app": "Library Management System", "version": "1.0.0"}


# -----------------------------------------------------------------------------
# Books Endpoints
# -----------------------------------------------------------------------------
@app.get("/books", response_model=List[BookResponse], tags=["Books"])
def list_books(genre: Optional[str] = Query(None, description="Optional genre filter")):
    """List all books in catalog or filter by genre."""
    if genre:
        return catalog_service.search_by_genre(genre)
    return catalog_service.list_all_books()


@app.get("/books/{isbn}", response_model=BookResponse, tags=["Books"])
def get_book(isbn: str):
    """Retrieve book details by ISBN."""
    book = catalog_service.get_book(isbn)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ISBN '{isbn}' not found.",
        )
    return book


@app.post(
    "/books",
    response_model=BookResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Books"],
)
def create_book(book_data: BookCreate):
    """Add a new book to the library catalog."""
    if db_service.get_book(book_data.isbn):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Book with ISBN '{book_data.isbn}' already exists.",
        )
    book = Book(**book_data.model_dump())
    db_service.insert_book(book)
    return book


# -----------------------------------------------------------------------------
# Members Endpoints
# -----------------------------------------------------------------------------
@app.get("/members", response_model=List[MemberResponse], tags=["Members"])
def list_members():
    """List all registered library members."""
    return membership_service.list_members()


@app.get("/members/{member_id}", response_model=MemberResponse, tags=["Members"])
def get_member(member_id: str):
    """Retrieve member record by ID."""
    member = membership_service.get_member(member_id)
    if not member:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Member '{member_id}' not found.",
        )
    return member


@app.post(
    "/members",
    response_model=MemberResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Members"],
)
def create_member(member_data: MemberCreate):
    """Register a new library member."""
    if db_service.get_member(member_data.member_id):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Member '{member_data.member_id}' already exists.",
        )
    member = Member(**member_data.model_dump())
    db_service.insert_member(member)
    return member


# -----------------------------------------------------------------------------
# Loans Endpoints
# -----------------------------------------------------------------------------
@app.get("/loans", response_model=List[LoanResponse], tags=["Loans"])
def list_loans():
    """List all active and past loan records."""
    return db_service.list_loans()


@app.post(
    "/loans/borrow",
    response_model=LoanResponse,
    status_code=status.HTTP_201_CREATED,
    tags=["Loans"],
)
def borrow_book(req: BorrowRequest):
    """Borrow a book from the library."""
    try:
        loan = loan_service.borrow_book(member_id=req.member_id, isbn=req.isbn)
        return loan
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
    except RuntimeError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))


@app.post("/loans/return", response_model=ReturnResponse, tags=["Loans"])
def return_book(req: ReturnRequest):
    """Return a borrowed book to the library."""
    try:
        loan = loan_service.return_book(loan_id=req.loan_id)
        return ReturnResponse(
            message="Book successfully returned",
            loan=LoanResponse.model_validate(loan),
            fine_amount=0.0,
        )
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
