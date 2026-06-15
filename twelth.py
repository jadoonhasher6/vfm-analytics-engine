csv_data='id,name,salary\n1,HAshir,5000\n2,Zainab,6000\n3,essa,4500'
lines=csv_data.split('\n')
data_rows=lines[1:]
print('employee names:')
for row in data_rows:
    columns=row.split(',')
    name=columns[1]
    print(f'-{name}')
