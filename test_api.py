import unittest
import os
import json
from app import create_app

class FastFoodTestCase(unittest.TestCase):
    """This class tests the endpoints"""
    
    def setUp(self):
        """initialise app and test variables"""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.EntryData = json.dumps({
                                    "name": "burger"
                                    })

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
        self.assertEqual(res.status_code, 201)

    def test_edit_orders(self):
        """check that an order is editted succeffully"""
        res = self.client().put("/api/v1/orders/1", data = self.EntryData, content_type = "application/json")
        self.assertEqual(res.status_code, 200)

if __name__ == "__main__":
    unittest.main()