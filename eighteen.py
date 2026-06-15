import pandas as pd
dirty_products = [
    {"product": "SSD 512GB",  "store": "Daraz", "price": 15000, "rating": 4.5},
    {"product": "RAM 8GB",    "store": "OLX",   "price": None,  "rating": 3.8},
    {"product": "CPU Cooler", "store": "Daraz", "price": 8500,  "rating": None},
    {"product": "Mouse Pad",  "store": "Daraz", "price": 1200,  "rating": 4.1},
    {"product": "HDMI Cable", "store": "OLX",   "price": None,  "rating": None},
]
df2 = pd.DataFrame(dirty_products)
print(df2.isnull().sum())

# Task B — fill missing ratings with the column average
df2['rating'] = df2['rating'].fillna(df2['rating'].mean())

# Task C — drop rows where price is still None/NaN
df2 = df2.dropna(subset=['price'])

# Task D — print and verify
print(df2)
print(df2.isnull().sum())