import sqlite3

conn = sqlite3.connect('register.db')
print("Opened database successfully")

conn.execute('CREATE TABLE students (username TEXT, email TEXT, password TEXT)')
print("Table created successfully")
conn.close()
Footer
© 2022 GitHub, Inc.