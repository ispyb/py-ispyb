# encoding: utf-8
#
#  Project: py-ispyb
#  https://github.com/ispyb/py-ispyb
#
#  This file is part of py-ispyb software.
#
#  py-ispyb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-ispyb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"


import os
import csv


class BaseConfig():

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

    API_ROOT = "/ispyb/api/v1"
    SECRET_KEY = os.urandom(16)
    SQLALCHEMY_DATABASE_URI = 'mysql://mxuser:mxpass@localhost/pydb_test'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    #SQLALCHEMY_POOL_RECYCLE = 2999
    #SQLALCHEMY_POOL_TIMEOUT = 20
    PAGINATION_ITEMS_LIMIT = 20

    DEBUG = True
    ERROR_404_HELP = False
    REVERSE_PROXY_SETUP = os.getenv('EXAMPLE_API_REVERSE_PROXY_SETUP', False)

    AUTHORIZATIONS = {
        "apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}
    }

    AUTH_MODULE = "app.extensions.auth.DummyAuth"
    AUTH_CLASS = "DummyAuth"
    JWT_CODING_ALGORITHM = 'HS256'
    TOKEN_EXP_TIME = 60  # in minutes
    MASTER_TOKEN = "MasterToken"

    ENABLED_MODULES = (
        'api',
    )

    ENABLED_DB_MODULES = []

    with open('%s/enabled_db_modules.csv' % PROJECT_ROOT) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if not row[0].startswith("#"):
                ENABLED_DB_MODULES.append(row[0])

    ENABLED_ROUTES = [
        'auth',
        'auto_proc',
        'data_collection',
        'proposal',
        'session',
        'schemas',
    ]

    SWAGGER_UI_JSONEDITOR = True
    SWAGGER_UI_OAUTH_CLIENT_ID = 'documentation'
    SWAGGER_UI_OAUTH_REALM = "Authentication for ISPyB Flask-RESTx server documentation"
    SWAGGER_UI_OAUTH_APP_NAME = "ISPyB Flask-RESTx server documentation"

    CSRF_ENABLED = True

    LOG_FILENAME = "/tmp/ispyb_server.log"
    #LOG_FORMAT = "%(asctime)s |%(levelname)-5s| %(message)s"


class ProductionConfig(BaseConfig):
    SECRET_KEY = os.getenv('EXAMPLE_API_SERVER_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.getenv('EXAMPLE_API_SERVER_SQLALCHEMY_DATABASE_URI')
    MASTER_TOKEN = None


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class TestingConfig(BaseConfig):
    TESTING = True
