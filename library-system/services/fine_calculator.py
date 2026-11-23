from typing import Tuple
from models import MemberType


class FineCalculator:
    """Calculates overdue fines based on loan duration and member type."""

    BASE_DAILY_RATE = 0.50  # $0.50 per day overdue
    MAX_FINE = 50.0         # Capped at $50.00
