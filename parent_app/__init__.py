import os
from flask import Flask  # Import the Flask class

def create_app():
    app = Flask(__name__)    # Create an instance of the class for our use
    print(__name__)
    app_settings = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
    return app
