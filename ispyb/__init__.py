#!/usr/bin/env python3
import os
import sys
import configparser
from logging.config import dictConfig

import werkzeug

if not hasattr(werkzeug, "cached_property"):
    werkzeug.cached_property = werkzeug.utils.cached_property

from flask import Flask, Blueprint
from flask_restplus import Api
from flask_sqlalchemy import SQLAlchemy


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

db = SQLAlchemy(app)
#-------------------------------------------------------------------------------------#
# Define api
#-------------------------------------------------------------------------------------#
authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "token"}}
blueprint = Blueprint('api', __name__, url_prefix='/ispyb/api/v1')
api = Api(
    blueprint,
    version="1.0",
    title="ISPyB",
    description="ISPyB Flask restplus server",
    doc="/doc",
    authorizations=authorizations,
    default="Main",
    default_label="Main",
)


#-------------------------------------------------------------------------------------#
# Add apis as namespaces
#-------------------------------------------------------------------------------------#
from ispyb.apis.login import ns as login_ns
from ispyb.apis.autoproc import ns as autoproc_ns
from ispyb.apis.crystal import ns as crystal_ns
from ispyb.apis.data_collection import ns as dc_ns
from ispyb.apis.data_collection_group import ns as dcgr_ns
from ispyb.apis.proposal import ns as prop_ns
from ispyb.apis.sample import ns as sample_ns

api.add_namespace(login_ns)
api.add_namespace(autoproc_ns)
api.add_namespace(crystal_ns)
api.add_namespace(dc_ns)
api.add_namespace(dcgr_ns)
api.add_namespace(prop_ns)
api.add_namespace(sample_ns)

app.register_blueprint(blueprint, url_prefix='/ispyb/api/v1')

if __name__ == "__main__":
    app.run(debug=config["general"].get("debug_mode", False))
