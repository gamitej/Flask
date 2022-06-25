from curses import curs_set
import sqlite3
from venv import create

from numpy import insert
from soupsieve import select

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int,username text, password text)"
cursor.execute(create_table)

#---------- INSERT SINGLE ROW ---------------

user = (1,'amitej','1234')

insert_query = "INSERT INTO users VALUES(?,?,?)"
cursor.execute(insert_query,user)

#---------- INSERT MANY ROWS ---------------

users = [ (2,'rooney','2211'),(3,'singh','4321')]

cursor.executemany(insert_query,users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()