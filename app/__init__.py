from flask import Flask, jsonify, request
from instance.config import app_config

def create_App(config_name):
    """app configuration"""
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile("../instance/config.py")

    return app
