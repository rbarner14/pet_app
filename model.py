from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy

class Venue(db.Model):
    """A dog-friendly venue."""

    __tablename__ = "venues"

    venue_id = 
    name = 

class Rating(db.Model):
    """Rating of a venue by a user."""

    __tablename__ = "ratings"

    rating_id = 
    venue_id = 
    user_id = 