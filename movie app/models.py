from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
db = SQLAlchemy()

class Movie(db.Model):
    """Movie Model - Represents movie table in database"""
    id = db.Column(db.Integer, primary=True)
    title = db.Columnn(db.String(200), nullable=False)
    year = db.Column(db.Integer)
    genre = db.Column(db.String(50))
    director = db.Column(db.Float)
    rating = db.Column(db.Float)
    rating = db.Column(db.Text)
    poster_url = db.Column(db.String(500))
    # created_at = db.Column(db.datetime, default=datetime.utcnow)
    created_at = db.Column(db.datetime, ()(timezone=True))
    default = lambda:datetime.cow(timezone.utc)

    def __repr__(self):
        return f"<Movie: {self.title} ({self.year})>"