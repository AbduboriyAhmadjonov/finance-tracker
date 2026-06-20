# Personal Finance Tracker — Feature Plan

A roadmap of features to build, staged by difficulty. The course adds one small
thing at a time, so work top to bottom — each item teaches one new idea.

## 🟢 Core (the foundation)
The must-haves that make it a real tracker.

- [ ] **Add a transaction** — amount, type (income/expense), category, date, note
- [ ] **List all transactions** — print them in a clean table
- [ ] **Categories** — Food, Transport, Rent, Salary… (fixed list first, own table later)
- [ ] **Current balance** — total income − total expenses
- [ ] **Edit / delete a transaction** — by its ID (teaches UPDATE and DELETE)
- [ ] **Search / filter** — "show only Food", "show only this month"

## 🟡 Reports & insight
What makes a finance app actually useful.

- [ ] **Monthly summary** — total spent, total earned, net for a given month
- [ ] **Spending by category** — "Food: 320, Transport: 90…" (GROUP BY)
- [ ] **Biggest expenses** — top 5 transactions this month
- [ ] **Budget per category** — set a limit (Food = 400) and warn when over
- [ ] **Daily average spend** — and a projection for the rest of the month
- [ ] **Compare months** — "you spent 15% more than last month"

## 🟠 Quality-of-life features

- [ ] **Recurring transactions** — rent/salary auto-added each month
- [ ] **Multiple accounts / wallets** — Cash, Card, Savings
- [ ] **Currency support** — store amounts with a currency (UZS + USD)
- [ ] **CSV import/export** — import a bank statement, export for Excel
- [ ] **Tags** — flexible labels beyond categories (#vacation, #work)
- [ ] **Savings goals** — "Save 5,000,000 for a laptop" with progress

## 🔵 Advanced / portfolio polish

- [ ] **Charts** — pie chart of spending with matplotlib
- [ ] **Command-line menu** — interactive app (1) Add  2) Report  3) Quit)
- [ ] **Web version** — expose it with Flask/FastAPI, a simple webpage
- [ ] **Reminders** — "you haven't logged anything in 3 days"
- [ ] **Insights / alerts** — "unusual spending on Transport this week"

---

### Suggested order for now
Start with the 🟢 Core items in this order — each builds on the last:

`add transaction → list transactions → balance → categories → edit/delete → filter`
