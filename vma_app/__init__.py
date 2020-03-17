import os
from flask import Flask  # Import the Flask class
from .db import DB, MIGRATE
import configparser

def create_app():
    config = configparser.ConfigParser()
    configfilename = os.environ.get("VMACONFIG")
    config.read(configfilename)
    app = Flask(__name__)  # Create an instance of the class for our use
    app_settings = os.getenv("APP_SETTINGS", "config.DevelopmentConfig")
    app.config.from_object(app_settings)
    DB.init_app(app)
    app.db = DB
    if config['parent']['servicename'] == 'parent':
        MIGRATE.init_app(app, DB)
    else:
        try:
            init_db(app)
        except Exception:
            raise RuntimeError("Could not initialize database schema")
    return app
