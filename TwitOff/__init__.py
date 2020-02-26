"""Entry point fro TwitOff flask app"""
from .app import create_app

APP = create_app()

if __name__ == "__main__":
    APP = create_app()
    APP.run(debug=True)
