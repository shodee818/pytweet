from flask import Flask
from .database import init_db
from .config import Config
import os
from .models import models

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.secret_key = os.urandom(24)
    init_db(app)
    return app

app = create_app()