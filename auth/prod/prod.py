from flask import Blueprint
from flask import jsonify
from db import prodAvailList,prodById,allProd

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
    res = prodAvailList(name)
    if res:
        return jsonify({"msg":"Product Avail"}),200
    return jsonify({"msg":"Product not found"}),404

