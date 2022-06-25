from flask import Flask,request,jsonify 

app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    try:
        req = request.get_json()
        if 'user' not in req or 'passwd' not in req:
            return jsonify({"msg":'Bad Request'}),400
        user,passwd = req['user'],req['passwd'] 
        res = g
        return res
    except Exception as e:
        return jsonify({"msg":'Error Occured'}),500