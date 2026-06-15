raw_ids=[101,101,104,106,104,101,103,106]
unique_ids=[]
for i in raw_ids:
    if i not in unique_ids:
        unique_ids.append(i)


print(f"Original List: {raw_ids}")
print(f"Cleaned List:  {unique_ids}")
