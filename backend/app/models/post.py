import datetime
from app import db, ma

#TODO 
#- Create all the columns
#- CRUD
#- Relationship with other tables

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    idade = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float, nullable=False)
    
