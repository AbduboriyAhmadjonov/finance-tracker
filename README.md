# Project: "Personal Finance Flow"

**Til / Language:** Python
**Kun / Day:** 01 — Setup and First Database

---

## 🎯 Maqsad (Goal)

Pul **kirgani** (income) va **chiqqanini** (expense) nazorat qiluvchi dastur.
Foydalanuvchi o'z pulini kuzatadi va **haftalik / oylik** sarflar tarixini ko'radi.

> Asosiy savol: *"Mening pulim qayerga ketyapti?"*

---

## 🧩 Asosiy imkoniyatlar (Features)

| # | Imkoniyat | Tavsif |
|---|-----------|--------|
| 0 | Akkount yaratish | Foydalanuvchi nomi bilan yangi akkount ochish |
| 1 | Pul kiritish (income) | Balansga pul qo'shish (masalan: oylik, sovg'a) |
| 2 | Pul ishlatish (expense) | Sarflangan pulni yozib qo'yish (masalan: ovqat, transport) |
| 3 | Balansni ko'rish | Hozirgi qoldiq = jami kirim − jami chiqim |
| 4 | Tarix (history) | Barcha kirim/chiqim yozuvlari ro'yxati |
| 5 | Hisobot (report) | Haftalik yoki oylik sarflar yig'indisi |

---

## 🗄️ Ma'lumotlar bazasi (Database — SQLite)

Bugungi dars markazi: **birinchi baza** bilan ishlash (SQLite).

### Jadval: `accounts`
| Ustun | Tip | Izoh |
|-------|-----|------|
| id | INTEGER | Primary key |
| name | TEXT | Akkount nomi (unique) |
| created | TEXT | Yaratilgan sana |

### Jadval: `transactions`
| Ustun | Tip | Izoh |
|-------|-----|------|
| id | INTEGER | Primary key |
| account_id | INTEGER | Qaysi akkountga tegishli (foreign key) |
| type | TEXT | `'income'` yoki `'expense'` |
| amount | REAL | Pul miqdori (musbat son) |
| category | TEXT | Toifa: ovqat, transport, oylik... |
| note | TEXT | Qo'shimcha izoh (ixtiyoriy) |
| created | TEXT | Yozuv sanasi |

**Balans formulasi:** `balance = SUM(income) − SUM(expense)`

---

## ✅ Bugungi vazifalar (Day-01 Tasks)

- [ ] **0.** SQLite bazaga ulanish va jadvallarni yaratish (`accounts`, `transactions`)
- [ ] **1.** Akkount yaratish funksiyasi
- [ ] **2.** Pul kiritish (income qo'shish)
- [ ] **3.** Pul ishlatish (expense qo'shish)
- [ ] **4.** Balansni hisoblash va chiqarish
- [ ] **5.** Oddiy CLI menyu (terminal orqali boshqarish)

> Keyingi kunlar uchun: haftalik/oylik hisobot, toifalar bo'yicha statistika.

---

## 📁 Rejalashtirilgan fayllar (Planned files)

```
finance-tracker/
├── README.md       # ushbu reja
├── database.py     # SQLite: ulanish, jadvallar, CRUD funksiyalari
├── main.py         # CLI menyu — foydalanuvchi bilan muloqot
└── finance.db      # SQLite bazasi (avtomatik yaratiladi)
```

---

## ▶️ Ishga tushirish (How to run)

```bash
python main.py
```

> Talab: Python 3.8+ (qo'shimcha kutubxona shart emas — `sqlite3` Python ichida bor).
