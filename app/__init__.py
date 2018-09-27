from flask import Flask, jsonify, request
from instance.config import app_config

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
        order_input = request.get_json()
        order_input = order_input["name"]
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
                    nfood={}
                    nfood["id"]=food["id"]
                    nfood["name"]=food["name"]
                    nfood["price"]=food["price"]
                    nfood["units"]=1
                    orders.append(nfood)
                    response = jsonify({"message": "updated successfully","ordered items": orders})
                    response.status_code = 200
                    return response
        return jsonify({"message":"food not found"}), 404 

    @app.route("/api/v1/orders/<orderId>", methods=["PUT"])
    def edit_orders(orderId):
        orderId = int(orderId)
        order_exists = find_order("id", orderId)[0]
        order = find_order("id", orderId)[1]
        order_status=request.get_json()
        if "status" not in order_status:
            return jsonify({"message": "your input must contain a 'status' field"}), 400
        order_status=order_status["status"].strip()
        if not order_exists:
            return jsonify({"message":"orderId does not exist"}), 404     
        if order_status == "accepted" or order_status == "declined" or order_status == "completed":     
            if order_exists:
                order["status"] = order_status
                return jsonify({"message": "order status changed successfully"}), 200
        return jsonify({"message": "order status must be accepted, declined or completed"}, order_status), 400

    @app.route("/api/v1/orders/<orderId>", methods=["DELETE"])
    def delete_order(orderId):
        orderId = int(orderId)
        found_order = find_order("id", orderId)
        if found_order[0]:
            orders.remove(found_order[1])
            return jsonify("message", "item removed successfully"), 200
        else:
            return jsonify("message", "Order id was not found"), 404

    @app.route("/api/v1/foods")
    def get_food():
        if not foods:
            return jsonify("message", "no foods in the foods list"), 404
        return jsonify(foods), 200

    @app.route("/api/v1/foods", methods=["POST"])
    def post_food():
        data = request.get_json()
        if not data:
            return jsonify("message", "data to be posted cannot be blank")
        elif find_foods("id", data["id"])[0]:
                return jsonify("message", "food already exists")
        else:
            foods.append(data)
            return jsonify("message:", "food added successfully")

    @app.route("/api/v1/foods/<foodId>")
    def get_one_food(foodId):
        foodId = int(foodId)
        if not foodId:
            return jsonify("message", "food id cannot be zero or empty")
        food_exists=find_foods("id", foodId)[0]
        food=find_foods("id", foodId)[1]
        if not food_exists:
            return jsonify("message", "food not found")
        if food_exists:
            return jsonify(food)
        return jsonify()

    @app.route("/api/v1/foods/<foodId>", methods=["PUT"])
    def put_food(foodId):
        data=request.get_json()
        if not data["id"] or not data["name"] or not data["price"]:
            return jsonify("message", "input should have 'id', 'name', 'price'")
        foodId=int(foodId)
        food_exists=find_foods("id", foodId)[0]
        food=find_foods("id", foodId)[1]
        if find_foods("id", data["id"])[0]:
            return jsonify("message", "another food with the same id exists")
        if food_exists:
            food["id"]=data["id"]
            food["name"]=data["name"]
            food["price"]=food["price"]
            return jsonify("message", "food updated successfully")
        if not food_exists:
            return jsonify("message", "food not found"), 404
        
    return app
