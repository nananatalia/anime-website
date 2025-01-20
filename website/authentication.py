# storing roots for the website

from flask import Blueprint, render_template, request, flash


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
    if request.method == "POST":
        email = request.form.get("email")
        userName = request.form.get("userName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        if len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(userName) < 2:
            flash("User name must be greater than 1 characters.", category="error")
        elif password1 != password2:
            flash("Passwords don't match.", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters.", category="error")
        else:
            # add user to database
            flash("Account successfully created!", category="success")

    return render_template("sign_up.html")

@authentication.route("/profile")
def profile():
    return "<p>Profile</p>"