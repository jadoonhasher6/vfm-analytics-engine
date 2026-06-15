import pandas as pd
import numpy as np

# =====================================================================
# 1. INGESTION LAYER (Raw Scraped Data)
# =====================================================================
daraz_data = {
    'product_name': ['Running Shoes ', 'smart watches', ' Leather Bags'],
    'price': ['5000', '15000', '8000'],
    'rating': [4.2, 4.5, 3.9]
}
olx_data = {
    'product_name': ['running shoes', 'Smart Watches ', 'leather bags'],
    'price': ['4500', 'not available', '7500'],
    'rating': [4.0, 4.1, 3.8]
}

df_daraz = pd.DataFrame(daraz_data)
df_olx = pd.DataFrame(olx_data)

# =====================================================================
# 2. CLEANING & TRANSFORMATION LAYER (Day 7 Pipeline)
# =====================================================================
# Standardize product names for exact merging matches
df_daraz['product_name'] = df_daraz['product_name'].str.strip().str.title()
df_olx['product_name'] = df_olx['product_name'].str.strip().str.title()

# Safely coerce non-numeric strings to NaN values
df_daraz['price'] = pd.to_numeric(df_daraz['price'], errors='coerce')
df_olx['price'] = pd.to_numeric(df_olx['price'], errors='coerce')

# Merge sources side-by-side using platform-specific suffixes
merged_df = pd.merge(df_daraz, df_olx, on='product_name', suffixes=('_daraz', '_olx'))

# =====================================================================
# 3. ANALYTICS ENGINE LAYER (Day 8 Row-Wise Logic)
# =====================================================================

# Pricing Matrix Decision Logic
def determine_cheaper(row):
    p_daraz = row['price_daraz']
    p_olx = row['price_olx']
    
    if pd.isna(p_daraz) and pd.isna(p_olx): return 'Unknown'
    elif pd.isna(p_daraz): return 'OLX'
    elif pd.isna(p_olx): return 'Daraz'
    elif p_daraz < p_olx: return 'Daraz'
    elif p_olx < p_daraz: return 'OLX'
    else: return 'Tie'

# Ratings Matrix Decision Logic
def determine_better_rated(row):
    r_daraz = row['rating_daraz']
    r_olx = row['rating_olx']
    
    if pd.isna(r_daraz) and pd.isna(r_olx): return 'Unknown'
    elif pd.isna(r_daraz): return 'OLX'
    elif pd.isna(r_olx): return 'Daraz'
    elif r_daraz > r_olx: return 'Daraz'
    elif r_olx > r_daraz: return 'OLX'
    else: return 'Tie'

# Execute row-by-row mapping
merged_df['cheaper_platform'] = merged_df.apply(determine_cheaper, axis=1)
merged_df['better_rated'] = merged_df.apply(determine_better_rated, axis=1)

# =====================================================================
# 4. VERIFICATION REPORT
# =====================================================================
print("\n" + "="*65)
print("             VFM PIPELINE DECISION REPORT (DAY 8)")
print("="*65)
columns_to_show = ['product_name', 'price_daraz', 'price_olx', 'cheaper_platform', 'better_rated']
print(merged_df[columns_to_show].to_string(index=False))
print("="*65)