"""Code for our app"""

from decouple import config
from flask import Flask, render_template, request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .models import DB, User

from TWITOFF.routes.home_routes import home_routes
from TWITOFF.routes.book_routes import book_routes

# Make our App Factory
def create_app():
    app = Flask(__name__)

    # configuring the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite///web_app_11.db"
    
    db = SQLAlchemy(app)
    migrate = Migrate(app, db)

    class Book(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(128))
        author_id = db.Column(db.String(128))

    # Registering Routes
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)

    return app

    # # Add config for database
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # # stop tracking modifications on sqlalchemy config
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # # ? app.config["TWITTER_API_CLIENT"] = twitter

    # # Have the database know about the app
    # DB.init_app(app)

    # @app.route("/")
    # def index():
    #     users = User.query.all()
    #     return render_template('base.html', title='Home',
    #                                 users=users)
    
    # @app.route("/about")
    # def about():
    #     return "About Me"

    # @app.route('/reset')
    # def reset():
    #     DB.drop_all()
    #     DB.create_all()
    #     return render_template('base.html', title='Reset', users=[])

    # return app