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


def add_transaction() -> None:
    amount = float(input("Enter amount: "))
    description = input("Enter description (optional): ")
    category = input("Enter category (optional): ")
    date = Date.today().isoformat()  # Get today's date in YYYY-MM-DD format

    transaction = Transaction(
        amount=amount,
        category=category,
        description=description,
        date=date
    )

    with SessionLocal() as session:
        session.add(transaction)
        session.commit()

    print("Transaction saved")


def list_transactions() -> None:
    with SessionLocal() as session:
        transactions = session.scalars(
            select(Transaction)
        ).all()

    if not transactions:
        return print("You don't have any transactions")

    print("ID   | Type   |   Amount   | Description   | Date")
    print("-" * 60)

    for transaction in transactions:
        print(
            f"{transaction.id} | "
            f"{transaction.category} | "
            f"{transaction.amount} | "
            f"{transaction.description} | "
            f"{transaction.date} | "
        )


if __name__ == "__main__":
    main()
