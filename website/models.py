from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Post(db.Model):
    id =db.Column(db.Integer, primary_key = True)
    title= db.Column(db.String(1000))
    description = db.Column(db.String(10000))
    date= db.Column(db.DateTime(timezone=True), default=func.now())
    img_name = db.Column(db.String(), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    comments= db.relationship('Comments', backref='post', lazy='dynamic', cascade = 'all, delete, delete-orphan')


class User(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    username = db.Column(db.String(64), index=True, unique=True)
    posts = db.relationship('Post', backref='user', lazy='dynamic')
    comments = db.relationship('Comments', backref='user_commenter', lazy='dynamic')

class Comments(db.Model, UserMixin):
    id= db.Column(db.Integer, primary_key = True)
    comment = db.Column(db.String(128), unique=False, index=False)
    post_id=db.Column(db.Integer, db.ForeignKey('post.id'))
    user_commenter_id = db.Column(db.Integer,db.ForeignKey('user.id'))
