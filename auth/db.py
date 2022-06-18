from flask import Flask, jsonify

userDb = {"Amitej": '1234', "singh": '4321'}


def getUser(userName, passwd):
    if userName in userDb:
        if userDb[userName] == passwd:
            return jsonify({"msg": 'Login Successfull'}), 200
        return jsonify({"msg": 'Password Incorrect'}), 401
    return jsonify({"msg": 'Username Incorrect'}), 401


def addUser(userName, passwd):
    if userName in userDb:
        return jsonify({"msg": "User already exist"}), 409
    userDb[userName] = passwd
    return jsonify({"msg": "SignUp SuccessFull"}), 200

# ********************** PRODUCT *******************************

prods = {2: {"name": "Chair", "Qua": 2}, 3: {"name": "Table", "Qua": 3},
         1: {"name": "Fan", "Qua": 1}, 4: {"name": "Bed", "Qua": 0}}

prodAvail = {"Chair", "Fan", "Table", "Fan"}

def allProd():
    lis = []
    for i in prods:
        lis.append(prods[i]['name'])
    return lis

def prodById(id):
    return prods[id]


def prodAvail(name):
    if name in prodAvail:
        return True 
    return False
