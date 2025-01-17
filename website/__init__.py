from flask import Flask


# setting up flask application
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "broombroom" # never share this in production

    return app

