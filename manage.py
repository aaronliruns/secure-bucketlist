# manage.py

import os
from flask_script import Manager # class for handling a set of commands
from flask_migrate import Migrate, MigrateCommand
from app import db, flaskapp
from instance.config import app_config
##from app import models

config_name=os.getenv('APP_SETTINGS')
flaskapp.config.from_object(app_config[config_name])

migrate = Migrate(flaskapp, db)
manager = Manager(flaskapp)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
