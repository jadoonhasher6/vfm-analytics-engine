import pandas as pd

raw_products = [
    {"product": "USB-C Hub",     "store": "Daraz",     "price": 3500, "rating": 4.2},
    {"product": "Mechanical KB", "store": "OLX",       "price": 8900, "rating": 3.8},
    {"product": "Monitor 24in",  "store": "Daraz",     "price": 42000,"rating": 4.6},
    {"product": "Webcam HD",     "store": "PakWheels", "price": 6200, "rating": 4.0},
    {"product": "USB-C Hub",     "store": "OLX",       "price": 2800, "rating": 3.5},
    {"product": "Mechanical KB", "store": "Daraz",     "price": 9500, "rating": 4.5},
]

df = pd.DataFrame(raw_products)
print(df.groupby('store')['price'].mean())
result=df.groupby('store').agg({'price':'mean','rating':'mean'})
print(result)
print(result.sort_values('price'))
df['vfm_score']=df['rating']/df['price'] *1000
print(df.groupby('store')['vfm_score'].max())