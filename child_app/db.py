from multiprocessing import Lock
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

from .utils import get_metadata_from_parent

DB = SQLAlchemy()
lock = Lock()


# connect to parent service and initialize database
def init_db(app):
    base_url = app.config["PARENT_BASE_URL"]

    with lock:
        metadata = get_metadata_from_parent(base_url)
        engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
        metadata.create_all(engine, checkfirst=True)
