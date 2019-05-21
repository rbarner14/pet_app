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
# For Google & Forsquare API calls.
from findAVenue import findAVenue

# API keys.
forsquare_client_id = os.environ.get("FORSQUARE_CLIENT_ID")
forsquare_client_secret = os.environ.get("FORSQUARE_CLIENT_SECRET")
google_api_key = os.environ.get("GOOGLE_API_KEY")

# Instantiate Flask app.
app = Flask(__name__)

# For debugging.
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
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


@app.route("/register", methods=["POST"])
def process_register():
    """Process registration."""

    email = request.form["email"]
    username = request.form["username"]
    password = request.form["password"]
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]

    user = User.query.filter_by(email=email).first()

    if user:
        flash("A user with that email is already registered.")
        
        return redirect("/register")
    else:
        new_user = User(first_name=first_name, last_name=last_name, 
                        username=username, email=email, password=password)
        
        db.session.add(new_user)
        db.session.commit()

        flash("User successfully registered!")

        return redirect("/login")


@app.route("/login", methods=["GET"])
def login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"]) # Why post if only referencing DB?
def process_login():
    """Process login."""

    username = request.form["username"]
    password = request.form["password"]

    user = User.query.filter_by(username=username).first()

    if not user:
        flash("No user by that username is registered.")
        return redirect("/login")
    
    if password != user.password:
        flash("Incorrect password.")
        return redirect("/login")

    session["user_id"] = user.user_id

    flash(f"Welcome back, {user.first_name}")

    return redirect(f"/users/{user.user_id}")

@app.route("/logout")
def logout():
    """Log out user from session."""

    if session.get("user_id"):
        del session["user_id"]

        flash("Logged out.")

    return redirect("/")


@app.route("/users")
def show_users():
    """Show users on platform in HTML format."""

    users = User.query.all()

    return render_template("users.html", users=users);


@app.route("/users.json")
def show_users_json():
    """Show users on platform in JSON format."""

    users = User.query.all()
    all_users = {}

    for user in users:
        all_users[user.username] = {
            "id": user.user_id,
            "name": f"{user.first_name} {user.last_name}"
        }

    return jsonify(all_users)


@app.route("/users/<int:user_id>")
def show_profile(user_id):
    """Show user's profile."""

    user = User.query.get(user_id)

    return render_template("user_profile.html", user=user)


@app.route("/search_result", methods=["POST"])
def show_search_result():

    location = request.form["location"]

    venue = findAVenue(location)

    name = venue.get("name", "")
    img_url = venue.get("img_url", "")
    address = venue.get("address","")

    matched_venue = Venue.query.filter_by(img_url=img_url).first()
    print(matched_venue)

    if venue == "No matching venues.":
        flash("No result for that location.  Try, 'San Francisco, CA'.")
        return redirect("/")

    if matched_venue:

        return render_template("search_result.html", matched_venue=matched_venue)
    else:
        matched_venue = None
        if img_url: 
            new_venue = Venue(name=name, address=address, img_url=img_url)
        
        db.session.add(new_venue)
        db.session.commit()

        return render_template("search_result.html", name=name, img_url=img_url,
                                address=address, matched_venue=matched_venue)


################################################################################
# Run app at command line.
if __name__ == "__main__":
    # For debugging.
    app.debug = True

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")


