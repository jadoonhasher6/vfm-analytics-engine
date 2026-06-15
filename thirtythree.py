import pandas as pd

raw_data = [
    {"product": "USB-C Hub",     "price": "3500",  "rating": 4.2,  "platform": "Daraz"},
    {"product": "usb-c hub",     "price": "3500",  "rating": 4.2,  "platform": "Daraz"},
    {"product": "Mechanical KB", "price": None,    "rating": 3.8,  "platform": "OLX"},
    {"product": "Webcam HD",     "price": "6200",  "rating": None, "platform": "daraz"},
    {"product": "Monitor 24in",  "price": "42000", "rating": 4.6,  "platform": "Daraz"},
    {"product": "  Webcam HD ",  "price": "6200",  "rating": None, "platform": "Daraz"},
    {"product": "USB-C Hub",     "price": "abc",   "rating": 4.2,  "platform": "OLX"},
]

df = pd.DataFrame(raw_data)
df['product']=df['product'].str.strip()
df['product']=df['product'].str.title()
df['platform']=df['platform'].str.title()
print(df[['product', 'platform']])
df['price']=pd.to_numeric(df['price'],errors='coerce')
print(df['price'])

avg_price=df['price'].mean()
avg_rating=df['rating'].mean()

df['price']=df['price'].fillna(avg_price)
df['rating']=df['rating'].fillna(avg_rating)

df=df.drop_duplicates(subset=['product','platform'])
print(df.reset_index(drop=True))

df['price']=df['price'].astype(int)
print("\n=== Final Clean Data ===")
print(df.reset_index(drop=True))
print("\n=== Final Data Types ===")
print(df.dtypes)
