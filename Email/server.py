from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '***'
app.config['MAIL_PASSWORD'] = '***'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/")
def index():
   msg = Message(subject='Hello Sam Rocky', sender = 'xyz@gmail', recipients = ['abc@gmail.com'])
   msg.body = "Mail nhi ja raha hai"
   mail.send(msg)
   return "Sent"

if __name__ == '__main__':
   app.run(debug = True)