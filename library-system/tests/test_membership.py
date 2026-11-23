import os
import shutil
import pytest
from models import MemberType
from services.database_service import DatabaseService
from services.membership_service import MembershipService


@pytest.fixture
def membership_svc(tmp_path):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    master_db = os.path.join(base_dir, "data", "library_db.json")
    test_db = str(tmp_path / "test_membership_db.json")
    shutil.copyfile(master_db, test_db)

    db = DatabaseService(test_db)
    return MembershipService(db)


def test_member_lookup(membership_svc):
    member = membership_svc.get_member("MEM-001")
    assert member is not None
    assert member.name == "Alice Smith"
    assert member.member_type == MemberType.STUDENT


def test_borrow_quota_allowance(membership_svc):
    # MEM-001 has 0 active loans and limit of 5
    assert membership_svc.can_borrow("MEM-001") is True


def test_blocked_member_with_high_fine(membership_svc):
    # MEM-004 has outstanding fine of $25.0 (>= $15.0 threshold)
    assert membership_svc.can_borrow("MEM-004") is False
