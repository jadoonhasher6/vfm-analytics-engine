data=[{'id': 1, 'name': 'hashir'},{'id':2}]
for record in data:
    name=record.get('name','name not found')
    print(f"User ID {record['id']}: {name}")