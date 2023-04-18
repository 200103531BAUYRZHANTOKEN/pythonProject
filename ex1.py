from selenium import webdriver
import sqlite3

conn = sqlite3.connect('database.sqlite2')

c = conn.cursor()

create_database_query = """CREATE TABLE user (
                        id INTEGER PRIMARY KEY, 
                        name TEXT NOT NULL, 
                        code TEXT NOT NULL);"""

insert_database_query = """INSERT INTO user 
                        (id, name, code)
                        VALUES(5,'test','12345');"""


read_table_query = """SELECT * FROM user;"""

c.execute(create_database_query)
c.execute(insert_database_query)
c.execute(read_table_query)

conn.commit()

data = c.fetchall()

usernames = []
passwords = []

for row in data:
    usernames.append(row[1])
    passwords.append(row[2])


print(usernames)
print(passwords)
