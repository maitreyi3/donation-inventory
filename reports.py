from collections import defaultdict
from typing import List, Dict
from models import Donation, Distribution

def inventory_report(donations: List[Donation], distributions: List[Distribution]) -> Dict[str, float]:
    inventory = defaultdict(float)

    for d in donations:
        inventory[d.donation_type] += d.amount

    for dist in distributions:
        inventory[dist.donation_type] -= dist.amount

    return dict(inventory)

def donor_report(donations: List[Donation]) -> Dict[str, float]:
    totals = defaultdict(float)

    for d in donations:
        totals[d.donor] += d.amount

    return dict(totals)
