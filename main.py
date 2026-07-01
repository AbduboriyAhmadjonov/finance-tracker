# db.py faylidagi funksiyalarni import qilamiz
from sqlalchemy import Date, select
from model import Transaction
from db import SessionLocal, create_tables


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
            break
        elif choice == "2":
            list_transactions()
            break
        elif choice == "3":
            pass
            break
        elif choice == "4":
            pass
            break
        elif choice == "5":
            pass
            break
        elif choice == "6":
            pass
            break
        else:
            print("You chose:", choice)



if __name__ == "__main__":
    main()
