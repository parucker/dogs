from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify, make_response
from ..models.user import User, user_schema, users_schema


def post_user():
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    print(username, password, email)

    pass_hash = generate_password_hash(password)
    print(pass_hash)
    user = User(username, pass_hash, email)
    print(user)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({'message': 'successfully registered', 'data': result }), 201
    except:
        return jsonify({'message': 'unable to create', 'data': {}}), 500

def user_by_username(username):
    try:
        return User.query.filter(User.username == username).one()
    except:
        return None

def get_user(id):
    user = User.query.get(id)
    if user:
        result = user_schema.dump(user)
        print("Result",result)
        return result
    return jsonify({'message': "user don't exist", 'data': {}}), 404