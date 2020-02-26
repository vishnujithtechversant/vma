# Entry point for the application.
from . import create_app
from .views import setup_routes

app = create_app()
setup_routes(app)
