import os

from flask import Flask  # Import the Flask class
from .db import DB, init_db

# def create_app():
#     app = Flask(__name__)    # Create an instance of the class for our use
#     app_settings = os.getenv('APP_SETTINGS', 'config.DevelopmentConfig')
#     app.config.from_object(app_settings)
#     base_url = app.config.get("PARENT_BASE_URL")
#     if not base_url:
#         raise RuntimeError("Error: You did not provide the PARENT_BASEURL environment variable.")
#
#     DB.init_app(app)
#     app.db = DB
#     try:
#         init_db(app)
#     except Exception:
#         raise RuntimeError("Could not initialize database schema")
#
#     return app
