schema={
    'user_id':'integer',
    'user_name':'string',
    'is_active':'boolean'
}
for column,stype in schema.items():
    print(f"Column: {column}, Type: {stype}")