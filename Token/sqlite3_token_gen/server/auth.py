import uuid
from datetime import datetime, timedelta
from db import selectFromTable,insertIntoTable,updateTable

def stringToDateTime(value):
    new_value = datetime.strptime(value, '%Y-%m-%d %H:%M:%S.%f')
    return new_value

def authUser(username, password):
    rows, table_name, find_by_row, value = "user_id,password", "users", "username", username
    row = selectFromTable(rows, table_name, find_by_row, value)
    if row:
        user_id, passwd = row[0], row[1]
        if passwd == password:
            token = uuid.uuid1().hex
            time = datetime.now()
            rows, table_name, find_by_row, value = "*", "users_token", "user_id", user_id
            row = selectFromTable(rows, table_name, find_by_row, value)
            # -------- INSERT INTO TABLE WHEN TOKEN IS NOT PRESENT -------
            if not row:
                user = (user_id, token, time,2)
                table_name, total_values, values = "users_token", "(?,?,?,?)", user
                insertIntoTable(table_name, total_values, values)
                return True, {"token": token}
            # -------- UPDATE THE TOKEN IF TOKEN IS ALREADY PRESENT -------
            new_value = (time, token,2,user_id)
            table_name, rows_to_update, where_cond, values = "users_token", "expire_time = ?,token = ?,time_limit = ?", "user_id = ?", new_value
            updateTable(table_name, rows_to_update, where_cond, values)
            return True, {"token": token}
        return False, {"msg": "Incorrect Password"}
    return False, {"msg": "Username not found"}

def tokenCheck(token, time, reqRoute):
    rows, table_name, find_by_row, value = "expire_time,time_limit", "users_token", "token", token
    row = selectFromTable(rows, table_name, find_by_row, value)
    if not row:
        return False, {"msg": "Token Not Found"}
    str_expire_time,time_limit = row[0],row[1]
    expire_time = stringToDateTime(str_expire_time)
    timeDiff = time - expire_time
    if timeDiff.seconds <= time_limit*60:
        # for requested route we will increase the expire time by 3 min
        if reqRoute:
            # ---------- UPDATE THE TOKEN EXPIRE TIME ------------
            new_expire_time = expire_time + timedelta(minutes=3)
            new_values = (time_limit+3, token)
            table_name, rows_to_update, where_cond, values = "users_token", "time_limit = ?", "token = ?", new_values
            updateTable(table_name, rows_to_update, where_cond, values)
        return True, {"msg": "Success"}
    return False, {"msg": "Token Expired Please Login Again"}
