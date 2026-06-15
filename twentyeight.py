import pandas as pd

products = pd.DataFrame([
    {"product_id": 1, "name": "USB-C Hub",     "price": 3500},
    {"product_id": 2, "name": "Mechanical KB", "price": 8900},
    {"product_id": 3, "name": "Webcam HD",     "price": 6200},
    {"product_id": 4, "name": "Monitor 24in",  "price": 42000},
])

reviews = pd.DataFrame([
    {"product_id": 1, "rating": 4.2, "review_count": 150},
    {"product_id": 2, "rating": 3.8, "review_count": 40},
    {"product_id": 3, "rating": 4.5, "review_count": 95},
])

# Left join
merged = pd.merge(products, reviews, on='product_id', how='left')
merged_filled=merged.fillna(0)
print(merged_filled)
merged_filled['vfm_score'] = (merged_filled['rating'] / merged_filled['price'] * 1000).round(4)
print("\n=== With VFM Score ===")
print(merged_filled)