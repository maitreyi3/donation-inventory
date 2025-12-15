from typing import List
from models import Donation, Distribution
from reports import inventory_report, donor_report
from validation import (
    validate_type,
    validate_amount,
    parse_date,
    ALLOWED_TYPES,
)

# In-memory storage
donations: List[Donation] = []
distributions: List[Distribution] = []

# ---- Prompt Helpers (re-prompt on failure) ----
def prompt_donation_type() -> str:
    while True:
        try:
            return validate_type(
                input(
                    f"Donation type ({' / '.join(sorted(ALLOWED_TYPES))}): "
                )
            )
        except ValueError as e:
            print(f"❌ {e}")

def prompt_amount(label: str) -> float:
    while True:
        try:
            return validate_amount(input(label))
        except ValueError as e:
            print(f"❌ {e}")

def prompt_date():
    while True:
        try:
            return parse_date(input("Date (YYYY-MM-DD): "))
        except ValueError as e:
            print(f"❌ {e}")

# ---- Actions ----
def register_donation():
    donor = input("Donor name: ").strip()
    if not donor:
        print("❌ Donor name cannot be empty\n")
        return

    donation_type = prompt_donation_type()
    amount = prompt_amount("Amount: ")
    donation_date = prompt_date()

    donations.append(Donation(donor, donation_type, amount, donation_date))
    print("✅ Donation registered\n")

def record_distribution():
    donation_type = prompt_donation_type()
    amount = prompt_amount("Amount distributed: ")
    distribution_date = prompt_date()

    current_inventory = inventory_report(donations, distributions).get(donation_type, 0.0)
    if amount > current_inventory:
        print(
            f"❌ Insufficient inventory for '{donation_type}'. "
            f"Available: {current_inventory}\n"
        )
        return

    distributions.append(
        Distribution(donation_type, amount, distribution_date)
    )
    print("✅ Distribution recorded\n")

def show_inventory():
    report = inventory_report(donations, distributions)

    print("\n📦 Inventory Report")
    print("-" * 30)

    if not report:
        print("No inventory available\n")
        return

    for k in sorted(report):
        print(f"{k}: {report[k]}")
    print()

def show_donors():
    report = donor_report(donations)

    print("\n👤 Donor Report")
    print("-" * 30)

    if not report:
        print("No donations recorded\n")
        return

    for k in sorted(report):
        print(f"{k}: {report[k]}")
    print()
