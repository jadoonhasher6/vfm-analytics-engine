import pandas as pd

raw_products = [
    {"product": "USB-C Hub",     "store": "Daraz",     "price": 3500, "rating": 4.2, "in_stock": True},
    {"product": "Mechanical KB", "store": "OLX",       "price": 8900, "rating": 3.8, "in_stock": False},
    {"product": "Monitor 24in",  "store": "Daraz",     "price": 42000,"rating": 4.6, "in_stock": True},
    {"product": "Webcam HD",     "store": "PakWheels", "price": 6200, "rating": 4.0, "in_stock": True},
    {"product": "USB-C Hub",     "store": "OLX",       "price": 2800, "rating": 3.5, "in_stock": True},
    {"product": "Mechanical KB", "store": "Daraz",     "price": 9500, "rating": 4.5, "in_stock": True},
]

# Task A
df = pd.DataFrame(raw_products)

# Task B
print(df)

# Task C — your turn: print only product and price columns
print(df[['product','price']])
print(df[df['store']=='Daraz'])

# Task D — your turn: filter rows where store == "Daraz"