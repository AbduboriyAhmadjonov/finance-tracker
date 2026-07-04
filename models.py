from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from db import Base


class Accounts(Base):
    __tablename__ = "accounts"

    email: Mapped[str] = mapped_column(unique=True)
    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column()
    first_name: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    date: Mapped[str] = mapped_column()


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column()
    category: Mapped[str | None] = mapped_column()
    description: Mapped[str | None] = mapped_column()
    date: Mapped[str] = mapped_column()

    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"))
    account: Mapped["Accounts"] = relationship("Accounts")
