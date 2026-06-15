raw_data = [10, "20", 30, "Hello", 50]
cleaned_data=[]
for item in raw_data:
    try:
        num=int(item)
        cleaned_data.append(num)
    except ValueError:
        print(f"'{item}' is not a number and will be skipped.")
print('cleaned_data',cleaned_data)
