import hashlib
from flask import request, make_response, jsonify
from app import User, db
from app.auth.tokens_utils import encode_auth_token, decode_auth_token
from app.auth.blacklist_token_model import BlacklistToken


def check_login_status():
    print('Checking login status')
    return True


def login(email, password):
    print('Logging in')
    try:
        # fetch the user data
        user = User.query.filter_by(
            email=email
        ).first()
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if user.password_hash != password_hash:
            raise Exception('Wrong password')
        auth_token = encode_auth_token(user.id, 60 * 30)
        if auth_token:
            responseObject = {
                'status': 'success',
                'message': 'Successfully logged in.',
                'auth_token': auth_token.decode()
            }
            resp = make_response(jsonify(responseObject))
            resp.set_cookie('accessToken', auth_token.decode())
            return resp, 200
    except Exception as e:
        print(e)
        responseObject = {
            'status': 'fail',
            'message': 'Try again'
        }
        return make_response(jsonify(responseObject)), 500


def register(username, first_name, last_name, email, password, status):
    print('Registering')
    # get the post data
    post_data = request.get_json()
    # check if user already exists
    responseObject = {}
    user = User.query.filter_by(email=email).first()
    if not user:
        try:
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password_hash=password_hash,
                status=status
            )

            # insert the user
            db.session.add(user)
            db.session.commit()
            # generate the auth token
            auth_token = encode_auth_token(user_id=user.id, expire_at=60 * 30)
            responseObject = {
                'status': 'success',
                'message': 'Successfully registered.',
                'auth_token': auth_token.decode()
            }
            resp = make_response(jsonify(responseObject))
            resp.set_cookie('accessToken', auth_token.decode())
            return resp, 201
        except Exception as e:
            responseObject = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
        return make_response(jsonify(responseObject)), 401
    else:
        responseObject = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return make_response(jsonify(responseObject)), 202


def logout():
    print('Logging out')
    # get auth token
    # auth_header = request.headers.get('Authorization')
    # if auth_header:
    #     auth_token = auth_header.split(" ")[1]
    # else:
    #     auth_token = ''
    auth_token = request.cookies.get('accessToken')
    if auth_token:
        resp = decode_auth_token(auth_token)
        if not isinstance(resp, str):
            # mark the token as blacklisted
            blacklist_token = BlacklistToken(token=auth_token)
            try:
                # insert the token
                db.session.add(blacklist_token)
                db.session.commit()
                responseObject = {
                    'status': 'success',
                    'message': 'Successfully logged out.'
                }
                resp = make_response(jsonify(responseObject))
                resp.set_cookie('accessToken', '', max_age=0)
                return resp, 200
            except Exception as e:
                responseObject = {
                    'status': 'fail',
                    'message': e
                }
                return make_response(jsonify(responseObject)), 200
        else:
            responseObject = {
                'status': 'fail',
                'message': resp
            }
            return make_response(jsonify(responseObject)), 401
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Provide a valid auth token.'
        }
        return make_response(jsonify(responseObject)), 403


def get_current_user_profile():
    print('Getting current user profile')
    # get the auth token
    auth_header = request.headers.get('Authorization')
    if auth_header:
        auth_token = auth_header.split(" ")[1]
    else:
        auth_token = ''
    if auth_token:
        resp = decode_auth_token(auth_token)
        if not isinstance(resp, str):
            user = User.query.filter_by(id=resp).first()
            responseObject = {
                'status': 'success',
                'data': {
                    'user_id': user.id,
                    'email': user.email,
                    'admin': user.admin,
                    'registered_on': user.registered_on
                }
            }
            return make_response(jsonify(responseObject)), 200
        responseObject = {
            'status': 'fail',
            'message': resp
        }
        return make_response(jsonify(responseObject)), 401
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Provide a valid auth token.'
        }
        return make_response(jsonify(responseObject)), 401
