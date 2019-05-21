# For templating.
from jinja2 import StrictUndefined
# To instantiate app, enable communications between front &
# back ends, process info from forms, make requests, create sessions and jsonify
# python dictionaries for javascript and html.
from flask import (Flask, redirect, render_template, request, session, jsonify,
                   flash)
# To debug app.
from flask_debugtoolbar import DebugToolbarExtension
from model import User, Venue, Rating, connect_to_db, db
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
    """Show homepage."""

    return render_template("homepage.html");


@app.route("/register", methods=["GET"])
def registration_form():
    """Show registration form."""

    return render_template("register.html")


@app.route("/login", methods=["GET"])
def login():
    """Show login form."""

    return render_template("login.html")

@app.route("/login", methods=["POST"])
def process_login():
    """Process login ."""

    email = request.form["email"]
    password = request.password["password"]

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("No user by that email is registered.")
        return redirect("/login")
    
    if password != user.password:
        flash("Incorrect password.")
        return redirect("/login")

    session["user_id"] = user.user_id

    flash(f"Welcome back, {user.name}")

    return redirect(f"/profile/{user_id}")


@app.route("/users")
def show_users(user):
    """Show users on platform in HTML format."""

    return render_template("users.html");


# @app.route("/users.json")
# def show_users():
#     """Show users on platform in JSON format."""

#     users = {

#     }

#     return jsonify(users);


@app.route("/users/<int:user_id>")
def show_profile(user_id):
    """Show user's profile."""

    return redirect(f"/profile/{user_id}")


################################################################################
# Run app at command line.
if __name__ == "__main__":
    # For debugging.
    app.debug = True
    app.run(host="0.0.0.0")



    