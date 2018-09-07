"""Entry point to the aplication"""
import os

from app import create_App

name = os.getenv('APP_SETTINGS')
app = create_App(name)

if __name__ == "__main__":
    app.run()