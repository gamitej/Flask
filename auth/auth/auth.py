from flask import Flask,request,jsonify
from flask import Blueprint
from db import getUser

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['POST'])
def login():
    try:
        req = request.get_json()
        user,passwd = req['user'],req['passwd'] 
        res = getUser(user,passwd)
        return res
    except Exception as e:
        return jsonify({"msg":'Error Occured'}),500
