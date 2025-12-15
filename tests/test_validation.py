import pytest
from validation import validate_type, validate_amount, parse_date

def test_validate_type_valid():
    assert validate_type("food") == "food"

def test_validate_type_invalid():
    with pytest.raises(ValueError):
        validate_type("invalid")

def test_validate_amount_valid():
    assert validate_amount("10") == 10.0

def test_validate_amount_invalid():
    with pytest.raises(ValueError):
        validate_amount("-5")

def test_parse_date_valid():
    d = parse_date("2025-12-14")
    assert str(d) == "2025-12-14"

def test_parse_date_invalid():
    with pytest.raises(ValueError):
        parse_date("14-12-2025")
