from cli import (
    register_donation,
    record_distribution,
    show_inventory,
    show_donors,
)

def run_app():
    """
    Application entrypoint.
    Handles the main menu loop and routes user actions.
    """
    while True:
        print("=== Donation Inventory System ===")
        print("1) Register Donation")
        print("2) Record Distribution")
        print("3) Inventory Report")
        print("4) Donor Report")
        print("5) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            register_donation()
        elif choice == "2":
            record_distribution()
        elif choice == "3":
            show_inventory()
        elif choice == "4":
            show_donors()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1–5.\n")

def main():
    run_app()

if __name__ == "__main__":
    main()
