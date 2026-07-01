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

    print("-" * 60)
