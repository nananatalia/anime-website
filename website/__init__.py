from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


# initialize our database
db = SQLAlchemy()
DataBase_Name = "database.db"

# setting up flask application
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "broombroom" # never share this in production
    # location of our database file
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DataBase_Name}"
    # initialize database with our app
    db.init_app(app)


    from .views import views
    from .authentication import authentication

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(authentication, url_prefix="/")

    from .models import User

    create_database(app)


    return app

def create_database(app):
    if not path.exists("website/" + DataBase_Name):
        with app.app_context():
            db.create_all()
        print("Created database!")