import sqlite3

class User:
    def __init__(self,_id,username,password):
        self.id = _id
        self.username = username
        self.password = password
    
    @classmethod
    def findByUserName(cls,username):
        try:
            connection = sqlite3.connect('data.db')
            cursor = connection.cursor()

            query = "SELECT * FROM users WHERE username=?"
            result =  cursor.execute(query,(username,))

            row = result.fetchone()
            if row:
                user = row
            else:
                user = None
            connection.close()
            return user

        except Exception as e:
            print("*** DB ERROR ***")
            print(e)
        
        