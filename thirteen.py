file_name='client_data.csv'
try:
    with open(file_name,'r') as file:
        data=file.read()
        print('data loaded successfully')
except FileNotFoundError:
    print('the file is npot found,skip ingestion')

print('pipeline status:ready for the next task.')