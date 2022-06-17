from flask import Blueprint

prod = Blueprint('prod', __name__)

@prod.route('/')
def index():
    return "prod"