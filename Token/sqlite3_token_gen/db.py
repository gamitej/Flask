import uuid
import sqlite3 
from datetime import datetime,timedelta

def connect_to_db():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    return cursor 
    
def authUser(user,passwd):
    if user in userDb:
        if userDb[user] == passwd:
            token = uuid.uuid1().hex
            userToken[user] = {"status":True,"token":token,"time":datetime.now()}
            tokenUser[token] = user
            print(tokenUser)
            return True,{"token":token} 
        return False,{"msg":"Incorrect Password"} 
    return False,{"msg":"Username not found"}

def tokenCheck(token,time,reqRoute):
    if token not in tokenUser:
        return False,{"msg":"Token Not Found"}
    user = tokenUser[token]
    if user in userToken and userToken[user]["status"] and userToken[user]["token"] == token:
        timeDiff = time - userToken[user]["time"]
        if timeDiff.seconds <= 120:
            # for requested route we will increase the expire time by 3 min
            if reqRoute:
                userToken[user]["time"] = userToken[user]["time"] + timedelta(minutes=3)
            return True,{"msg":"Success"} 
        return False,{"msg":"Token Expired Please Login Again"} 
    return False,{"msg":"Token Invalid"}
