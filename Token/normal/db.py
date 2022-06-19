import uuid 
from datetime import datetime

userDb = {"amitej":'1234',"singh":'4321'}

userToken = {"amitej":{"status":False},"singh":{"status":False}}

tokenUser = {}

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

def tokenCheck(token,time):
    if token not in tokenUser:
        return False,{"msg":"Token Not Found"}
    user = tokenUser[token]
    if user in userToken and userToken[user]["status"] and userToken[user]["token"] == token:
        timeDiff = time - userToken[user]["time"]
        if timeDiff.seconds <= 120:
            return True,{"msg":"Success"} 
        return False,{"msg":"Token Expired"} 
    return False,{"msg":"Token Invalid"}

