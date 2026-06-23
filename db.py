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


def add_transaction(amount, description, category, date):
    conn = get_connection()
    # ? placeholderlar SQL injectiondan himoya qiladi — har doim shulardan foydalanamiz
    conn.execute(
        "INSERT INTO transactions (amount, description, category, date) VALUES (?, ?, ?, ?)",
        (amount, description, category, date),
    )
    conn.commit()
    conn.close()


def get_all_transactions():
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM transactions")
    rows = cursor.fetchall()   # ma'lumotlarni xotiraga olib kelamiz
    conn.close()
    return rows


# --- Dars 2 mashqlari ---

def count_transactions():
    # jadvalda nechta qator (transaction) borligini qaytaradi
    conn = get_connection()
    cursor = conn.execute("SELECT COUNT(*) FROM transactions")
    count = cursor.fetchone()[0]  # fetchone bitta qator qaytaradi, masalan (5,)
    conn.close()
    return count


def get_by_category(category):
    # faqat berilgan kategoriyadagi transactionlarni qaytaradi
    conn = get_connection()
    cursor = conn.execute("SELECT * FROM transactions WHERE category = ?", (category,))
    rows = cursor.fetchall()
    conn.close()
    return rows
