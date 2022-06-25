from flask import Flask,request,jsonify 
from user import User

app = Flask(__name__)

@app.route('/login',methods=['POST'])
def login():
    try:
        req = request.get_json()
        if 'username' not in req or 'password' not in req:
            return jsonify({"msg":'Bad Request'}),400
        username,password = req['username'],req['password'] 
        res = User.findByUserName(username)
        if not res:
            return jsonify({"msg":"User Not Found!!"}),401
        if password == res[2]:
            return jsonify({"msg":"Login Successfull!!"}),200
        return jsonify({"msg":"Password Incorrect!!"}),401
    except Exception as e:
        print(e)
        return jsonify({"msg":'Error Occured'}),500

if __name__=='__main__':
    app.run(debug=True)