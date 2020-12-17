import json

from app import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    text = db.Column(db.String(30000), index=True)
    published_at = db.Column(db.DateTime)

    def __repr__(self):
        return '<User id: {}, text: {}, author_id: {}>'.format(self.id, self.text, self.author_id)

    def to_dict(self):
        comment = {
            'id': self.id,
            'author': self.author.to_dict(),
            'post_id': self.post_id,
            'text': self.text,
            'published_at': self.published_at,
        }
        return comment
