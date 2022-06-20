from flask import Flask,request,jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome To Home Page"


if __name__=="__main__":
    app.run(port=5050,debug=True)