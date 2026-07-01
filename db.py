from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# 1. The engine: our connection to the database file.
engine = create_engine("sqlite:///finance.db", echo=False)


class Base(DeclarativeBase):
    pass


# 3. The Session factory: makes "workspaces" for reading/writing.
SessionLocal = sessionmaker(bind=engine)

# - **Engine** = the database connection. `sqlite:///finance.db` is a database URL ("use SQLite, file finance.db").
# - **Base** = a parent class. Every table we define inherits from it, and Base remembers them all.
# - **Session** = your workspace. You open one, add/read objects, commit, close. `SessionLocal` is a factory that makes them.


# Next: temporarily use `create_engine("sqlite:///finance.db", echo=True)`. Now SQLAlchemy prints the real SQL it runs. Showing "it's still SQL underneath". Turn it off later.


# Creates tables in the database if they don't exist yet
def create_tables():
    Base.metadata.create_all(engine)
