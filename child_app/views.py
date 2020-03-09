from flask import render_template


def setup_routes(app):
    @app.route("/")
    def home():
        return render_template("home.html")
