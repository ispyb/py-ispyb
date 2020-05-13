# encoding: utf-8
"""
API extension
=============
"""

from copy import deepcopy
from flask import current_app, Blueprint
from flask_restx import Api, Namespace


api_v1 = Api(
    version="1.0",
    title="ISPyB",
    description="ISPyB Flask rest server",
    doc="/doc",
    default="Main",
    default_label="Main",
)


def init_app(app, **kwargs):
    # pylint: disable=unused-argument
    """
    API extension initialization point.
    """
    # Prevent config variable modification with runtime changes
    api_v1.authorizations = deepcopy(app.config["AUTHORIZATIONS"])
