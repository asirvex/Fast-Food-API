"""Entry point to the aplication"""
import os

from app import create_app

name = os.getenv('APP_SETTINGS')
app = create_app(name)

if __name__ == "__main__":
    app.run()