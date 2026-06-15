import pandas as pd

raw_products = [
    {"product": "USB-C Hub",     "store": "Daraz",     "price": 3500, "rating": 4.2, "in_stock": True},
    {"product": "Mechanical KB", "store": "OLX",       "price": 8900, "rating": 3.8, "in_stock": False},
    {"product": "Monitor 24in",  "store": "Daraz",     "price": 42000,"rating": 4.6, "in_stock": True},
    {"product": "Webcam HD",     "store": "PakWheels", "price": 6200, "rating": 4.0, "in_stock": True},
    {"product": "USB-C Hub",     "store": "OLX",       "price": 2800, "rating": 3.5, "in_stock": True},
    {"product": "Mechanical KB", "store": "Daraz",     "price": 9500, "rating": 4.5, "in_stock": True},
]
df=pd.DataFrame(raw_products)
print(df[df['price']<7000])
print(df[(df['price']<7000) & (df['rating']>3.9)])
df['vfm_score']=df['rating']/df['price']*1000
print(df['vfm_score'].max())