import mysql.connector

def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="44974",
        database="vfm_analytics"
    )
    print("Connected to MySQL successfully!")
    return connection

def insert_vfm_data(connection, data):
    cursor =connection.cursor()
    cursor.execute("DELETE FROM vfm_results")
    insert_query = "INSERT INTO vfm_results (product_name, daraz_price, daraz_rating, olx_price, olx_rating, vfm_winner) VALUES (%s,%s, %s,%s,%s,%s)"
    cursor.executemany(insert_query, data)
    connection.commit()
    print(f"{cursor.rowcount} rows inserted successfully!")

vfm_data =[
    ("running shoes", 100, 4.5, 80, 4.0, "Daraz"),
    ("gucci handbag", 150, 4.2, 120, 3.8, "OLX"),
    ('women sandals', 50, 4.0, 60, 4.5, "OLX"),
    ('gym track suit', 80, 4.3, 70, 4.1, "Daraz")

]
connection =connect_to_db()
insert_vfm_data(connection, vfm_data)

def fetch_vfm_data(connection):
    cursor=connection.cursor()
    cursor.execute("SELECT * FROM vfm_results")
    return cursor.fetchall()
results = fetch_vfm_data(connection)
print("\n--- VFM Results from MySQL ---")
for row in results:
    print(row)
