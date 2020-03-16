import os
from flask import Flask  # Import the Flask class
from .db import DB, MIGRATE
import configparser
from child_app.db import DB, init_db

def create_app():
    config = configparser.ConfigParser()
    configfilename = "appconfig.ini"
    config.read(configfilename)
    app = Flask(__name__)
    if config['appconfig']['servicename'] == 'parent':
        import pdb;pdb.set_trace()
        app_settings = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
        app.config.from_object(app_settings)
        DB.init_app(app)
        app.db = DB
        MIGRATE.init_app(app, DB)
        return app
    else:
        app_settings = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
        app.config.from_object(app_settings)
        base_url = app.config.get("PARENT_BASE_URL")
        if not base_url:
            raise RuntimeError("Error: You did not provide the PARENT_BASEURL environment variable.")

        DB.init_app(app)
        app.db = DB
        try:
            init_db(app)
        except Exception:
            raise RuntimeError("Could not initialize database schema")

        return app


