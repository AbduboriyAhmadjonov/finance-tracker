# db.py faylidagi funksiyalarni import qilamiz
from db import SessionLocal, create_tables
from funcitons.accounts import create_account, log_in
from funcitons.transactions import (
    add_transaction,
    list_transactions,
    delete_tranaction,
    total_amount,
    search_transacions,
    list_by_category,
)


def main():
    # Create tables if they don't exist
    create_tables()
    account = None

    while True:
        if account is None:
            print("\n=== Finance Tracker ===")
            print("1. Create Account")
            print("2. Login In")
            print("0. Quit")
            choice = input("Choice: ").strip()

            if choice == "0":
                print("Good Bye!")
                break
            elif choice == "1":
                account = create_account()
            elif choice == "2":
                account = log_in()
            else:
                print("Unknown choice:", choice)

        else:
            print(f"\n=== Finance Tracket - {account.first_name} ===")
            print("1. Add transaction")
            print("2. List transactions")
            print("3. Delete Transaction")
            print("4. Total Amount")
            print("5. Search transactions")
            print("6. List transactions by category")
            print("7. Log Out")
            print("0. Quit")
            choice = input("Choose: ").strip()

            if choice == "0":
                print("Goodbye!")
                break
            elif choice == "1":
                add_transaction(account.id)
            elif choice == "2":
                list_transactions(account.id)
            elif choice == "3":
                delete_tranaction(account.id)
            elif choice == "4":
                total_amount(account.id)
            elif choice == "5":
                search_transacions(account.id)
            elif choice == "6":
                list_by_category(account.id)
            elif choice == "7":
                account = None
                print("You have been logged out.")
            else:
                print("Unknown choice:", choice)


if __name__ == "__main__":
    main()
