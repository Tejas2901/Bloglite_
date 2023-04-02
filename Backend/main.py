import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
from application import config
from application.config import LocalDevelopmentConfig
from application.data.database import db
from sqlalchemy.orm import scoped_session,sessionmaker
from flask_security import Security, SQLAlchemySessionUserDatastore, SQLAlchemyUserDatastore
from application.data.models import User, Role
from flask_login import LoginManager
from flask_security import utils
from application.jobs import workers
from application.utils import helpers

from flask import send_from_directory

app = None
api = None
celery = None


app = Flask(__name__, static_url_path='/static')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


# allow cross origin
CORS(app)


#configure the app and connect it to the database
app.config.from_object(LocalDevelopmentConfig)
db.init_app(app)
app.app_context().push()

#Setup flask Security
user_datastore = SQLAlchemySessionUserDatastore(db.session,User,Role)
security = Security(app, user_datastore)

#Add api
api = Api(app)
app.app_context().push()

#Add Celery
celery = workers.celery

#Update with configuration

celery.conf.update(
    broker_url = app.config['CELERY_BROKER_URL'],
    backend_url = app.config['CELERY_BACKEND_URL']
)
print('celery config done')

celery.Task = workers.ContextTasK
app.app_context().push()

# #Add Cache
# cache = Cache(app)
# app.app_context().push()
from application.controller.controllers import *

from application.controller.api import TestAPI,UserAPI,UserBlogsAPI,CreateBlog,UpdateUser, CheckFollow, LogFollow,Followers,Following,BlogCsv,Search,Blog_like,Pref
api.add_resource(TestAPI,'/api')
api.add_resource(UserAPI,'/api/user')
api.add_resource(CreateBlog, '/api/createblog')
api.add_resource(UpdateUser, '/api/updateuser')
api.add_resource(CheckFollow,'/api/checkfollow')
api.add_resource(LogFollow,'/api/logfollow')
api.add_resource(Followers,'/api/followers')
api.add_resource(Following,'/api/following')
api.add_resource(UserBlogsAPI,'/api/userblogs')
api.add_resource(BlogCsv,'/api/blogscsv')
api.add_resource(Search,'/api/search')
api.add_resource(Blog_like,'/api/like')
api.add_resource(Pref,'/api/pref')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)