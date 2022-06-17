from flask import Flask,jsonify

userDb = {"Amitej":'1234',"singh":'4321'}

def getUser(userName,passwd):
    if userName in userDb:
        if userDb[userName]==passwd:
            return jsonify({"msg":'Login Successfull'}),200
        return jsonify({"msg":'Password Incorrect'}),401
    return jsonify({"msg":'Username Incorrect'}),401