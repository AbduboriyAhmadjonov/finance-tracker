import db  # db.py faylidagi funksiyalarni import qilamiz

def main():
    db.create_table()  # Jadval mavjudligiga ishonch hosil qilamiz
    while True:
        print("\n=== Finance Tracker ===")
        print("1. Add transaction")
        print("2. List transactions")
        print("0. Quit")
        choice = input("Choose: ").strip()

        if choice == "0":
            print("Goodbye!")
            break
        else:
            print("You chose:", choice)


if __name__ == "__main__":
    main()

# Jadval mavjudligiga ishonch hosil qilamiz
# db.create_table()

# Bitta namuna transaction qo'shamiz (sanani YYYY-MM-DD ko'rinishida yozamiz)
# db.add_transaction(50000000, "Otam pul tashab berdi", "Kirim", "2026-06-21")

# Hammasini o'qib, chiroyli jadval ko'rinishida chiqaramiz
# transactions = db.get_all_transactions()
# print("ID  | Amount     | Category     | Date       | Description")
# print("-" * 60)
# for row in transactions:
#     print(f"#{row[0]:<3} | {row[1]:<10} | {row[3]:<12} | {row[4]:<10} | {row[2]}")

# Jami nechta transaction bor? (Mashq 1)
# print("\nJami transactionlar soni:", db.count_transactions())

# Faqat 'Kirim' kategoriyasidagi transactionlar (Mashq 3)
# print("\nFaqat Kirim kategoriyasi:")
# for row in db.get_by_category("Kirim"):
#     print(row)


