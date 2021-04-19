import datetime
from app import db, ma

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(500), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())
    name = db.Column(db.String(20), unique=False, nullable=False)
   
    #posts = db.relationship('Posts', backref='users', lazy=True)
    #commentaries = db.relationship('Commentaries', backref='users', lazy=True)

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.name = username



class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'name', 'email', 'password', 'created_on')


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)