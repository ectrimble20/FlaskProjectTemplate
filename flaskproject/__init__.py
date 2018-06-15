import logging
from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flaskproject.config import Config
from flaskproject.database import database

# remove if you don't need encryption (flask_bcrypt)
crypt = Bcrypt()
# remove if you don't need user authentication (flask_login)
login_manager = LoginManager()


def create_application(configuration=Config):
    app = Flask(__name__)
    with app.app_context():
        """
        # customize the logger:
        logging.basicConfig(filename=configuration.LOGGING_FILE, level=configuration.LOGGING_LEVEL)
        # if you need SQL logging (for debug) or wrap it in an if configuration.DEBUG check
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
        # REMEMBER to reload the configuration if you change it
        app.config.from_object(configuration)
        """
        database.init_app(app)
        crypt.init_app(app)  # remove if you don't need encryption
        login_manager.init_app(app) # remove if you don't need authentication
        # load blue prints
        # to do this import the route blueprint (example):
        # from flaskproject.routes.user import user
        # register blue prints
        # to do this (example):
        # app.register_blueprint(user)  # user is the route blueprint from ex above
    return app
