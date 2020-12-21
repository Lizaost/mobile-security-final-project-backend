from app import app, db
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
    author_id = 40  # TODO: get user_id from token
    text = request.form.get('text')
    post_id = request.form.get('post_id')
    published_at = datetime.now()
    comment = Comment(text=text, author_id=author_id, post_id=post_id, published_at=published_at)
    db.session.add(comment)
    db.session.commit()
    return 'ok'
