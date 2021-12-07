from src import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class Courses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    tags = db.Column(db.Text)
    categories = db.Column(db.Text)
    link = db.Column(db.Text, nullable=False)
    type = db.Column(db.String(120), nullable=False)
    featured = db.Column(db.Text)
    level = db.Column(db.String(20))
    created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
