
from flask import Blueprint, jsonify, request, render_template

home_routes = Blueprint("home_routes", __name__)

    
@home_routes.route("/")
def index():
    users = User.query.all()
    return render_template('base.html', title='Home',
                                users=users)

@home_routes.route("/about")
def about():
    return "About Me"

@home_routes.route('/reset')
def reset():
    DB.drop_all()
    DB.create_all()
    return render_template('base.html', title='Reset', users=[])

# # Add config for database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# # stop tracking modifications on sqlalchemy config
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # ? app.config["TWITTER_API_CLIENT"] = twitter

# # Have the database know about the app
# DB.init_app(app)