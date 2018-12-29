import os
from project.config import BaseConfig
from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()


def create_app() -> Flask:
    """
    Flask application factory
    """
    app = Flask("ShortUrl")
    app_setting = os.getenv("FLASK_CONFIG", BaseConfig)
    app.config.from_object(app_setting)
    app.config['MONGODB_SETTINGS'] = {
        'db': 'urlDatabs'
    }

    # Initialize Database
    db.init_app(app)

    from project.api.hello import short_url_api_bp

    URL_PREFIX = app.config["URL_PREFIX"]
    app.register_blueprint(short_url_api_bp, url_prefix=URL_PREFIX)

    return app
