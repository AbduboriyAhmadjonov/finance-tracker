from sqlalchemy.orm import Mapped, mapped_column
from db import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column()
    category: Mapped[str | None] = mapped_column()
    description: Mapped[str | None] = mapped_column()
    date: Mapped[str] = mapped_column()