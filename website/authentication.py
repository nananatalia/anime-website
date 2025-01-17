# storing roots for the website

from flask import Blueprint, render_template


# define that this file is a blueprint of application
# setting up a blueprint
authentication = Blueprint("authentication", __name__)

@authentication.route("/login")
def login():
    return render_template("login.html")

@authentication.route("/logout")
def logout():
    return "<p>Logout</p>"

@authentication.route("/sign-up")
def sign_up():
    return render_template("sign_up.html")

@authentication.route("/profile")
def profile():
    return "<p>Profile</p>"