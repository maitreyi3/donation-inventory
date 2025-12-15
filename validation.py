from datetime import datetime

ALLOWED_TYPES = {"money", "food", "clothing", "medicine", "supplies"}
DATE_FORMAT = "%Y-%m-%d"

def validate_type(value: str) -> str:
    value = value.lower().strip()
    if value not in ALLOWED_TYPES:
        raise ValueError(
            f"Invalid donation type. Allowed types: {', '.join(sorted(ALLOWED_TYPES))}"
        )
    return value

def validate_amount(value: str) -> float:
    try:
        amount = float(value)
        if amount <= 0:
            raise ValueError
        return amount
    except ValueError:
        raise ValueError("Amount must be a positive number")

def parse_date(value: str):
    try:
        return datetime.strptime(value.strip(), DATE_FORMAT).date()
    except ValueError:
        raise ValueError("Date must be in YYYY-MM-DD format")
