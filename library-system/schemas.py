from datetime import date
from typing import Optional, List
from pydantic import BaseModel, ConfigDict, Field
from models import MemberType, LoanStatus


class BookBase(BaseModel):
    isbn: str = Field(..., description="Unique ISBN of the book")
    title: str = Field(..., description="Title of the book")
    author: str = Field(..., description="Author name")
    genre: str = Field(..., description="Book genre/category")
    total_copies: int = Field(1, ge=1, description="Total inventory count")
    available_copies: int = Field(1, ge=0, description="Available copies for borrowing")
    is_reference_only: bool = Field(False, description="Whether book is restricted to in-library use")


class BookCreate(BookBase):
    pass


class BookResponse(BookBase):
    model_config = ConfigDict(from_attributes=True)


class MemberBase(BaseModel):
    member_id: str = Field(..., description="Unique member identifier")
    name: str = Field(..., description="Full member name")
    email: str = Field(..., description="Contact email")
    member_type: MemberType = Field(MemberType.REGULAR, description="Member membership type")
    max_borrow_limit: int = Field(3, ge=1, description="Max simultaneous loans allowed")
    active_loans_count: int = Field(0, ge=0, description="Currently active loan count")
    outstanding_fine: float = Field(0.0, ge=0.0, description="Outstanding balance in fines")


class MemberCreate(MemberBase):
    pass


class MemberResponse(MemberBase):
    model_config = ConfigDict(from_attributes=True)


class BorrowRequest(BaseModel):
    member_id: str = Field(..., description="ID of the member requesting the loan")
    isbn: str = Field(..., description="ISBN of the book to checkout")


class ReturnRequest(BaseModel):
    loan_id: str = Field(..., description="ID of the loan record being returned")


class LoanResponse(BaseModel):
    loan_id: str
    member_id: str
    isbn: str
    borrow_date: date
    due_date: date
    return_date: Optional[date] = None
    status: LoanStatus

    model_config = ConfigDict(from_attributes=True)


class ReturnResponse(BaseModel):
    message: str
    loan: LoanResponse
    fine_amount: float
