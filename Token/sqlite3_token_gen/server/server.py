from flask import Flask,request,jsonify
from auth import authUser ,tokenCheck
from datetime import datetime

app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    req = request.get_json()
    if "username" in req and "password" in req:
        res,msg = authUser(req["username"],req["password"])
        if res:
            return jsonify(msg),200
        return jsonify(msg),404
    return jsonify({"msg":"Invalid Request"}),400

@app.route('/details',methods=['POST'])
def detail():
    req = request.get_json()
    token = req["token"]
    time = datetime.now()
    res,msg = tokenCheck(token,time,False)
    if res:
        return jsonify(msg),200
    return jsonify(msg),400

@app.route('/summary',methods=['POST'])
def summary():
    req = request.get_json()
    token = req["token"]
    time = datetime.now()
    res,msg = tokenCheck(token,time,True)
    if res:
        return jsonify(msg),200
    return jsonify(msg),400

if __name__=='__main__':
    app.run(debug=True,port=5050)
