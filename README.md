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

	- get "/api/v1/orders" - get all orders

	- get "/api/v1/orders/<orderId>" - get a specific order

	- post "/api/v1/orders" - post an order
	use json format and specify only the order name 
		e.g {"name":"burger"}

	- put "/api/v1/orders/<orderId>" - edit an order where <orderId> is an integer
	use json format and specify only the order name 
		e.g {"name":"burger"}