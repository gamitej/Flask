from flask import Flask,request,jsonify
from flask_jwt import JWT,jwt_required 

app = Flask(__name__)
app.secret_key = 'ami'

@app.route('/')
def home():
    return "Welcome To Home Page"


if __name__=="__main__":
    app.run(port=5050,debug=True)