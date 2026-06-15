import pandas as pd

orders = [
    {"order_id": 1, "customer": "Ali",     "amount": "5000", "city": "lahore"},
    {"order_id": 2, "customer": "  Sara ", "amount": "abc",  "city": "Karachi"},
    {"order_id": 3, "customer": "Bilal",   "amount": "8000", "city": "ISLAMABAD"},
    {"order_id": 4, "customer": "Ali",     "amount": "5000", "city": "lahore"},
    {"order_id": 5, "customer": "Ayesha",  "amount": None,   "city": "Peshawar"},
]

df = pd.DataFrame(orders)
df['customer']=df['customer'].str.strip()
df['city']=df['city'].str.title()
df['amount']=pd.to_numeric(df['amount'],errors='coerce')
df['amount']=df['amount'].fillna(df['amount'].mean())
df=df.drop_duplicates(subset=['customer','city','amount'])
print(df.reset_index(drop=True))
print(df)

print(df.isnull().sum())
print(df.dtypes)
print(df.duplicated().sum())
print(df.reset_index(drop=True))
