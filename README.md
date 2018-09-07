This is an online food delivery service

[![Build Status](https://travis-ci.org/asirvex/Fast-Food-API.svg?branch=master)](https://travis-ci.org/asirvex/Fast-Food-API)

To run this project:
	1. Create a virtual environment   
	$ virtualenv -p python3 env
	
	2. Activate the virtual environment   
	$ source env/Scripts/activate
	
	
	4. Clone this repo   
	$ git clone "https://github.com/asirvex/Fast-Food-API.git"
	
	5. Install requirements   
	$ pip install -r requirements.txt
	
	6. To run:
		i. for tests run
		$ python test_api.py
		
		ii. for the app run
		$ export APP_SETTINGS="development"
		$ python run.py
		
You can test the endpoints using postman:
	1. get "/api/v1/orders" - get all orders
	
	2. get "/api/v1/orders/<orderId>" - get a specific order

	3. post "/api/v1/orders" - post an order
		use json format and specify only the order name 
			e.g {"name":"burger"}

	4. put "/api/v1/orders/<orderId>" - edit an order 
		use json format and specify only the order name 
			e.g {"name":"burger"}