# storing roots for the website

from flask import Blueprint, render_template, request


# define that this file is a blueprint of application
# setting up a blueprint
authentication = Blueprint("authentication", __name__)

@authentication.route("/login", methods=["GET", "POST"])
def login():
    # data = request.form
    # print(data) printuje w dict dane from (hasło, username)
    return render_template("login.html", text="Testing...")

@authentication.route("/logout")
def logout():
    return "<p>Logout</p>"

@authentication.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    return render_template("sign_up.html")

@authentication.route("/profile")
def profile():
    return "<p>Profile</p>"