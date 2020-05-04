# encoding: utf-8
# pylint: disable=invalid-name,wrong-import-position,wrong-import-order
"""
ISPyB flask server
"""

from .logging import Logging
logging = Logging()

from .flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from .auth import AuthProvider
auth_provider = AuthProvider()

from . import api


def init_app(app):
    """
    Application extensions initialization.
    """
    for extension in (
            api,
            auth_provider,
            logging,
            db,
        ):
        extension.init_app(app)
