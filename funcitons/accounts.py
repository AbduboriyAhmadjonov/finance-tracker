from datetime import date
from sqlalchemy import select
from db import SessionLocal
from models import Accounts
from auth import hash_password, verify_hash


def create_account() -> Accounts:
    email = input("Enter your email: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    password = input("Enter your password: ")
    second_password = input("Confirm your password: ")
    if not email or "@" not in email:
        print("Invalid email")
        return None

    if password != second_password:
        print("Passwords do not match. Please try again.")
        return None

    with SessionLocal() as session:
        account = session.scalars(
            select(Accounts).where(
                Accounts.email == email
            )
        ).first()

    if account:
        print("An account with this email already exists. Please log in.")
        return None

    # Hash the password and convert to hex
    hashed_password = hash_password(password).hex()

    with SessionLocal() as session:
        new_account = Accounts(
            email=email,
            password=hashed_password,
            first_name=first_name,
            last_name=last_name,
            date=str(date.today()),
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
                Accounts.email == email
            )
        ).first()

        print(
            f"Account found: {account.first_name} {account.last_name}" if account else "No account found with that email.")

        if account is None or not verify_hash(password=password, hash_hex=account.password):
            print("Invalid credentials. Please try again.")
            return None

        print(f"Welcome, {account.first_name} {account.last_name}!")
        return account


def log_out() -> None:
    print("You have been logged out.")
