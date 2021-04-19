from flask import Flask, jsonify
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import string
import random
import os

random_string = string.ascii_letters + string.digits + string.ascii_uppercase
#print(random_string)
key = ''.join(random.choice(random_string) for i in range(12))

basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__)
#app.config.from_object('config')
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = key
db = SQLAlchemy(app)
ma = Marshmallow(app)

CORS(app)

from .models import user
from .routes import routes