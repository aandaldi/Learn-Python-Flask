import sqlite3

connection = sqlite3.connect('data.db')             #this will be create new file name data.db (sql lite)
cursor = connection.cursor()

# CREATE TABLE
create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY AUTOINCREMENT, name text, price real)"
cursor.execute(create_table)

cursor.execute("INSERT INTO items(id,name, price) VALUES ('chair', 10.99)")

connection.commit()
connection.close()

