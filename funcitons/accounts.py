from datetime import date
from sqlalchemy import select
from db import SessionLocal
from models import Accounts




def create_account() -> Accounts:
    email = input("Enter your email: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    password = input("Enter your password: ")
    second_password = input("Confirm your password: ")

    if password != second_password:
        print("Passwords do not match. Please try again.")
        return None

    with SessionLocal() as session:
        new_account = Accounts(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            date=str(date.today())
        )
        session.add(new_account)
        session.commit()
        session.refresh(new_account) 
        print(f"Account created successfully for {first_name} {last_name}.")
        return new_account


def log_in() -> Accounts | None:
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    with SessionLocal() as session:
        account = session.scalars(
            select(Accounts).where(
                Accounts.email == email,
                Accounts.password == password
            )
        ).first()

        if account is None:
            print("Invalid credentials. Please try again.")
            return None

        print(f"Welcome, {account.first_name} {account.last_name}!")
        return account


def log_out() -> None:
    print("You have been logged out.")
