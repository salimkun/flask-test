from flask import jsonify
from .. import db

class ProductService:

    def addProduct(product):
        prd = product.serialize()
        bks = [b.serialize() for b in db.view()]
        name = prd['name']
        for b in bks:
            if b['name'] == name:
                return jsonify({
                    'res': f'Error ⛔❌! Product with name {name} is already in library!',
                    'status': '404'
                }), 404

        db.insert(product)
        return jsonify({
                    # 'error': '',
                    'res': prd,
                    'status': '291',
                    'msg': 'Success creating a new product'
                }), 201

    def getProduct(order_by="", sort_by=""):
        pds = [b.serialize() for b in db.view(order_by, sort_by)]
        return jsonify({
                    # 'error': '',
                    'res': pds,
                    'status': '200',
                    'msg': 'Success getting all product in library',
                    'no_of_products': len(pds)
                }), 200

