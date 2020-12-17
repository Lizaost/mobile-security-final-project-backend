from app import app, db
from flask import jsonify
from datetime import datetime
import random
from app.users.model import User
from app.posts.model import Post
from app.comments.model import Comment


@app.route('/')
@app.route('/index')
def index():
    print(Post.query.all())
    return "Hello, World!"


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


from app.users.routes import *
from app.comments.routes import *
from app.posts.routes import *
