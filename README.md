This is an online food delivery service

[![Build Status](https://travis-ci.org/asirvex/Fast-Food-API.svg?branch=master)](https://travis-ci.org/asirvex/Fast-Food-API)

[![Coverage Status](https://coveralls.io/repos/github/asirvex/Fast-Food-API/badge.svg)](https://coveralls.io/github/asirvex/Fast-Food-API)

[![Maintainability](https://api.codeclimate.com/v1/badges/8c5bc842bc44fc7b1e26/maintainability)](https://codeclimate.com/github/asirvex/Fast-Food-API/maintainability)

To run this project:

1. Create a virtual environment   
$ virtualenv -p python3 env

1. Activate the virtual environment   
$ source env/Scripts/activate


1. Clone this repo   
$ git clone "https://github.com/asirvex/Fast-Food-API.git"

1. Install requirements   
$ pip install -r requirements.txt

1. To run:
	1. for tests run
	$ python test_api.py

	1. for the app run
	$ export APP_SETTINGS="development"
	$ python run.py

You can test the endpoints using postman:

	1. get "/api/v1/orders" - get all orders

	1. get "/api/v1/orders/<orderId>" - get a specific order

	1. post "/api/v1/orders" - post an order
	use json format and specify only the order name 
		e.g {"name":"burger"}

	1. put "/api/v1/orders/<orderId>" - edit an order where <orderId> is an integer
	use json format and specify only the order name 
		e.g {"name":"burger"}