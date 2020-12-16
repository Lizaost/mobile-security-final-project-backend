from app import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(1000), index=True)
    text = db.Column(db.String(30000), index=True)
    published_at = db.Column(db.DateTime)
    author = db.relationship('User', backref='posts', lazy='dynamic')
    author_id = lecture_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return '<Post id: {}, title: {}, author: {}>'.format(self.id, self.title, self.author.username)
