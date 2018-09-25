#Fast-Food-Fast
Fast-Food-Fast is an online food delivery service

[![Build Status](https://travis-ci.org/asirvex/Fast-Food-API.svg?branch=master)](https://travis-ci.org/asirvex/Fast-Food-API)

[![Coverage Status](https://coveralls.io/repos/github/asirvex/Fast-Food-API/badge.svg)](https://coveralls.io/github/asirvex/Fast-Food-API)

[![Maintainability](https://api.codeclimate.com/v1/badges/8c5bc842bc44fc7b1e26/maintainability)](https://codeclimate.com/github/asirvex/Fast-Food-API/maintainability)

To run this project:

- Create a virtual environment   
`$ virtualenv -p python3 env`

- Activate the virtual environment   
`$ source env/Scripts/activate`


- Clone this repo   
`$ git clone "https://github.com/asirvex/Fast-Food-API.git"`

- Install requirements   
`$ pip install -r requirements.txt`

- To run:
	- for tests run
	`$ python test_api.py`

	- for the app run
	`$ export APP_SETTINGS="development"`
	`$ python run.py`

You can test the endpoints using postman:

| endpoint | method | description |
| --- | --- | --- |
| /api/v1/orders | GET | view all orders |
| /api/v1/orders | POST | add an order |
| /api/v1/orders/orderId | GET | view a specific order |
| /api/v1/orders/orderId | PUT | edit a specific order |
| /api/v1/orders/orderId | DELETE | delete a specific order |

| endpoint | method | description |
| --- | --- | --- |
| /api/v1/foods | GET | view all foods |
| /api/v1/foods | POST | add a food |
| /api/v1/foods/foodId | GET | view a specific food |
| /api/v1/foods/foodId | PUT | edit a specific food |