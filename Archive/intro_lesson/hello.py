"""Minimal Flask App"""

from flask import Flask, render_template

# Make the Application
app = Flask(__name__)

# Make the Route
@app.route("/") # Home Page

# Now Define a Function

def hello():
    return "Hello World!"

# Make a 2nd Route

@app.route("/about")

# Now Make Function that Goes with About
def preds():
    return render_template("about.html")