from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

BASE_PCS_URL = f'http://product_catalog_service:5000/products'
BASE_CS_URL = f'http://cart_service:5001/cart'

# ------------------------------------------------------ CART SERVICE
# Get cart items
@app.route('/cart', methods=['GET'])
def get_cart_items():
    url = f'{BASE_CS_URL}'
    req = requests.get(url)
    return jsonify(req.json()), req.status_code

# Add a product to cart
@app.route('/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    url = f'{BASE_CS_URL}'
    req = requests.post(url, json=data)
    return jsonify(req.json()), req.status_code

# Remove product from cart
@app.route('/cart/<int:id>', methods=['DELETE'])
def delete_item_from_cart(id):
    url = f'{BASE_CS_URL}/{id}'
    req = requests.post(url)
    return jsonify(req.json()), req.status_code

# Update product amount
@app.route('/cart/<int:id>', methods=['PATCH'])
def update_product_amount(id):
    data = request.json
    url = f'{BASE_CS_URL}/{id}'
    req = requests.patch(url, json=data)
    return jsonify(req.json()), req.status_code

# ------------------------------------------------------ PRODUCT CATALOG SERVICE
# Get All
@app.route('/products')
def get_products():
    url = f'{BASE_PCS_URL}'
    req = requests.get(url)
    return jsonify(req.json()), req.status_code

# Get one
@app.route('/products/<int:id>')
def get_product(id):
    url = f'{BASE_PCS_URL}/{id}'
    req = requests.get(url)
    return jsonify(req.json()), req.status_code

app.run(debug=True, host='0.0.0.0', port=5050)