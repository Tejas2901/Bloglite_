from application.data.models import User,Blog,Follow_track
from flask import current_app as app
from flask_caching import Cache

cache = Cache(app)
app.app_context().push()

# @cache.cached(timeout = 50, key_prefix = "get_all_blogs")
@cache.memoize(50)
def get_blogs_by_userid(email):
    print("in data access")
    user_id = User.query.filter_by(email=email).first().id
    user_followers = Follow_track.query.filter_by(follower_id = user_id).all()
    print(user_followers)
    feed_blogs = []
    for i in user_followers:
        user_i = Blog.query.filter_by(author_id=i.followed_id).all()
        feed_blogs.extend(user_i)
    print(feed_blogs)
    # blog = Blog.query.filter(Blog.author_id != user.id).all()
    blogs = []
    j = 1
    for i in feed_blogs:
        b = {}
        author = User.query.filter_by(id=i.author_id).first()
        b['pp'] = author.profile_picture        
        b['blog_id'] = i.id
        b['title'] = i.title
        b['description'] = i.description
        b['by'] = author.username
        b['image'] = i.image
        
        j += 1
        blogs.append(b)  
    return blogs