import sqlite3

connection = sqlite3.connect('data.db')             #this will be create new file name data.db (sql lite)
cursor = connection.cursor()

# CREATE TABLE
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (name text, price real)"
cursor.execute(create_table)

cursor.execute("INSERT INTO items VALUES ('chair', 10.99)")

connection.commit()
connection.close()

