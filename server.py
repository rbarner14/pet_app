# For templating.
from jinja2 import StrictUndefined
# To instantiate app, enable communications between front &
# back ends, process info from forms, make requests, create sessions and jsonify
# python dictionaries for javascript and html.
from flask import (Flask, redirect, render_template, request, session, jsonify,
                   flash)
# To debug app.
from flask_debugtoolbar import DebugToolbarExtension
# To make API requests.
import requests
# To use secret keys.
import os
# For functions that pic randomly from arrays.
import random
# For pause for UX design. 
import time

# API keys.
forsquare_client_id = os.environ.get("FORSQUARE_CLIENT_ID")
forsquare_client_secret = os.environ.get("FORSQUARE_CLIENT_SECRET")
google_api_key = os.environ.get("GOOGLE_API_KEY")

# Instantiate Flask app.
app = Flask(__name__)

# For debugging.
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True
app.secret_key = "ABC"

# For raising errors to prevent app failing silently.
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def index():

    return render_template("homepage.html");


@app.route("/register")
def show_registration_form():

    return render_template("register.html")


@app.route("/login")
def show_login():

    return render_template("login.html")


@app.route("/users")
def show_users():

    return render_template("users.html");


# @app.route("/users.json")
# def show_users():

#     users = {

#     }

#     return jsonify(users);


@app.route("/profile/<int:id>")
def show_profile():

    return render_template("profile.html")


################################################################################
# Run app at command line.
if __name__ == "__main__":
    # For debugging.
    app.debug = True
    app.run(host="0.0.0.0")