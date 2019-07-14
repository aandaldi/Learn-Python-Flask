import sqlite3

connection = sqlite3.connect('data.db')             #this will be create new file name data.db (sql lite)
cursor = connection.cursor()

# CREATE TABLE
create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

# INSERT USER
user = (1, 'Aan', 'asdf')
insert_query = "INSERT INTO users VALUES(?,?,?)"
cursor.execute(insert_query,user)

users = [
    (2, 'iin', 'asdf'),
    (3, 'uun', 'asdf')
]

cursor.executemany(insert_query,users)

# SHOW THE DATA
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)


connection.commit()
connection.close()
