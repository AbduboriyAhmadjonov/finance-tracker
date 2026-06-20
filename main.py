import sqlite3  # Sqlite kutibxonasini import qilamiz


def get_connection():
    # connection yaratamiz va finance.db faylini yaratamiz
    connection = sqlite3.connect("finance.db")
    return connection


def create_table():
    conn = get_connection()  # connectionni olamiz
    # SQL Query yordamida transactions jadvalini yaratamiz, agar mavjud bo'lmasa
    conn.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            description TEXT,
            category TEXT,
            date TEXT NOT NULL
        );
    """)
    conn.commit()  # o'zgarishlarni saqlaymiz
    conn.close()  # connectionni yopamiz


def get_transactions():
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()   # actually pull the data into memory
    conn.close()
    return rows


def add_transaction(amount, description, category, date):
    conn = get_connection()
    conn.execute("INSERT INTO transactions (amount, description, category, date) VALUES (?, ?, ?, ?)",
                 (amount, description, category, date))
    conn.commit()
    conn.close()


create_table()
add_transaction(amount=50000000, description="Otam pul tashab berdi",
                category="Kirim", date="21.06.2026")
transaction = get_transactions()
print("Here is the latest transaction: ", transaction)
