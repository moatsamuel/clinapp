import os
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from config import DevelopmentConfig
from pkg.models import db

load_dotenv()

def create_app():

    app = Flask(__name__)

    app.config.from_object(DevelopmentConfig)

    from pkg.admin.routes import admin
    from pkg.users.routes import users
    # from pkg.doctors.routes import doctors

    app.register_blueprint(users)
    app.register_blueprint(admin,url_prefix='/admins')
    # app.register_blueprint(doctors,url_prefix='/doctors')
    
  

    db.init_app(app)

    migrate = Migrate(app, db)
    
    app.secret_key = os.getenv("SECRET_KEY")

    return app

app = create_app()



