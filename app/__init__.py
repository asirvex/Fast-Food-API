from flask import Flask, jsonify, request
from instance.config import app_config
from werkzeug.security import generate_password_hash, check_password_hash

foods =  [{
    "id": 1,
    "name": "burger",
    "quantity": "1 piece",
    "price": 80,
    "units": 1
}, {
    "id": 2,
    "name": "smokey",
    "quantity": "1 piece",
    "price": 35,
    "units": 1
}, {
    "id": 3,
    "name": "chicken sandwich",
    "quantity": "1 piece",
    "price": 100,
    "units": 1
}, {
    "id": 4,
    "name": "soda",
    "quantity": "500ml",
    "price": 80,
    "units": 1
}
]

orders = [{
    "id": 2,
    "name": "chicken sandwich",
    "quantity": "1 piece",
    "price": 100,
    "units": 1
}, {
    "id": 1,
    "name": "burger",
    "quantity": "1 piece",
    "price": 80,
    "units": 1
}
]

users = {}

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
    
def add_user(email, username, password):
    user={}
    user["email"] = email
    user["password"] = generate_password_hash(password, method="sha256")
    users["username"] = user

def create_app(config_name):
    """app configuration"""
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("../instance/config.py")

    @app.route("/api/v1/orders")
    def get_orders():
        response = jsonify(orders)
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

    return app
