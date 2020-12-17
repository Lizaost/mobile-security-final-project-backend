import json

from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), index=True)
    text = db.Column(db.String(30000), index=True)
    published_at = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def __repr__(self):
        return '<Post id: {}, title: {}>'.format(self.id, self.title)

    def to_dict(self):
        post = {
            'id': self.id,
            'title': self.title,
            'text': self.text,
            'published_at': self.published_at,
            'author': self.author.to_dict()
        }
        return post
