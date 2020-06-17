from app import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # db.relationship is defined on the one side to get access to the many
    # The backref argument defines the name of a field that will be added to the objects of the "many"   class that points back at the "one" object.
    #

    def __repr__(self):
        return '<User {}>'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(144))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    # timestamp indexed if we want to retrieve in chronological order
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # here 'user' is the name of the table generated for the model User, hence user.id

    def __repr__(self):
        return '<Post {}>'.format(self.body)
