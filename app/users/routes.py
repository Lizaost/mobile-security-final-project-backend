from app import app, db
from app.users.model import User
from flask import jsonify, request
from datetime import datetime
from hashlib import sha256


@app.route('/api/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    if users:
        users_list = [user.to_dict() for user in users]
        return jsonify(users_list)
    else:
        return jsonify([])


@app.route('/api/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.filter(User.id == user_id).first()
    if user:
        user_dict = user.to_dict()
        return jsonify(user_dict)
    else:
        return jsonify({})


@app.route('/api/users', methods=['POST'])
def create_user():
    username = request.form.get('username')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    # TODO: Maybe it will be more secure to transfer hash of password, not password itself
    # almost no need if HTTPS is used since client-side code is easily visible
    password = request.form.get('password')
    status = request.form.get('status')
    registered_at = datetime.now()
    password_hash = sha256(password.encode('utf-8')).hexdigest()
    print(password_hash)
    user = User(username=username, first_name=first_name, last_name=last_name, email=email,
                registered_at=registered_at, status=status, password_hash=password_hash)
    db.session.add(user)
    db.session.commit()
    return 'ok'


@app.route('/api/users/<user_id>', methods=['PUT'])
def edit_user(user_id):
    user = User.query.filter(User.id == user_id).first()
    if request.form.get('username'):
        user.username = request.form.get('username')
    if request.form.get('first_name'):
        user.first_name = request.form.get('first_name')
    if request.form.get('last_name'):
        user.last_name = request.form.get('last_name')
    if request.form.get('status'):
        user.status = request.form.get('status')
    db.session.commit()
    return 'ok'