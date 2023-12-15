import sqlite3

# establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# query all data based on a condition
cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# query certain columns based on a condition
cursor.execute("SELECT band, date FROM events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# insert new rows
# new_rows = [('Cat', 'Cat City', '2088.10.17'),
#             ('Hen', 'Hen City', '2088.10.17')]
# cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
# connection.commit()

# query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)
