from flask import Flask

from auth.auth import auth
from prod.prod import prod

app = Flask(__name__)
app.register_blueprint(auth, url_prefix='/user')
app.register_blueprint(prod, url_prefix='/prod')

app.run(debug=True)