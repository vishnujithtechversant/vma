from flask import jsonify, render_template
from serializer import serialize
from .db import get_schema

from .models import User  # trigger migration


def setup_routes(app):
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/api/get-schema")
    def shema_view():
        schema = get_schema()
        return jsonify({
            "schema": serialize(schema)
        })
