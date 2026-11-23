import uuid
from typing import Dict, Any


class NotificationService:
    """Mock notification service for overdue and checkout notices."""

    def send_notice(self, email: str, subject: str, message: str) -> Dict[str, Any]:
        """Send notification dispatch simulation."""
        if not email or "@" not in email:
            return {"success": False, "error": "Invalid email address format"}

        notice_id = f"notif_{uuid.uuid4().hex[:8]}"
        return {
            "success": True,
            "notice_id": notice_id,
            "recipient": email,
            "subject": subject,
        }
