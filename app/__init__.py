from flask import Flask, jsonify, request
from instance.config import app_config
from werkzeug.security import generate_password_hash, check_password_hash

foods =  []

orders = []

users = []

def find_order(key, value):
    for order in orders:
        if order[key] == value:
            return True, order
    return False, 0

def find_foods(key, value):
    for food in foods:
        if food[key] == value:
            return True, food
    return False, 0
    
"""def add_user(email, username, password):
    user={}
    user["email"] = email
    user["password"] = generate_password_hash(password, method="sha256")
    users["username"] = user"""

def create_app(config_name):
    """app configuration"""
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("../instance/config.py")

    @app.route("/api/v1/orders")
    def get_orders():
        if orders:
            response = jsonify(orders)
        else:
            response = jsonify("message", "no orders available")
        return response

    @app.route("/api/v1/orders/<orderId>")
    def get_order(orderId):
        orderId = int(orderId)
        for order in orders:
            if order["id"] == orderId:
                response = jsonify(order)
                return response
        return "orderId not found"

    @app.route("/api/v1/orders", methods=["POST"])
    def post_orders():
        order_input = request.json["name"]
        order_exists = find_order("name", order_input)[0]
        order = find_order("name", order_input)[1]
        for food in foods:
            if order_input == food["name"]:
                if order_exists:
                    order["units"] += 1
                    response = jsonify({"message": "updated successfully","ordered items": orders})
                    response.status_code = 201
                    return response
                else:
                    orders.append(food)
                    response = jsonify({"message": "updated successfully","ordered items": orders})
                    response.status_code = 201
                    return response
        return "food not found"

    @app.route("/api/v1/orders/<orderId>", methods=["PUT"])
    def edit_orders(orderId):
        orderId = int(orderId)
        order_input = request.json["name"]
        orderid_exists = find_order("id", orderId)[0]
        order_byid = find_order("id", orderId)[1]
        food_exists = find_foods("name", order_input)[0]
        food = find_foods("name", order_input)[1]
        order_exists = find_order("name", order_input)[0]
        order = find_order("name", order_input)[1]

        if orderid_exists:
            if food_exists:
                if order_exists:
                    order["units"] += 1
                    order_byid["units"] -= 1
                    if order_byid["units"] == 0:
                        orders.__delitem__(orders.index(order_byid))
                    response = jsonify({"message": "updated successfully","ordered items": orders})
                    response.status_code = 201
                    return response
                else:
                    orders[orders.index(order_byid)] = food
                    response = jsonify({"message": "updated successfully","ordered items": orders})
                    response.status_code = 201
                    return response
            else:
                return "food not found"
        else:
            return "orderId not available"

        
    @app.route("/api/v1/orders/<orderId>", methods=["DELETE"])
    def delete_order(orderId):
        orderId = int(orderId)
        found_order = find_order("id", orderId)
        if found_order[0]:
            orders.remove(found_order[1])
            return jsonify("message", "item removed successfully")
        else:
            return jsonify("message", "Order id was not found")

    @app.route("/api/v1/food")
    def get_food():
        return jsonify(foods)

    @app.route("/api/v1/food", methods=["POST"])
    def post_food():
        data = request.get_json()
        if not data:
            return jsonify("message", "data to be posted cannot be blank")
        foods.append(data)
        return jsonify("message:", "food added successfully")
        



    """@app.route("/api/v1/signup", methods=["POST"])
    def create_user():
        data = request.get_json()
        username = data["username"].strip()
        email = data["email"].strip()
        password = data["password"].strip()
        add_user(email, username, password)"""


    return app
