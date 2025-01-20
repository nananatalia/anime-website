# storing roots for the website

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


# define that this file is a blueprint of application
# setting up a blueprint
authentication = Blueprint("authentication", __name__)

@authentication.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        # looking in databse for our user, by email
        user =  User.query.filter_by(email=email).first()
        # if we actually find the user
        if user:
            if check_password_hash(user.password, password):
                flash("Login successfully!", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home_page"))
            else:
                flash("Incorrect login or password! Try again.", category="error")
        else:
            flash("User not found.", category="error")


    # testing purpose
    # data = request.form
    # print(data) printuje w dict dane from (hasło, username)
        

    return render_template("login.html", text="Testing...")

@authentication.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("authentication.login"))


@authentication.route("/sign-up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        userName = request.form.get("userName")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")

        user = User.query.filter_by(email=email).first()
        if user:
            flash("Email already exist!", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.", category="error")
        elif len(userName) < 2:
            flash("User name must be greater than 1 characters.", category="error")
        elif password1 != password2:
            flash("Passwords don't match.", category="error")
        elif len(password1) < 7:
            flash("Password must be at least 7 characters.", category="error")
        else:
            # creating new user
            new_user = User(email=email, userName=userName, password=generate_password_hash(password1, method="sha256"))
            # adding and updating database
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            # add user to database
            flash("Account successfully created!", category="success")
            # when everything ids working, we're moving to home page
            return redirect(url_for("views.home_page")) # views.home_page because that's where the function is views.py -> home_page()

    return render_template("sign_up.html")

@authentication.route("/profile")
def profile():
    return "<p>Profile</p>"