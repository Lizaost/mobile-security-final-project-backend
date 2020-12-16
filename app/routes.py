from app import app
from flask import jsonify


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


from app.users.routes import *
from app.comments.routes import *
from app.posts.routes import *
