"""Entry point fro TwitOff flask app"""
from .app import create_app

APP = create_app()

# if __name__ = '__main__':
#     my_app = create_app()
#     my_app.run(debug=True)

#     APP = create_app()