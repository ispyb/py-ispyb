#!/usr/bin/env python3
import os
import sys
import configparser
from logging.config import dictConfig

import werkzeug

if not hasattr(werkzeug, "cached_property"):
    werkzeug.cached_property = werkzeug.utils.cached_property

from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api, Resource, fields
from flask import Flask, Blueprint


fname = os.path.dirname(__file__)
sys.path.insert(0, fname)

config = configparser.ConfigParser()
config_filename = os.path.join(os.path.dirname(__file__), "../config.cfg")
config.read(config_filename)

#-------------------------------------------------------------------------------------#
# Logging
#-------------------------------------------------------------------------------------#

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

#-------------------------------------------------------------------------------------#
# Init Flask
#-------------------------------------------------------------------------------------#

app = Flask(__name__)
app.config["SECRET_KEY"] = config["general"].get("secret_key", "ispyb_secret_key")
app.config["SQLALCHEMY_DATABASE_URI"] = config["general"]["db_uri"]
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SWAGGER_UI_JSONEDITOR"] = True

authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "token"}}

api_v1 = Blueprint("api", __name__, url_prefix="/ispyb/api/v1")
api = Api(
    api_v1,
    version="1.0",
    title="ISPyB",
    description="ISPyB Flask restplus server",
    doc="/doc",
    authorizations=authorizations,
    default="Main",
    default_label="Main namespace",
)
app.register_blueprint(api_v1)

db = SQLAlchemy(app)

#-------------------------------------------------------------------------------------#
# Import routes
#-------------------------------------------------------------------------------------#

from ispyb.routes import login, proposal


if __name__ == "__main__":
    app.run(debug=config["general"].get("debug_mode", False))
