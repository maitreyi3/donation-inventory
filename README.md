# Donation Inventory System

A backend-focused system for managing NGO donations, distributions, and inventory.

## Design Focus

This solution intentionally emphasizes backend engineering fundamentals:
- Clear domain modeling for donations and distributions
- Inventory treated as derived state (inflow − outflow)
- Centralized validation and defensive error handling
- Separation of concerns between API, CLI, validation, and business logic
- Automated unit and API tests

## Architecture Overview

- main.py: application entrypoint
- cli.py: command-line user interaction
- api.py: REST API (FastAPI)
- validation.py: domain validation rules
- models.py: domain entities
- reports.py: business logic
- tests/: unit and API tests

## Running the CLI
```bash
python main.py
