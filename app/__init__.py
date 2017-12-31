# app/__init__.py

# built-in
import os

# 3rd party
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth



# local import
from instance.config import app_config


# initialize sql-alchemy
db = SQLAlchemy()

# initialize flaskapp
flaskapp = FlaskAPI(__name__, instance_relative_config=True)
config_name = os.getenv('APP_SETTINGS') # config_name = "development"
secret_key  = os.getenv('SECRET')
flaskapp.config.from_object(app_config[config_name])

##app.config.from_pyfile('config.py')
flaskapp.config['SECRET_KEY'] = secret_key
flaskapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
flaskapp.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db.init_app(flaskapp) #Similar to db = SQLAlchemy(flaskapp)

# initialize http auth
auth = HTTPBasicAuth()

# Import all models
# from app.models.Bucketlist import Bucketlist

# Import all app routes
import app.routes.Bucketlist
import app.routes.Auth 

