from flask import Flask, jsonify, request, Response
from instance.config import app_config


orders = [{
    "id": 1,
    "food": "burger",
    "price": 80
}, {
    "id": 2,
    "food": "smokey",
    "price": 35
}
]

def create_App(config_name):
    """app configuration"""
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("../instance/config.py")

    @app.route("/orders")
    def get_orders():
        return jsonify(orders)



    return app

