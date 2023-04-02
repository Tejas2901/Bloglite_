from flask_restful import Resource, Api, marshal_with, fields, reqparse
from flask_security import auth_required
from flask import request
from flask_security import current_user
from application.jobs import task
from application.data.models import User,Blog,Follow_track,User_Search,Blog_likelog
import json
from datetime import date
from application.data.database import db
import os

from time import perf_counter_ns
from application.data import data_access
from application.data.data_access import cache


user_resource_fields = {
    "id": fields.Integer,
    "email":fields.String,
    "username": fields.String,
    "no_of_blogs":fields.Integer,
    "followers":fields.Integer,
    "following":fields.Integer
}




class TestAPI(Resource):
    @auth_required("token")
    def get(self):
        email = request.args.get('email')    
        blogs = data_access.get_blogs_by_userid(email)
        for i in blogs:
            no_of_likes = Blog.query.filter_by(id = i['blog_id']).first().no_of_likes
            i['no_of_likes'] = no_of_likes
        return blogs


class UserBlogsAPI(Resource):
    @auth_required("token")
    def get(self):
        username = request.args.get('username')
        if username is None:
            email = current_user.email
            user =User.query.filter_by(email=email).first()
        else:
            user = User.query.filter_by(username = username).first()
        blog = Blog.query.filter(Blog.author_id  == user.id).all()
        blogs = []
        j = 1
        for i in blog:
            b = {}
            author = User.query.filter_by(id=i.author_id).first()
            b['pp'] = author.profile_picture
            b['blog_id'] = i.id
            b['title'] = i.title
            b['description'] = i.description
            b['by'] = author.username
            b['image'] = i.image
            b['no_of_likes'] = i.no_of_likes
            
            blogs.append(b)        
        return blogs


class UserAPI(Resource):
    # @marshal_with(user_resource_fields)
    @auth_required("token")
   
    def get(self):
            email = request.args.get('email')
            print(email)
            if(email is None):
                username = request.args.get('username')
                user = User.query.filter_by(username = username).first()
                                
            else:
                user = User.query.filter_by(email = email).first()

            # GET followers
            followers_arr =[]
            user_followers = Follow_track.query.filter_by(followed_id = user.id).all()
            print(user_followers)
            for i in user_followers:
                user_i = User.query.filter_by(id=i.follower_id).first().username
                followers_arr.append(user_i)
            print(followers_arr)
            
            following_arr = []
            user_followers = Follow_track.query.filter_by(follower_id = user.id).all()
            print(user_followers)
            for i in user_followers:
                user_i = User.query.filter_by(id=i.followed_id).first().username
                following_arr.append(user_i)
            print(following_arr)
            
            user = {
                        "id":user.id,
                        "profile_picture":user.profile_picture,
                        "pref":user.pref,
                        "email":user.email,
                        "username": user.username,
                        "no_of_blogs":user.no_of_blogs,
                        "followers":user.followers,
                        "following":user.following,
                }
            return [user,followers_arr,following_arr]

    def post(self):
        user = current_user
        image = request.files.get('image')
        if image:
            filename_ = image.filename

            # save the image in static folder
            image_path = os.path.join('static',filename_)
            image.save(image_path)
            image_path = 'http://localhost:8080/'+ os.path.join('static',filename_)
            
            print(image_path)
            user.profile_picture = image_path
            db.session.commit()
        return "Image Changed"
            
class CreateBlog(Resource):
    @auth_required("token")
    def post(self):
        #parsing the request payload
        
        email = request.args.get('email')
        user = User.query.filter_by(email = email).first()
        nb = user.no_of_blogs
        title_ = request.form.get('title')
        print(title_)
        
        description_ = request.form.get('description')
        print(description_)
        
        image_ = request.files.get('image')
        print(image_)
        filename_ = image_.filename
        now = date.today()
        
        # save the image in static folder
        image_path = os.path.join('static',filename_)
        image_.save(image_path)
        image_path = 'http://localhost:8080/'+ os.path.join('static',filename_)
        
        print(image_path)
        blog =Blog.query.filter(Blog.title ==title_).first()
        if blog is None:

            new_blog =Blog(title = title_,
                           image = image_path,
                           creation_date = now,
                           description = description_,
                           author_id = user.id)
            db.session.add(new_blog)
            user.no_of_blogs = nb + 1
            db.session.commit()

        # print("received something")
        return('Recieved Something')
    
    def put(self):

        blog_id = request.args.get('blog_id')
        
        title_ = request.form.get('title')
        print(title_)

        description_ = request.form.get('description')
        print(description_)

        #Update the blog
        editblog = Blog.query.filter(Blog.id==blog_id).first()
        editblog.title = title_
        
        editblog.description = description_
       
        
        image_ = request.files.get('image')
        if image_ is None:
            image_ = request.form.get('image')
            editblog.image = image_
            db.session.commit()
        else:
            filename_ = image_.filename

            # save the image in static folder
            image_path = os.path.join('static',filename_)
            image_.save(image_path)
            image_path = 'http://localhost:8080/'+ os.path.join('static',filename_)
            
            print(image_path)
            editblog.image = image_path
            db.session.commit()
    
    def delete(self):
        email = current_user.email
        blog_id = request.args.get('blog_id')
        Blog.query.filter(Blog.id == blog_id).delete()
        
        user = User.query.filter_by(email = email).first()
        nb = user.no_of_blogs
        user.no_of_blogs = nb - 1
        db.session.commit()
        
        
class UpdateUser(Resource):
    def post(self):
        email = request.args.get('email')
        update_user =  User.query.filter(User.email == email).update(dict(username = "rakesh"))
        db.session.commit()
        return "Done"

class CheckFollow(Resource):
    @auth_required("token")
    def get(self):
        user1 = request.args.get('user1')
        user2 = request.args.get('user2')
        user1_id = User.query.filter_by(email=user1).first().id
        user2_id = User.query.filter_by(username = user2).first().id
        check = Follow_track.query.filter(Follow_track.follower_id == user1_id, Follow_track.followed_id == user2_id).first()
        print(check)
        print("Check request")
        if(check):
            print(True)
            return True
        else:
            print(False)
            return False

class LogFollow(Resource):
    @auth_required("token")
    def post(self):
        user1 = request.args.get('user1')
        user2 = request.args.get('user2')
        user1_id = User.query.filter_by(email=user1).first().id
        user2_id = User.query.filter_by(username = user2).first().id
        new_follow = Follow_track(
                follower_id = user1_id,
                followed_id = user2_id
        )
        db.session.add(new_follow)
        User.query.filter_by(email=user1).first().following += 1
        User.query.filter_by(username = user2).first().followers += 1
        db.session.commit()
        return "done"
        
    def delete(self):
        user1 = request.args.get('user1')
        user2 = request.args.get('user2')
        user1_id = User.query.filter_by(email=user1).first().id
        user2_id = User.query.filter_by(username = user2).first().id
        delete_follow = Follow_track.query.filter(Follow_track.follower_id == user1_id, Follow_track.followed_id == user2_id).delete()
        
        User.query.filter_by(email=user1).first().following -= 1
        User.query.filter_by(username = user2).first().followers -= 1
        db.session.commit()
        return "done"


class Followers(Resource):
    @auth_required("token")
    def get(self):

        """
            This api returns the list of followers of a particular user
            Takes email of the user as argument.

        Returns:
            List() : Followers_array
        """

        followers_arr = []
        email = request.args.get('email')
        user_id = User.query.filter_by(email=email).first().id
        user_followers = Follow_track.query.filter_by(followed_id = user_id).all()
        print(user_followers)
        for i in user_followers:
            user_i = User.query.filter_by(id=i.follower_id).first().username
            followers_arr.append(user_i)
        print(followers_arr)
        return followers_arr

class Following(Resource):
    @auth_required("token")
    def get(self):

        """
            Produces a list of People the user is currently following
            Takes email of the user as an argument

        Returns:
            List(): Following_array
        """
        
        following_arr = []
        email = request.args.get('email')
        user_id = User.query.filter_by(email=email).first().id
        user_followers = Follow_track.query.filter_by(follower_id = user_id).all()
        print(user_followers)
        for i in user_followers:
            user_i = User.query.filter_by(id=i.followed_id).first().username
            following_arr.append(user_i)
        print(following_arr)
        return following_arr

class BlogCsv(Resource):
    @auth_required("token")
    def get(self):
        user_id = current_user.id
        email = current_user.email
        job = task.send_blogs_csv_task(email,user_id)
        # job = task.send_mail_task()
        return "done"

class Search(Resource):
    @auth_required("token")
    def get(self):
        q = request.args.get('q')+'*'
        results = User_Search.query.filter(User_Search.username.op("MATCH")(q)).all()
        users = []
        for i in results:
            users.append(i.username)
        return users

class Blog_like(Resource):
    @auth_required("token")
    def get(self):
        user = current_user
        user_id = user.id
        blog_id = request.args.get('blog_id')
        Like = Blog_likelog.query.filter(Blog_likelog.blog_id == blog_id, Blog_likelog.liked_by == user_id).first()
        if(Like != None):
            return True
        else:
            return False

    def post(self):
        user = current_user
        user_id = user.id
        blog_id = request.args.get('blog_id')
        new_blog_like = Blog_likelog(
                        blog_id = blog_id,
                        liked_by = user_id,
                        when = date.today()
        )
        blog = Blog.query.filter_by(id = blog_id).first()
        blog.no_of_likes = 1 + blog.no_of_likes
        db.session.add(new_blog_like)
        db.session.commit()
        return "Like Added"
    
    def delete(self):
        user = current_user
        user_id = user.id
        blog_id = request.args.get('blog_id')
        Like = Blog_likelog.query.filter(Blog_likelog.blog_id == blog_id, Blog_likelog.liked_by == user_id).first()
        blog = Blog.query.filter_by(id = blog_id).first()
        blog.no_of_likes = blog.no_of_likes - 1
        db.session.delete(Like)
        db.session.commit()
        return "Like Deleted"


class Pref(Resource):
    def post(self):
        pref = request.args.get('pref')
        user = current_user 
        user.pref = pref
        db.session.commit()
        return "Preference changed"