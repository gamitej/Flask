import uuid
import sqlite3 
from datetime import date, datetime,timedelta

def connect_to_db():
    connection = sqlite3.connect('data.db')
    return connection

def fetchOneRow(rows,table_name,find_by_row,value):
    cursor = connect_to_db()
    query = f"select {rows} from {table_name} where {find_by_row}=?"
    result =  cursor.execute(query,(value,))
    row = result.fetchone()
    return row

def authUser(username,password):
    connection = connect_to_db()
    cursor = connection.cursor()
    rows,table_name,find_by_row,value = "user_id,password","users","username",username
    row = fetchOneRow(rows,table_name,find_by_row,value)
    if row:
        user_id,passwd = row[0],row[1]
        if passwd == password:
            token = uuid.uuid1().hex
            time = datetime.now()
            user = (user_id,token,time)
            rows = "user_id,password"
            #row = fetchOneRow("users_token",token,rows,"username")
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
    # ----- To convert into datetime format -------
    expire_time = datetime.strptime(row[0],'%Y-%m-%d %H:%M:%S.%f') 
    timeDiff = time - expire_time
    if timeDiff.seconds <= 120:
        # for requested route we will increase the expire time by 3 min
        if reqRoute:
            # ---------- UPDATE THE TOKEN EXPIRE TIME ------------
            update_query = "UPDATE users_token SET expire_time = ? where token = ?"
            new_expire_time = expire_time + timedelta(minutes=3)
            update = (new_expire_time,token)
            cursor.execute(update_query,update)
            connection.commit()
            connection.close()
            # ---------- UPDATE THE TOKEN EXPIRE TIME ------------
        return True,{"msg":"Success"} 
    return False,{"msg":"Token Expired Please Login Again"} 

