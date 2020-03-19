#!/usr/bin/env python3
import os
import sys
import configparser

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth


fname = os.path.dirname(__file__)
sys.path.insert(0, fname)

config = configparser.ConfigParser()
config_filename = os.path.join(os.path.dirname(__file__), "../config.cfg")
config.read(config_filename)


server = Flask(__name__)
server.config['SECRET_KEY'] = 'very secret key...'
server.config['SQLALCHEMY_DATABASE_URI'] = "%s://%s:%s@%s/%s" %    (
        config["db_connection"]["engine"],
        config["db_connection"]["usr"],
        config["db_connection"]["pwd"],
        config["db_connection"]["host"],
        config["db_connection"]["db_name"],
    )
server.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(server)
auth = HTTPBasicAuth()

from ispyb.routes import (proposal)


if __name__ == "__main__":
    server.run(debug=True)
