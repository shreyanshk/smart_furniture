from flask import Flask
from flask_sqlalchemy_session import flask_scoped_session

from .webui import webui
from .api import api
from .dbmodels import Session


def create_app():
	app = Flask(__name__)
	register_extensions(app)
	register_blueprints(app)
	return app


def register_extensions(app):
	flask_scoped_session.init_app(Session, app)


def register_blueprints(app):
	app.register_blueprint(api)
	app.register_blueprint(webui)
