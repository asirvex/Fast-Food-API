from flask import Flask, jsonify, request
from instance.config import app_config

foods =  [{
    "id": 1,
    "name": "burger",
    "price": 80
}, {
    "id": 2,
    "name": "smokey",
    "price": 35
}, {
    "id": 3,
    "name": "chicken sandwich",
    "price": 150
}
]

orders = [{
    "id": 1,
    "name": "burger",
    "price": 80
}
]

def find_order(key, name):
    for order in orders:
        if order[key] == name:
            return True, order
    return False, "filler"

def find_foods(key, name):
    for food in foods:
        if food[key] == name:
            return True, food
    return False, "filler"
    

def create_App(config_name):
    """app configuration"""
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("../instance/config.py")

    @app.route("/orders")
    def get_orders():
        return jsonify(orders)

    @app.route("/orders/<orderId>")
    def get_order(orderId):
        orderId = int(orderId)
        for order in orders:
            if order["id"] == orderId:
                return jsonify(order)

    @app.route("/orders", methods=["POST"])
    def post_orders():
        order_input = request.json["name"]
        for food in foods:
            if order_input == food["name"]:
                orders.append(food)
                return jsonify(orders)
        return "food not found"

    @app.route("/orders/<orderId>", methods=["PUT"])
    def edit_orders(orderId):
        orderId = int(orderId)
        order_input = request.json["name"]
        bool1 = find_order("id", orderId)[0]
        order = find_order("id", orderId)[1]
        bool2 = find_foods("name", order_input)[0]
        food = find_foods("name", order_input)[1]
        if bool1:
            if bool2:
                orders[orders.index(order)] = food
                return jsonify(orders)
            else:
                return "food not found"
        else:
            return "orderId not available"





    return app
