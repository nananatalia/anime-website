# storing roots for the website

from flask import Blueprint


# define that this file is a blueprint of application
# setting up a blueprint
authentication = Blueprint("authentication", __name__)

@authentication.route("/login")
def login():
    return "<h3>Login</h3>"

@authentication.route("/logout")
def logout():
    return "<p>Logout</p>"

@authentication.route("/sign-up")
def sign_up():
    return "<p>Sign up</p>"

@authentication.route("/profile")
def profile():
    return "<p>Profile</p>"