from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config):
    """Init Flask application."""
    app = Flask(__name__)
    app.config.from_object(config)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    from .index import index as index_blueprint
    app.register_blueprint(index_blueprint)

    return app