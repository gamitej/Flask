# only amisha & manvi are important employee

db_user = {"amitej": {"password": "gadha", "_id": 1}, "amisha": {
    "password": "1234", "_id": 2}, "amrita": {"password": "gadha", "_id": 3}, "manvi": {"passwd": "4321", "_id": 4}}

def userCheck(user,passwd):
    if user in db_user:
        if db_user[user]["password"] == passwd:
            return True,{"msg":"Login Successfull"}
        return False,{"msg":"Password Incorrect"}
    return False,{"msg":"User not found"}
