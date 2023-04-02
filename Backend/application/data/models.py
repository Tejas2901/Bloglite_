from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

from application.data.database import db
import datetime

roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(),
                                 db.ForeignKey('User.id')),
                       db.Column('role_id', db.Integer(),
                                 db.ForeignKey('role.id')))

# The roles_users table is used to establish a
# many-to-many relationship between the Users 

# and Role classes. In a many-to-many relationship
# , a single user can have multiple roles and a single
# role can have multiple users. The roles_users table 
# is used to store the relationship between users and
# roles, with a user_id column and a role_id column.
# Each row in the table represents a single relationship
# between a user and a role. The backref on the Users
# and Role classes allows for easy access to the related
# rows in the other table.

class User(db.Model, UserMixin):
    __tablename__ = 'User'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    no_of_blogs = db.Column(db.Integer, default = 0)
    followers = db.Column(db.Integer, default = 0)
    following = db.Column(db.Integer, default = 0)
    pref = db.Column(db.Integer,default = 0)
    profile_picture = db.Column(db.String,default = "http://localhost:8080/static/pp_placeholder.jpg")
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('user', lazy='dynamic'))
    blogs = db.relationship('Blog', backref='user', lazy='subquery')


class Role(db.Model, RoleMixin):
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class Blog(db.Model):
    __tablename__ = 'Blog'
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    title = db.Column(db.String, nullable=False)
    image = db.Column(db.String)
    description = db.Column(db.String)
    creation_date = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('User.id'),
                        nullable=False)
    no_of_likes= db.Column(db.Integer, default = 0)
    
class Follow_track(db.Model):
    __tablename__ = 'Follow_track'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    follower_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable = False)
    followed_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable = False)

class User_Search(db.Model):
    __tablename__ = 'User_Search'
    rowid = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String) 


class Blog_likelog(db.Model):
    __tablename__ = 'Blog_likelog'
    id = db.Column(db.Integer, autoincrement = True, primary_key = True)
    blog_id = db.Column(db.Integer, db.ForeignKey(Blog.id), nullable = False)
    liked_by = db.Column(db.Integer, db.ForeignKey(User.id), nullable = False)
    when = db.Column(db.String)