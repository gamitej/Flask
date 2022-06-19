import uuid 
from datetime import datetime

userDb = {"amitej":'1234',"singh":'4321'}

userToken = {"amitej":{"status":False},"singh":{"status":False}}


def authUser(user,passwd):
    if user in userDb:
        if userDb[user] == passwd:
            token = uuid.uuid1().hex
            userToken[user] = {"status":True,"token":token,"time":datetime.now()}
            return True,{"token":token} 
        return False,{"msg":"Incorrect Password"} 
    return False,{"msg":"Username not found"}

def tokenCheck():
    return ''

