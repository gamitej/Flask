from flask import Blueprint
from db import prodAvail,prodById,allProd

prod = Blueprint('prod', __name__)

@prod.route('/')
def prodList():
    res = 
    return allProd()

@prod.route('/<int:id>')
def prodId(id):
    return prodById(id)

@prod.route('/<string:name>')
def prodName(name):
    return prodAvail(name)

