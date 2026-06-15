import pandas as pd

daraz_raw = [
    {"product": "USB-C Hub",     "price": "3500",  "rating": 4.2, "reviews": 150, "platform": "Daraz"},
    {"product": "Mechanical KB", "price": "9500",  "rating": 4.5, "reviews": 55,  "platform": "Daraz"},
    {"product": "Webcam HD",     "price": "5800",  "rating": 4.3, "reviews": 80,  "platform": "Daraz"},
    {"product": "Monitor 24in",  "price": "42000", "rating": 4.6, "reviews": 25,  "platform": "Daraz"},
    {"product": "USB-C Hub",     "price": "3500",  "rating": 4.2, "reviews": 150, "platform": "Daraz"},
    {"product": "Headphones",    "price": "abc",   "rating": 4.1, "reviews": 200, "platform": "Daraz"},
]

olx_raw = [
    {"product": "USB-C Hub",      "price": "2800",  "rating": 3.5, "reviews": 200, "platform": "OLX"},
    {"product": "Mechanical KB",  "price": "8900",  "rating": 3.8, "reviews": 40,  "platform": "OLX"},
    {"product": "Webcam HD",      "price": "6200",  "rating": 4.0, "reviews": 60,  "platform": "OLX"},
    {"product": "  Monitor 24in", "price": "38000", "rating": 4.1, "reviews": 15,  "platform": "OLX"},
    {"product": "Headphones",     "price": None,    "rating": 3.9, "reviews": 180, "platform": "OLX"},
]

daraz_df = pd.DataFrame(daraz_raw)
olx_df   = pd.DataFrame(olx_raw)

def clean_platform_data(df):
    df['product']  = df['product'].str.strip().str.title()
    df['platform'] = df['platform'].str.strip().str.title()
    df['price']    = pd.to_numeric(df['price'], errors='coerce')
    df['price']    = df['price'].fillna(round(df['price'].mean(), 0))
    df = df.drop_duplicates(subset=['product', 'platform'])
    return df.reset_index(drop=True)

daraz_clean = clean_platform_data(daraz_df)
olx_clean   = clean_platform_data(olx_df)

merged=pd.merge(daraz_clean,olx_clean,on='product',suffixes=('_daraz','_olx'))
print(merged)

merged['cheaper_platform']=merged.apply(lambda row:'Daraz' if row['price_daraz']<row['price_olx'] else 'OLX',axis=1)
merged['better_rated']=merged.apply(lambda row:'Daraz' if row['rating_daraz']>row['rating_olx'] else 'OLX',axis=1)

merged['vfm_daraz'] = (merged['rating_daraz'] / merged['price_daraz'] * 1000).round(4)
merged['vfm_olx'] = (merged['rating_olx'] / merged['price_olx'] * 1000).round(4)

merged['better_vfm']=merged.apply(lambda row:'Daraz' if row['vfm_daraz']>row['vfm_olx'] else 'OLX',axis=1)

print("="*50)
print("    DARAZ vs OLX -- FINAL REPORT")
print("="*50)

print(f"\nTotal Products Compared: {len(merged)}")

print("\nCheaper Platform Wins:")
print(merged['cheaper_platform'].value_counts().to_string())

print("\nBetter Rated Platform Wins:")
print(merged['better_rated'].value_counts().to_string())

print("\nBetter Value Platform Wins:")
print(merged['better_vfm'].value_counts().to_string())

print(f"\nAverage Price Comparison:")
print(f"   Daraz avg price : Rs. {merged['price_daraz'].mean():,.0f}")
print(f"   OLX   avg price : Rs. {merged['price_olx'].mean():,.0f}")

print(f"\nAverage Rating Comparison:")
print(f"   Daraz avg rating: {merged['rating_daraz'].mean():.2f}")
print(f"   OLX   avg rating: {merged['rating_olx'].mean():.2f}")

print("\n" + "="*50)
print("         END OF REPORT")
print("="*50)