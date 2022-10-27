from flask import Flask, render_template, jsonify
from FlaskAPI.settings import MONGO_URI
from pprint import pprint

from .extensions import mongo, login_manager

from .routes.auth import auth
from .routes.main import main

def create_app(config_object='FlaskAPI.settings'):
    app = Flask(__name__)

    app.config.from_object((config_object))

    mongo.init_app(app)

    # login_manager.init_app(app)

    # login_manager.login_view = ''

    # @login_manager.load_user
    # def load_user(user_id):
    #     return User.query.get(user_id)

    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app