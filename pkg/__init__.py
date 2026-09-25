import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from config import DevelopmentConfig


def create_app():
    from pkg.models import db

    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

  

    db.init_app(app)

    migrate = Migrate(app, db)
    
    app.secret_key = os.getenv("SECRET_KEY")

    return app

app = create_app()

from pkg import routes

load_dotenv()