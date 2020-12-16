from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), index=True, unique=True)
    first_name = db.Column(db.String(30), index=True)
    last_name = db.Column(db.String(30), index=True)
    email = db.Column(db.String(100), index=True)
    password_hash = db.Column(db.String(10000))
    status = db.Column(db.String(1000))
    registered_at = db.Column(db.DateTime)

    def __repr__(self):
        return '<User id: {}, email: {}>'.format(self.id, self.email)
