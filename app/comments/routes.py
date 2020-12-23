from app import app, db
from app.auth.tokens_utils import decode_auth_token
from app.comments.model import Comment
from flask import jsonify, request
from datetime import datetime


@app.route('/api/comments/<comment_id>', methods=['GET'])
def get_comment(comment_id):
    comment = Comment.query.filter(Comment.id == comment_id).first()
    if comment:
        comment_dict = comment.to_dict()
        return jsonify(comment_dict)
    else:
        return jsonify({})


@app.route('/api/posts/<post_id>/comments', methods=['GET'])
def get_post_comments(post_id):
    comments = Comment.query.filter(Comment.post_id == post_id)
    if comments:
        comments_list = [comment.to_dict() for comment in comments]
        return jsonify(comments_list)
    else:
        return jsonify([])


@app.route('/api/comments', methods=['POST'])
def create_comment():
    auth_token = request.cookies.get('accessToken')
    author_id = None
    print(auth_token)
    if auth_token:
        resp = decode_auth_token(auth_token)
        if not isinstance(resp, str):
            author_id = resp
        else:
            raise Exception('Unauthorized user')
    data = request.json
    post_id = data['post_id']
    text = data['text']
    published_at = datetime.now()
    comment = Comment(text=text, author_id=author_id, post_id=post_id, published_at=published_at)
    print(comment)
    db.session.add(comment)
    db.session.commit()
    return jsonify({'status': 'success'})
