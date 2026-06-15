import pandas as pd

orders = [
    {"order_id": 1, "customer": "Ali",     "amount": "5000", "city": "lahore"},
    {"order_id": 2, "customer": "  Sara ", "amount": "abc",  "city": "Karachi"},
    {"order_id": 3, "customer": "Bilal",   "amount": "8000", "city": "ISLAMABAD"},
    {"order_id": 4, "customer": "Ali",     "amount": "5000", "city": "lahore"},
    {"order_id": 5, "customer": "Ayesha",  "amount": None,   "city": "Peshawar"},
]

df = pd.DataFrame(orders)

# ── Missing values per column ─────────────
print("=== Missing Values ===")
print(df.isnull().sum())

# ── Duplicate rows ────────────────────────
print("\n=== Duplicates ===")
print(df.duplicated().sum(), "duplicate rows found")

# ── Data types ────────────────────────────
print("\n=== Data Types ===")
print(df.dtypes)