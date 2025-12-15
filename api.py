from fastapi import FastAPI, HTTPException
from typing import List
from models import Donation, Distribution
from reports import inventory_report, donor_report
from validation import validate_type, validate_amount, parse_date

app = FastAPI(
    title="Donation Inventory API",
    description="Backend service for managing NGO donations and inventory",
    version="1.0.0",
)

# In-memory storage (shared with CLI-style logic)
donations: List[Donation] = []
distributions: List[Distribution] = []

# ----------- API Endpoints -----------

@app.post("/donations")
def create_donation(payload: dict):
    try:
        donor = payload.get("donor", "").strip()
        if not donor:
            raise ValueError("Donor name cannot be empty")

        donation_type = validate_type(payload.get("donation_type", ""))
        amount = validate_amount(str(payload.get("amount", "")))
        donation_date = parse_date(payload.get("date", ""))

        donation = Donation(donor, donation_type, amount, donation_date)
        donations.append(donation)

        return {"message": "Donation recorded", "donation": donation}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/distributions")
def create_distribution(payload: dict):
    try:
        donation_type = validate_type(payload.get("donation_type", ""))
        amount = validate_amount(str(payload.get("amount", "")))
        distribution_date = parse_date(payload.get("date", ""))

        current_inventory = inventory_report(donations, distributions).get(donation_type, 0.0)
        if amount > current_inventory:
            raise ValueError(
                f"Insufficient inventory for '{donation_type}'. Available: {current_inventory}"
            )

        distribution = Distribution(donation_type, amount, distribution_date)
        distributions.append(distribution)

        return {"message": "Distribution recorded", "distribution": distribution}

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/reports/inventory")
def get_inventory_report():
    return inventory_report(donations, distributions)


@app.get("/reports/donors")
def get_donor_report():
    return donor_report(donations)
