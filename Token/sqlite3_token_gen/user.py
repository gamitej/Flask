import uuid
import sqlite3 
from datetime import date, datetime,timedelta

def connect_to_db():
    connection = sqlite3.connect('data.db')
    return connection
    
def authUser(username,password):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = "select user_id,password from users where username=?"
    result =  cursor.execute(query,(username,))
    row = result.fetchone()
    if row:
        user_id,passwd = row[0],row[1]
        if passwd == password:
            token = uuid.uuid1().hex
            time = datetime.now()
            user = (user_id,token,time)
            insert_query = "INSERT OR IGNORE INTO users_token VALUES(?,?,?)"
            cursor.execute(insert_query,user)
            connection.commit()
            connection.close()
            return True,{"token":token} 
        return False,{"msg":"Incorrect Password"} 
    return False,{"msg":"Username not found"}


def tokenCheck(token,time,reqRoute):
    connection = connect_to_db()
    cursor = connection.cursor()
    query = "select expire_time from users_token where token=?"
    result =  cursor.execute(query,(token,))
    row = result.fetchone()
    if not row:
        return False,{"msg":"Token Not Found"}
    # ----- To convert into datetime format
    expire_time = datetime.strptime(row[0],'%Y-%m-%d %H:%M:%S.%f') 
    timeDiff = datetime.now() - expire_time
    if timeDiff.seconds <= 120:
        # for requested route we will increase the expire time by 3 min
        if reqRoute:
            new_expire_time = expire_time + timedelta(minutes=3)
        return True,{"msg":"Success"} 
    return False,{"msg":"Token Expired Please Login Again"} 

