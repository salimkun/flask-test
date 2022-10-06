from flask import Flask, jsonify, request
import os, datetime
from config import db
from config.services.product_svc import ProductService
from config.models.product_model import Product

app = Flask(__name__)
# create the database and table.
if not os.path.isfile('products.db'):
    db.connect()
    

@app.route("/product", methods=['POST'])
def postRequest():
    req_data = request.get_json()
    name = req_data['name']
    price = req_data['price']
    description = req_data['description']
    quantity = req_data['quantity']
    pd = Product(db.getNewId(), name, price, description, quantity, datetime.datetime.now())
    resp = ProductService.addProduct(pd)
    return resp


@app.route('/product', methods=['GET'])
def getRequest():
    args = request.args
    order_by = args.get('order_by')
    sort_by = args.get('sort_by')
    resp = ProductService.getProduct(order_by, sort_by)
    return resp

if __name__ == '__main__':
    app.run()