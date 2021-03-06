import functools
import jwt
import datetime
from flask import Flask,request,jsonify
from functools import wraps
from db import userCheck

app = Flask(__name__)
app.secret_key = 'amitej'

def token_req(f):
    @wraps(f)
    def decorated(*args,**kwargs):
        token = request.args.get('token') # /route?token = asda788dasds
        if not token:
            return jsonify({"msg":"Token Missing!!"}),403
        try:
            data = jwt.decode(token,app.secret_key)
        except:
            return jsonify({"msg":"Token Invalid!!"}),403

        return f(*args,**kwargs)
    return decorated

@app.route('/login',methods=["POST"])
def login():
    req = request.get_json()
    if 'username' not in req or 'password' not in req:
        return jsonify({"msg":"Invalid Request"}),400
    user,passwd = req['username'],req['password']
    res,msg = userCheck(user,passwd)
    if res:
        token = jwt.encode({'user':user,'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=15)},app.secret_key)
        return jsonify({"token":token.decode('UTF-8')}),200
    return jsonify(msg),401

@app.route('/')
def home():
    return "Welcome To Home Page"

@app.route('/details')
@token_req
def details():
    return "Welcome To Details Page"





if __name__=="__main__":
    app.run(port=5050,debug=True)