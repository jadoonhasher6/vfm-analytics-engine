import pandas as pd
import os
import sys
def load_data(daraz_path,olx_path):
    daraz_data =pd.read_csv(daraz_path)
    olx_data = pd.read_csv(olx_path)
    print('data loading completed')
    return daraz_data,olx_data

def validate_inputs():
    if len(sys.argv) != 3:
        print("ERROR: Please provide exactly two CSV file paths.")
        sys.exit(1)
    
    daraz_path = sys.argv[1]
    olx_path = sys.argv[2]
    
    if not os.path.exists(daraz_path):
        print(f"ERROR: Daraz file not found: {daraz_path}")
        sys.exit(1)
    
    if not os.path.exists(olx_path):
        print(f"ERROR: OLX file not found: {olx_path}")
        sys.exit(1)
    
    return daraz_path, olx_path

def merge_data(daraz_data,olx_data):
    merged_data = pd.merge(daraz_data, olx_data, on='product', suffixes=('_daraz', '_olx'))
    print('merged data',merged_data)
    return merged_data

def smart_vfm(row):
    max_price = max(row['price_daraz'], row['price_olx'])
    max_rating = max(row['rating_daraz'], row['rating_olx'])
    daraz_price_score = 1 - row['price_daraz'] / max_price
    olx_price_score = 1 - row['price_olx'] / max_price
    daraz_rating_score = row['rating_daraz'] / max_rating
    olx_rating_score = row['rating_olx'] / max_rating
    daraz_score = (0.6 * daraz_price_score) + (0.4 * daraz_rating_score)
    olx_score = (0.6 * olx_price_score) + (0.4 * olx_rating_score)

    if daraz_score > olx_score:
        return 'Daraz'
    elif olx_score > daraz_score:
        return 'OLX'
    else:
        return 'Tie'
    
def calculate_vfm(merged_data):
    merged_data['best_value'] = merged_data.apply(smart_vfm, axis=1)
    print('vfm winners:', merged_data['best_value'].value_counts())
    return merged_data

def generate_report(merged_data):
    report = merged_data[['product', 'price_daraz', 'rating_daraz', 'price_olx', 'rating_olx', 'best_value']]
    report.to_excel('vfm_score_report.xlsx',index=False)
    print('Report generated: vfm_score_report.xlsx')

def main():
    daraz_path, olx_path = validate_inputs()
    daraz_data, olx_data = load_data(daraz_path, olx_path)
    merged_data = merge_data(daraz_data, olx_data)
    merged_data_with_vfm = calculate_vfm(merged_data)
    generate_report(merged_data_with_vfm)

main()