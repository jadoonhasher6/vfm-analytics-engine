import pandas as pd
import os
import sys
print(sys.argv)
print(len(sys.argv))
if len(sys.argv) != 3:
    print("ERROR: Please provide exactly two CSV file paths.")
    sys.exit(1)

daraz_path=sys.argv[1]
olx_path=sys.argv[2]

print(f"Reading Daraz data from: {daraz_path}")
print(f"Reading OLX data from: {olx_path}")


if not os.path.exists(daraz_path):
    print(f"ERROR: Daraz file not found: {daraz_path}")
    sys.exit(1)

if not os.path.exists(olx_path):
    print(f"ERROR: OLX file not found: {olx_path}")
    sys.exit(1)

print("Both files verified. Ready to process.")
daraz_df = pd.read_csv(daraz_path)
olx_df = pd.read_csv(olx_path)

print("Daraz Data:")
print(daraz_df)
print("OLX Data:")
print(olx_df)

print("\n--- DARAZ PROFILE ---")
print(f"Shape: {daraz_df.shape}")
print(f"Columns: {list(daraz_df.columns)}")
print(f"Data Types:\n{daraz_df.dtypes}")
print(f"Missing Values:\n{daraz_df.isnull().sum()}")

print("\n--- OLX PROFILE ---")
print(f"Shape: {olx_df.shape}")
print(f"Columns: {list(olx_df.columns)}")
print(f"Data Types:\n{olx_df.dtypes}")
print(f"Missing Values:\n{olx_df.isnull().sum()}")

merged_df = pd.merge(daraz_df, olx_df, on='product', suffixes=('_daraz', '_olx'))

print("\n--- MERGED DATA ---")
print(merged_df)