from datetime import datetime
from app import app, db
from app.auth.tokens_utils import decode_auth_token
from app.posts.model import Post
from flask import jsonify, request


@app.route('/api/posts', methods=['GET'])
def get_all_posts():
    # print(request.cookies)
    posts = Post.query.all()
    if posts:
        posts_list = [post.to_dict() for post in posts]
        print(posts_list)
        return jsonify(posts_list)
    else:
        return jsonify([])


@app.route('/api/posts/<post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.filter(Post.id == post_id).first()
    if post:
        post_dict = post.to_dict()
        return jsonify(post_dict)
    else:
        return jsonify({})


@app.route('/api/users/<author_id>/posts', methods=['GET'])
def get_user_posts(author_id):
    posts = Post.query.filter(Post.author_id == author_id)
    if posts:
        posts_list = [post.to_dict() for post in posts]
        return jsonify(posts_list)
    else:
        return jsonify([])


@app.route('/api/posts', methods=['POST'])
def create_post():
    auth_token = request.cookies.get('accessToken')
    author_id = None
    if auth_token:
        resp = decode_auth_token(auth_token)
        if not isinstance(resp, str):
            author_id = resp
        else:
            raise Exception('Unauthorized user')
    data = request.json
    title = data['title']
    text = data['text']
    published_at = datetime.now()
    post = Post(title=title, text=text, author_id=author_id, published_at=published_at)
    db.session.add(post)
    db.session.commit()
    return jsonify({'status': 'success', 'user_id': author_id})
