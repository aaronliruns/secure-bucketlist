# app/__init__.py

# built-in
import os

# 3rd party
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy


# local import
from instance.config import app_config


# initialize sql-alchemy
db = SQLAlchemy()

flaskapp = FlaskAPI(__name__, instance_relative_config=True)
config_name = os.getenv('APP_SETTINGS') # config_name = "development"
flaskapp.config.from_object(app_config[config_name])
##app.config.from_pyfile('config.py')

flaskapp.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(flaskapp) #Similar to db = SQLAlchemy(flaskapp)

# Import all models
# from app.models.Bucketlist import Bucketlist

# Import all app routes
import app.routes.Bucketlist 

