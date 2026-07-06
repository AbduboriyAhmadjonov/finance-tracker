from datetime import date
from sqlalchemy import func, select
from db import SessionLocal
from models import Transaction


def add_transaction(account_id: int) -> None:
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid number")
        return
    if amount <= 0:
        print("Amount must be positive.")
        return
    description = input("Enter description (optional): ")
    category = input("Enter category (optional): ")
    # <- UnboundlocolError berar edi agaar date = date.today().isoformat() buganda chuni locol uzgaruvchi deb uylaydi python buni
    today = date.today().isoformat()

    transaction = Transaction(
        amount=amount,
        category=category,
        description=description,
        date=today,
        account_id=account_id,
    )

    with SessionLocal() as session:
        session.add(transaction)
        session.commit()

    print("Transaction saved")


def list_transactions(account_id: int) -> None:
    with SessionLocal() as session:
        transactions = session.scalars(
            select(Transaction).where(Transaction.account_id == account_id)
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


def delete_tranaction(account_id: int) -> None:
    transaction_id = int(input("Enter transaction ID to delete: "))

    with SessionLocal() as session:
        transaction = session.get(Transaction, transaction_id)

        if transaction is None or transaction.account_id != account_id:
            print("Transaction not found ")
            return
        session.delete(transaction)
        session.commit()

        print("Transaction deleted")


def total_amount(account_id: int) -> None:
    with SessionLocal() as session:
        total = session.scalar(
            select(func.sum(Transaction.amount)).where(
                Transaction.account_id == account_id
            )
        )

        if total is None:
            print("No transactions found")
            return

        print(f"Total amount: {total}")


def search_transacions(account_id: int) -> None:
    keyword = input("Search: ")

    with SessionLocal() as session:
        transactions = session.scalars(
            select(Transaction).where(
                Transaction.account_id == account_id,
                Transaction.description.contains(keyword),
            )
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


def list_by_category(account_id: int) -> None:
    category = input("Enter category: ")
    with SessionLocal() as sesson:
        transactions = sesson.scalars(
            select(Transaction).where(
                Transaction.account_id == account_id, Transaction.category == category
            )
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
