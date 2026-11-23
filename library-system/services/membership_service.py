from typing import List, Optional
from models import Member, MemberType
from services.database_service import DatabaseService


class MembershipService:
    """Manages member accounts, privileges, and borrowing limits via database."""

    LIMITS_BY_TYPE = {
        MemberType.STUDENT: 5,
        MemberType.FACULTY: 10,
        MemberType.REGULAR: 3,
    }

    def __init__(self, db_service: Optional[DatabaseService] = None):
        self.db = db_service or DatabaseService()

    def get_member(self, member_id: str) -> Optional[Member]:
        """Fetch member by ID from database."""
        return self.db.get_member(member_id)

    def list_members(self) -> List[Member]:
        """List all registered members from database."""
        return self.db.list_members()

    def can_borrow(self, member_id: str) -> bool:
        """Verify member has remaining borrow quota and no outstanding fine >= $15.0."""
        member = self.get_member(member_id)
        if not member:
            return False
        if member.outstanding_fine >= 15.0:
            return False
        return member.active_loans_count < member.max_borrow_limit

    def register_loan(self, member_id: str) -> bool:
        """Increment active loan count for member in database if within limits."""
        if self.can_borrow(member_id):
            return self.db.update_member_loans(member_id, 1)
        return False

    def close_loan(self, member_id: str) -> bool:
        """Decrement active loan count on book return in database."""
        return self.db.update_member_loans(member_id, -1)
