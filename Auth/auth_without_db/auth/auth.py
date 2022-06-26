from flask import Flask,request,jsonify
from flask import Blueprint
from db import getUser,addUser

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['POST'])
def login():
    try:
        req = request.get_json()
        if 'user' not in req or 'passwd' not in req:
            return jsonify({"msg":'Bad Request'}),400
        user,passwd = req['user'],req['passwd'] 
        res = getUser(user,passwd)
        return res
    except Exception as e:
        return jsonify({"msg":'Error Occured'}),500

@auth.route('/signup',methods=['POST'])
def signup():
    try:
        req = request.get_json()
        if 'user' not in req or 'passwd' not in req:
            return jsonify({"msg":'Bad Request'}),400
        user,passwd = req['user'],req['passwd'] 
        res = addUser(user,passwd)
        return res
    except Exception as e:
        return jsonify({"msg":'Error Occured'}),500
        