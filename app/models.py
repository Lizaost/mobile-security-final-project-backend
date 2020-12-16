from app import db


class Lecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(100), index=True, unique=True)
    title = db.Column(db.String(1000), index=True, unique=True)
    cover = db.Column(db.String(1000), index=True)
    is_visible = db.Column(db.Boolean, index=True)
    order = db.Column(db.Integer, index=True)
    slides = db.relationship('Slide', backref='lecture', lazy='dynamic')

    def __repr__(self):
        return '<Lecture title: {}>'.format(self.title)
