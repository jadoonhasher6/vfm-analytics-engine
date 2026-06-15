raw_data = "  2023-05-01 ,  Sales_Data ,  1500  "
split_data=raw_data.split(',')
clean_data=[item.strip() for item in split_data]
print(clean_data)
