from app import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.relationship('User', backref='comments', lazy='dynamic')
    author_id = lecture_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    post = db.relationship('Post', backref='comments', lazy='dynamic')
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    text = db.Column(db.String(30000), index=True)
    published_at = db.Column(db.DateTime)

    def __repr__(self):
        return '<User id: {}, text: {}, author: {}>'.format(self.id, self.text, self.author.username)