from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')
    # db.relationship is defined on the one side to get access to the many
    # The backref argument defines the name of a field that will be added to the objects of the "many"   class that points back at the "one" object.
    def set_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

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

@login.user_loader
#since flask-login doesnt know about our tables, it excpects the app to configure a                   user loader function
def load_user(id):
    return User.query.get(int(id))
