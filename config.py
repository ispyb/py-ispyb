import os
import csv

class BaseConfig(object):
    SECRET_KEY = 'this-really-needs-to-be-changed'

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

    # POSTGRESQL
    # DB_USER = 'user'
    # DB_PASSWORD = 'password'
    # DB_NAME = 'restplusdb'
    # DB_HOST = 'localhost'
    # DB_PORT = 5432
    # SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}:{port}/{name}'.format(
    #     user=DB_USER,
    #     password=DB_PASSWORD,
    #     host=DB_HOST,
    #     port=DB_PORT,
    #     name=DB_NAME,
    # )

    SQLALCHEMY_DATABASE_URI = 'mysql://mxuser:mxpass@localhost/pydb_test'

    DEBUG = False
    ERROR_404_HELP = False

    REVERSE_PROXY_SETUP = os.getenv('EXAMPLE_API_REVERSE_PROXY_SETUP', False)

    AUTHORIZATIONS = {
        #'oauth2_password': {
        #    'type': 'oauth2',
        #    'flow': 'password',
        #    'scopes': {},
        #    'tokenUrl': '/auth/oauth2/token',
        #},
        "apikey": {"type": "apiKey", "in": "header", "name": "X-API-KEY"}
    }

    #RESTX_MASK_HEADER = "token"

    AUTH_MODULE = "app.extensions.auth.DummyAuth"
    AUTH_CLASS = "DummyAuth"
    MASTER_TOKEN = "MasterToken"

    ENABLED_MODULES = (
        'api',
        'login',
    )

    ENABLED_DB_MODULES = []

    with open('%s/enabled_db_modules.csv' % PROJECT_ROOT) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            ENABLED_DB_MODULES.append(row[0])


    STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

    SWAGGER_UI_JSONEDITOR = True
    SWAGGER_UI_OAUTH_CLIENT_ID = 'documentation'
    SWAGGER_UI_OAUTH_REALM = "Authentication for ISPyB Flask-RESTplus server documentation"
    SWAGGER_UI_OAUTH_APP_NAME = "ISPyB Flask-RESTplus server documentation"

    # TODO: consider if these are relevant for this project
    SQLALCHEMY_TRACK_MODIFICATIONS = True
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
