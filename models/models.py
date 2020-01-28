from datetime import datetime

from pytweet.database import db

from flask_login import UserMixin


class User(UserMixin,db.Model):

    __tablename__="users"

    id = db.Column(db.Integer,primary_key= True)
    fullname = db.Column(db.String(255),nullable=False)
    username = db.Column(db.String(255),nullable=False)
    password = db.Column(db.String(255),nullable=False)

    posts = db.relationship('Post',backref="author",lazy=True)

    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.now,onupdate=datetime.now)


class Profile(db.Model):

    __tablename__="profile"
    
    id = db.Column(db.Integer,primary_key= True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    first_name = db.Column(db.String(255),nullable=False)
    last_name = db.Column(db.String(255),nullable=False)
    address = db.Column(db.String(255),nullable=False)
    occupation = db.Column(db.String(255),nullable=False)
    birthday = db.Column(db.String(255),nullable=False)
    skills = db.Column(db.String(255),nullable=False)
    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.now,onupdate=datetime.now)


class Post(db.Model):

    __tablename__="post"
    
    id = db.Column(db.Integer,primary_key= True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    comments = db.relationship('Comment',backref="post",lazy=True)
    post = db.Column(db.String(1000),nullable=False)
    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.now,onupdate=datetime.now)
   

class Comment(db.Model):

    __tablename__="comment"
    
    id = db.Column(db.Integer,primary_key= True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    comment = db.Column(db.String(1000),nullable=False)
    post_id = db.Column(db.Integer,db.ForeignKey('post.id'),nullable=False)
    created_at = db.Column(db.DateTime,nullable=False,default=datetime.now)
    updated_at = db.Column(db.DateTime,nullable=False,default=datetime.now,onupdate=datetime.now)
    