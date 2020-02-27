"""Code for our App"""

import os
from dotenv import load_dotenv

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from TWITOFF.models import db, User, Tweet, migrate
from TWITOFF.routes import routes

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", default="OOPS")

# Make App Factory
def create_app():
    app = Flask(__name__)
    app.config["CUSTOM_VAR"] = 5
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(routes)

    return app











# --- Archived Imports ---
# from decouple import config
# from flask import Flask, render_template, request
# from flask import jsonify
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# from .models import DB, User

# from TWITOFF.routes.home_routes import home_routes
# from TWITOFF.routes.book_routes import book_routes