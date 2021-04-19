import datetime
from functools import wraps
from app import app
from flask import request, jsonify
from .user import user_by_username, get_user
import jwt
from werkzeug.security import check_password_hash

def auth():
    username = request.json['username']
    password = request.json['password']

    auth = request.authorization

    #if not auth or not username or not password:
    #    return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401
    print(username, password)
    
    user = user_by_username(username)
    print("USer", user)
    print
    if not user:
        return jsonify({'message': 'user not found', 'data': []}), 401

    print(app.config['SECRET_KEY'])
    if user and check_password_hash(user.password, password):
        token = jwt.encode({'username': user.username}, app.config['SECRET_KEY'])
        return jsonify({'message': 'Validated successfully', 'token': token.decode('UTF-8')})

    return jsonify({'message': 'could not verify', 'WWW-Authenticate': 'Basic auth="Login required"'}), 401

    
def token_required_test():
    token = request.headers['Authorization'].replace("Bearer ", "")
    if not token:
            return jsonify({'message': 'Missing Token', 'data': {}}), 401
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'])
        print("Token decode", data)
        
        current_user = user_by_username(username=data['username'])
        print("Current,",current_user)
        id = current_user.id
        email = current_user.email
        username = current_user.userna,e
    except:
        return jsonify({'message': 'Invalid Token', 'data': {}}), 401
    #TODO - return only the necessary information
    return jsonify(current_user), 200