"""
Project: py-ispyb.

https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along
"""


__license__ = "LGPLv3+"


import os
import ruamel.yaml


class BaseConfig:
    """Base config class"""

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
    STATIC_ROOT = os.path.join(PROJECT_ROOT, "static")

    API_ROOT = "/ispyb/api/v1"
    SECRET_KEY = os.urandom(16)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_POOL_RECYCLE = 2999
    # SQLALCHEMY_POOL_TIMEOUT = 20
    PAGINATION_ITEMS_LIMIT = 100

    DEBUG = True
    ERROR_404_HELP = False
    REVERSE_PROXY_SETUP = bool(os.getenv("EXAMPLE_API_REVERSE_PROXY_SETUP", ""))

    AUTHORIZATIONS = {
        "apikey": {"type": "apiKey", "in": "header", "name": "Authorization"}
    }

    AUTHORIZATION_RULES = {}

    AUTH_MODULE = "pyispyb.app.extensions.auth.DummyAuth"
    AUTH_CLASS = "DummyAuth"
    JWT_CODING_ALGORITHM = "HS256"
    TOKEN_EXP_TIME = 60  # in minutes
    MASTER_TOKEN = "MasterToken"
    ADMIN_ROLES = ["manager", "admin"] # allows to access all resources

    SWAGGER_UI_JSONEDITOR = True
    SWAGGER_UI_OAUTH_CLIENT_ID = "documentation"
    SWAGGER_UI_OAUTH_REALM = "Authentication for ISPyB server documentation"
    SWAGGER_UI_OAUTH_APP_NAME = "ISPyB server documentation"

    CSRF_ENABLED = True

    USER_OFFICE_LINK_MODULE = "pyispyb.app.extensions.user_office_link.DummyUserOfficeLink"
    USER_OFFICE_LINK_CLASS = "DummyUserOfficeLink"
    #USER_OFFICE_SYNC_INTERVAL = 60 * 60 * 5 #in seconds
    USER_OFFICE_SYNC_INTERVAL = 30

    def __init__(self, config_filename=None):
        with open(config_filename) as f:
            config = ruamel.yaml.load(f.read(), ruamel.yaml.RoundTripLoader)

            for key, value in config["server"].items():
                setattr(self, key, value)

            if config.get("authorization_rules") is not None:
                self.AUTHORIZATION_RULES = {}
                for key, value in config["authorization_rules"].items():
                    self.AUTHORIZATION_RULES[key] = value

        print("Authorization rules: ")
        print("[method] Endpoint - Allowed roles")
        for endpoint, value in self.AUTHORIZATION_RULES.items():
            for method, roles in value.items():
                print("[%s] %s - %s" % (method, endpoint, str(roles)))


class ProductionConfig(BaseConfig):
    """Production config

    Args:
        BaseConfig ([type]): [description]
    """
    def __init__(self, config_filename=None):
        super().__init__(config_filename)

        SECRET_KEY = os.getenv("EXAMPLE_API_SERVER_SECRET_KEY")
        SQLALCHEMY_DATABASE_URI = os.getenv("EXAMPLE_API_SERVER_SQLALCHEMY_DATABASE_URI")
        MASTER_TOKEN = None


class DevelopmentConfig(BaseConfig):
    """Dev config

    Args:
        BaseConfig ([type]): [description]
    """
    def __init__(self, config_filename=None):
        super().__init__(config_filename)

        DEBUG = True


class TestingConfig(BaseConfig):
    """Testing config

    Args:
        BaseConfig ([type]): [description]
    """
    def __init__(self, config_filename=None):
        super().__init__(config_filename)
    
        TESTING = True
