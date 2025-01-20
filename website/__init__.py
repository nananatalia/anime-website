from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# initialize our database
db = SQLAlchemy()
DataBase_Name = "database.db"

# setting up flask application
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "broombroom" # never share this in production
    # location of our database
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DataBase_Name}"
    # initialize database with our app
    db.init_app(app)


    from .views import views
    from .authentication import authentication

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(authentication, url_prefix="/")


    return app

