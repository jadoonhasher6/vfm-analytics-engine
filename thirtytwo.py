import pandas as pd

# This is what REAL scraped data looks like — messy!
raw_data = [
    {"product": "USB-C Hub",     "price": "3500",  "rating": 4.2,  "platform": "Daraz"},
    {"product": "usb-c hub",     "price": "3500",  "rating": 4.2,  "platform": "Daraz"},
    {"product": "Mechanical KB", "price": None,    "rating": 3.8,  "platform": "OLX"},
    {"product": "Webcam HD",     "price": "6200",  "rating": None, "platform": "daraz"},
    {"product": "Monitor 24in",  "price": "42000", "rating": 4.6,  "platform": "Daraz"},
    {"product": "  Webcam HD ",  "price": "6200",  "rating": None, "platform": "Daraz"},
    {"product": "USB-C Hub",     "price": "abc",   "rating": 4.2,  "platform": "OLX"},
]
df=pd.DataFrame(raw_data)
print(df)
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.dtypes)