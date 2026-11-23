from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Optional


class MemberType(Enum):
    STUDENT = "STUDENT"
    FACULTY = "FACULTY"
    REGULAR = "REGULAR"


class LoanStatus(Enum):
    ACTIVE = "ACTIVE"
    RETURNED = "RETURNED"
    OVERDUE = "OVERDUE"


@dataclass
class Book:
    isbn: str
    title: str
    author: str
    genre: str
    total_copies: int = 1
    available_copies: int = 1
    is_reference_only: bool = False


@dataclass
class Member:
    member_id: str
    name: str
    email: str
    member_type: MemberType = MemberType.REGULAR
    max_borrow_limit: int = 3
    active_loans_count: int = 0
    outstanding_fine: float = 0.0


@dataclass
class LoanRecord:
    loan_id: str
    member_id: str
    isbn: str
    borrow_date: date
    due_date: date
    return_date: Optional[date] = None
    status: LoanStatus = LoanStatus.ACTIVE
