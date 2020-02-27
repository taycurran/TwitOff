from flask import Blueprint, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    return render_template("home.html")

@home_routes.route("/about")
def about():
    return "About Me"