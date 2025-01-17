# storing roots for the website

from flask import Blueprint, render_template


# define that this file is a blueprint of application
# setting up a blueprint
views = Blueprint("views", __name__)

@views.route("/")
def home_page():
    return render_template("home.html")