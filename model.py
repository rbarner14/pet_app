from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Venue(db.Model):
    """A dog-friendly venue."""

    __tablename__ = "venues"

    venue_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.Text)
    address = db.Column(db.Text)
    img_url = db.Column(db.Text)

    def __repr__(self):
        """Provide helpful representation of Venue instance when printed."""

        return f"<Venue venue_id={self.venue_id} name={self.name}"

class User(db.Model):
    """A user(referred by app as owner) on platform."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text)
    username = db.Column(db.Text)
    email = db.Column(db.Text)
    password = db.Column(db.Text)

    def __repr__(self):
        """Provide a helpful representation of User instance when printed."""

        return f"<User user_id={self.user_id} email={self.email}>"


class Rating(db.Model):
    """Rating of a venue by a user."""

    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venues.venue_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    score = db.Column(db.Integer)

    # Establish relationships for easier query composition.
    venue = db.relationship("Venue", backref=db.backref("ratings", 
                                                        order_by=rating_id)) 
    user = db.relationship("User", backref=db.backref("rating", 
                                                      order_by=rating_id))

    def __repr__(self):
        """Provide a helpful resentation of Rating instance when printed."""

        return f"""<Rating rating_id={self.rating_id}
                         venue_id={self.venue_id}
                         user_id={self.user_id}
                         score={self.score}>"""


################################################################################
# Helper functions to connect to db.

def connect_to_db(app):

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///petvenues"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


################################################################################
# Create database model at command line.

if __name__ == "__main__":

    from server import app

    connect_to_db(app)

    print("Connected to DB.")


