from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from flask_pack.database import init_db

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    Migrate(app,db)
    return db
