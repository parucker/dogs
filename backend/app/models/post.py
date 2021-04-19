import datetime
from app import db, ma

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idade = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    