from flask import render_template

def setup_routes(app):
    @app.route("/")
    def home():
        return render_template("home.html")

    @app.route("/api/data")
    def get_data():
        return app.send_static_file("data.json")
