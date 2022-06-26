import sqlite3
from datetime import datetime,timedelta

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = '''
        CREATE TABLE IF NOT EXISTS users (
            user_id text,
            username VARCHAR(25) NOT NULL,
            password VARCHAR(25) NOT NULL,
            PRIMARY KEY (user_id)
        )
        ''' 
cursor.execute(create_table)

create_table = '''
        CREATE TABLE IF NOT EXISTS users_token (
            user_id text,
            token VARCHAR(25) NOT NULL,
            expire_time date NOT NULL,
            PRIMARY KEY (user_id),
            CONSTRAINT fk_user_id FOREIGN KEY (user_id) REFERENCES users (user_id)
        )
        ''' 
cursor.execute(create_table)

#---------- INSERT MANY ROWS --------------

users = [ (1,'amitej','1234'),(2,'rooney','2211'),(3,'singh','4321')]

insert_query = "INSERT OR IGNORE INTO users VALUES(?,?,?)"

cursor.executemany(insert_query,users)

connection.commit()
connection.close()