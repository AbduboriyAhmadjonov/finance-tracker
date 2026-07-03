from datetime import date
from sqlalchemy import select
from db import SessionLocal
from models import Transaction


def add_transaction() -> None:
    amount = float(input("Enter amount: "))
    description = input("Enter description (optional): ")
    category = input("Enter category (optional): ")
    # <- UnboundlocolError berar edi agaar date = date.today().isoformat() buganda chuni locol uzgaruvchi deb uylaydi python buni
    today = date.today().isoformat()

    transaction = Transaction(
        amount=amount,
        category=category,
        description=description,
        date=today
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


def delete_tranaction() -> None:
    transaction_id = int(input("Enter transaction ID to delete: "))

    with SessionLocal() as session:
        transaction = session.get(Transaction, transaction_id)

        if transaction is None:
            print("Transaction not found ")
            return
        session.delete(transaction)
        session.commit()

        print("Transaction deleted")


def total_amount() -> None:
    with SessionLocal() as session:
        transactions = session.scalars(
            select(Transaction)
        ).all()
        if not transactions:
            print("You don't have any transactions")
            return

        total = sum(t.amount for t in transactions)
        print(f"Total: {total}")


def search_transacions() -> None:
    keyword = input("Search: ")

    with SessionLocal() as session:
        transactions = session.scalars(
            select(Transaction).where(
                Transaction.description.contains(keyword))
        ).all()

        if not transactions:
            print("Nothing found")
            return

        print("ID   | Category   |   Amount   | Description   | Date")
        print("-" * 60)

        for transaction in transactions:
            print(
                f"{transaction.id} | "
                f"{transaction.category} | "
                f"{transaction.amount} | "
                f"{transaction.description} | "
                f"{transaction.date}"
            )


def list_by_category() -> None:
    category = input("Enter category: ")
    with SessionLocal() as sesson:
        transactions = sesson.scalars(
            select(Transaction).where(Transaction.category == category)
        ).all()

        if not transactions:
            print("No transactions in this category")
            return

        print("ID  | Category | Amout | Description | Date ")
        print("-" * 60)

        for transaction in transactions:
            print(
                f"{transaction.id} | "
                f"{transaction.category} | "
                f"{transaction.amount} | "
                f"{transaction.description} | "
                f"{transaction.date}"
            )
