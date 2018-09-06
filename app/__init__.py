from flask import Flask, jsonify, request
from instance.config import app_config

foods =  [{
<<<<<<< HEAD
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
=======
>>>>>>> post_orders
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

orders = []

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
        order_input = request.json["name"],
<<<<<<< HEAD
        order_input = str(order_input)
        
=======
        for food in foods:
            if order_input[0] == food["name"]:
                orders.append(food)
                return jsonify(orders)
        return "food not found"
>>>>>>> post_orders

    return app
