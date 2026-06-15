import pandas as pd

# Raw Daraz Data
daraz_data = {
    'product_name': ['Running Shoes ', 'smart watches', ' Leather Bags'],
    'price': ['5000', '15000', '8000'],
    'rating': [4.2, 4.5, 3.9]
}
df_daraz = pd.DataFrame(daraz_data)

# Raw OLX Data
olx_data = {
    'product_name': ['running shoes', 'Smart Watches ', 'leather bags'],
    'price': ['4500', 'not available', '7500'], # Notice the dirty text 'not available'
    'rating': [4.0, 4.1, 3.8]
}
df_olx = pd.DataFrame(olx_data)

df_daraz['product_name']=df_daraz['product_name'].str.strip().str.title()
df_olx['product_name']=df_olx['product_name'].str.strip().str.title()

suffixes=('_daraz','_olx')
df_daraz['price']=pd.to_numeric(df_daraz['price'],errors='coerce')
df_olx['price']=pd.to_numeric(df_olx['price'],errors='coerce')

merged_df = pd.merge(df_daraz, df_olx, on='product_name', suffixes=suffixes)
print(merged_df)



