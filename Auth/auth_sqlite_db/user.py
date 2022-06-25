import sqlite3
from tkinter.messagebox import NO


class User:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password
    
    def findByUserName(self,username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result =  cursor.execute(query,(username,))

        row = result.fetchone()
        if row:
            user = User(*row)
        else:
            user = None

        connection.close()

        return user