"""Minimal Flask App"""

from flask import Flask

# Make the Application
app = Flask(__name__)

# Make the Route
@app.route("/") # Home Page

# Now Define a Function

def hello:
    return "Hello World!"