from flask import Blueprint
from flask import Flask,jsonify
from db import prodAvail,prodById,allProd

prod = Blueprint('prod', __name__)

@prod.route('/')
def prodList():
    res = allProd()
    return jsonify(res),200

@prod.route('/<int:id>')
def prodId(id):
    res = prodById(id)
    return jsonify(res)

@prod.route('/<string:name>')
def prodName(name):
    res = prodAvail(name)
    return jsonify(res)

