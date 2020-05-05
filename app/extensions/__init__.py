# encoding: utf-8
# pylint: disable=invalid-name,wrong-import-position,wrong-import-order
"""
ISPyB flask server
"""

from . import api
from .auth import AuthProvider
from .flask_sqlalchemy import SQLAlchemy
from .logging import Logging

logging = Logging()

db = SQLAlchemy()

auth_provider = AuthProvider()


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
