# db.py faylidagi funksiyalarni import qilamiz
from db import SessionLocal, create_tables
from funcitons import add_transaction, list_transactions, delete_tranaction, total_amount, search_transacions, list_by_category


def main():
    # Create tables if they don't exist
    create_tables()

    while True:
        print("\n=== Finance Tracker ===")
        print("1. Add transaction")
        print("2. List transactions")
        print("3. Delete Transaction")
        print("4. Total Amount")
        print("5. Search transactions")
        print("6. List transactions by category")
        print("0. Quit")
        choice = input("Choose: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            add_transaction()

        elif choice == "2":
            list_transactions()

        elif choice == "3":
            delete_tranaction()
        elif choice == "4":
            total_amount()

        elif choice == "5":
            search_transacions()

        elif choice == "6":
            list_by_category()

        else:
            print("You chose:", choice)


if __name__ == "__main__":
    main()
