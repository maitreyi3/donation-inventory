from dataclasses import dataclass
from datetime import date

@dataclass
class Donation:
    donor: str
    donation_type: str
    amount: float
    donation_date: date

@dataclass
class Distribution:
    donation_type: str
    amount: float
    distribution_date: date
