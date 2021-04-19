from ..views import user, helper
from app import app
from flask import request, jsonify

@app.route('/api/user', methods=['POST'])
def post_user():
    return user.post_user()

@app.route('/jwt-auth/v1/token', methods=['POST'])
def authenticate_user():
    return helper.auth()

@app.route('/api/user', methods=['GET'])
def test():
    return helper.token_required_test()