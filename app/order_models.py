class Orders():
    def __init__(self):
        self.orders = []
        self.foods = []

    def find_order(self, key, value):
        for order in self.orders:
            if order[key] == value:
                return True, order
        return False, 0

    def find_foods(self, key, value):
        for food in self.foods:
            if food[key] == value:
                return True, food
        return False, 0
            
    def all_orders(self):
        return self.orders

    def specific_order(self, orderId):
        self.orderId = int(orderId)
        if not self.orderId:
            return "message", "order id cannot be blank or 0"
        data=find_order("id", self.orderId)
        return jsonify(data[1])

    def add_order(self):
        data = request.get_json()
        if not data:
            return "message", "post cant be empty"
        food = find_foods("name", data["name"])[0]
        food_exists = find_foods("name", data["name"])[0]
        order_exists = find_order("name", data["name"])[0]
        order = find_order("name", data["name"])[1]
        if food_exists:
            if order_exists:
                order["units"] += 1
                return "message","order added successfully"
            else:
                self.orders.append(food)
                return "message","order added successfully"

    def del_order(self, orderId):
        self.orderId = int(orderId)
        if not self.orderId:
            return "message", "order id cannot be empty or a 0"
        order_exists=find_order("id", self.orderId)[0]
        order = find_order("id", self.orderId)[1]
        if order_exists:
            self.orders.remove(order)
            return "message", "order deleted successfully"
        else:
            return "message", "order id not found"
    
    

                

                

        


    
