"""Code for our app"""

from flask import Flask
from .models import DB
# Make our App Factory

def create_app():
    app = Flask(__name__)

    # Add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

    # Have the database know about the app
    DB.init_app(app)

    @app.route("/")
    def root():
        return "Welcome to Twitoff!"
    return app
