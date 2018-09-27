import unittest
import os
import json
from app import create_app, find_order, find_foods

class FastFoodTestCase(unittest.TestCase):
    """This class tests the endpoints"""
    
    def setUp(self):
        """initialise app and test variables"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.EntryData = json.dumps({
                                    "id":1,
                                    "name": "burger",
                                    "price": 80
                                    })
        self.statusData = json.dumps({
                                    "status": "accepted"
                                    })
    def test_find_order(self):
        self.assertEqual(find_order("id", 1), (False, 0))

    def test_find_foods(self):
        self.assertEqual(find_foods("id", 1), (False, 0))

    def test_post_foods(self):
        """test whether a food is posted successfully or not"""
        res = self.client().post("/api/v1/foods", data=self.EntryData, content_type = "application/json")
        self.assertEqual(res.status_code, 200)

    def test_get_orders(self):
        """check if all orders are returned"""
        res = self.client().get("/api/v1/orders")
        self.assertEqual(res.status_code, 200)

    def test_get_order(self):
        """test if a specific order is returned"""
        res = self.client().get("/api/v1/orders/1")
        self.assertEqual(res.status_code, 200)

    def test_post_orders(self):
        """test if an order is posted successfully"""
        res = self.client().post("/api/v1/orders", data=self.EntryData, content_type = "application/json")
        self.assertEqual(res.status_code, 200)

    def test_edit_orders(self):
        """check that an order is editted succeffully"""
        res = self.client().put("/api/v1/orders/1", data = self.EntryData, content_type = "application/json")
        self.assertEqual(res.status_code, 400)
        res = self.client().put("/api/v1/orders/1", data=self.statusData, content_type="application/json")
        self.assertEqual(res.status_code, 404)
    
    def test_delete_order(self):
        res = self.client().delete("/api/v1/orders/1", data = self.EntryData, content_type = "application/json")
        self.assertEqual(res.status_code, 404)

    def test_get_food(self):
        res = self.client().get("/api/v1/orders")
        self.assertEqual(res.status_code, 200)

    def test_get_one_food(self):
        res = self.client().get("/api/v1/orders/1")
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()