from models import Donation, Distribution
from reports import inventory_report, donor_report
from datetime import date

def test_inventory_report():
    donations = [
        Donation("Alice", "food", 10, date.today()),
        Donation("Bob", "food", 5, date.today()),
    ]
    distributions = [
        Distribution("food", 6, date.today())
    ]

    report = inventory_report(donations, distributions)
    assert report["food"] == 9

def test_donor_report():
    donations = [
        Donation("Alice", "food", 10, date.today()),
        Donation("Alice", "money", 20, date.today()),
    ]

    report = donor_report(donations)
    assert report["Alice"] == 30
