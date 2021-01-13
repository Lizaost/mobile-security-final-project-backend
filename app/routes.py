import os
from os import listdir
from os.path import isfile, isdir, join

from app import app, db
from flask import jsonify, make_response, render_template, send_from_directory
from datetime import datetime
import random
from app.users.model import User
from app.posts.model import Post
from app.comments.model import Comment


@app.route('/')
@app.route('/index')
def serve():
    return 'Hello from backend'


@app.route('/init')
def init_random_data():
    password_hash = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'
    users = [None, None, None]
    for i in range(0, 3):
        rand_int_str = str(random.randint(1, 1000))
        users[i] = User(username='test_' + rand_int_str, first_name=rand_int_str, last_name=rand_int_str,
                        email=f'test_{rand_int_str}@example.com', password_hash=password_hash,
                        status=f'I am a test user {rand_int_str}', registered_at=datetime.now())
        print(users[i])
        db.session.add(users[i])
    posts = [None, None, None]
    for i in range(0, 3):
        rand_int_str = str(random.randint(1, 1000))
        posts[i] = Post(title=f'Test post {rand_int_str}', text=f'Example post with random int {rand_int_str}',
                        author=users[i], published_at=datetime.now())
        print(posts[i])
        db.session.add(posts[i])
    for i in range(0, 3):
        rand_int_str = str(random.randint(1, 1000))
        comment = Comment(text=f'Test comment for post {i}, rand int {rand_int_str}', author=users[i], post=posts[i],
                          published_at=datetime.now())
        print(comment)
        db.session.add(comment)
    db.session.commit()
    print(Post.query.all())
    return "Initialized random posts, users and comments"


@app.route('/set-test-cookies', methods=['GET', 'POST'])
def set_test_cookies():
    resp = make_response(jsonify({'token': 'test_access_token'}))
    resp.set_cookie('accessToken', 'test_access_token')
    return resp


@app.route('/get-cookies')
def get_test_cookies():
    print(request.cookies)
    token = request.cookies.get('accessToken')
    return jsonify({'token': token})


@app.route('/upload', methods=['POST'])
def upload_image():
    category = request.form.get('category')
    print(category)
    uploads_dir = os.path.join(app.static_folder, 'images', category)
    os.makedirs(uploads_dir, exist_ok=True)
    image = request.files.get('image')
    print(image.filename)
    print(os.path.join(uploads_dir, image.filename))
    image.save(os.path.join(uploads_dir, image.filename))
    return 'ok', 200


@app.route('/get-images', methods=['GET'])
def get_all_uploaded_images():
    images_folder = os.path.join(app.static_folder, 'images')
    categories = [f for f in listdir(images_folder) if isdir(join(images_folder, f))]
    images = {}
    for c in categories:
        images[c] = [f for f in listdir(join(images_folder, c)) if isfile(join(images_folder, c, f))]
    return jsonify(images)


@app.route('/get-images/<category>', methods=['GET'])
def get_images_by_category(category):
    category_folder = os.path.join(app.static_folder, 'images', category)
    if isdir(category_folder):
        images = [f for f in listdir(category_folder) if isfile(join(category_folder, f))]
        return jsonify(images)
    else:
        return 'No such category: ' + category, 404


from app.users.routes import *
from app.comments.routes import *
from app.posts.routes import *
from app.auth.routes import *
