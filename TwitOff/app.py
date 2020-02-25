"""Code for our app"""

from decouple import config
from flask import Flask, render_template, request
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
        return render_template('base.html')
    return app
