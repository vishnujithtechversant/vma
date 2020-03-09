from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import current_app
from sqlalchemy import MetaData

DB = SQLAlchemy()
MIGRATE = Migrate()


def get_schema():
    meta = MetaData()
    meta.reflect(bind=current_app.db.engine)
    return meta
