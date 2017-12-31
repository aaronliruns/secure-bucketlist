import os
config_name = os.getenv('APP_SETTINGS') # config_name = "development"

from app import db,flaskapp
print("type=" + str(type(flaskapp)))

from instance.config import app_config
flaskapp.config.from_object(app_config[config_name])

if __name__ == '__main__':
    flaskapp.run()
