# encoding: utf-8
"""
API extension
=============
"""

from copy import deepcopy

from flask import current_app, Blueprint

from flask_restx import Api, Namespace
from .http_exceptions import abort

authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "X-API-KEY"}}
blueprint = Blueprint('api', __name__, url_prefix='/ispyb/api/v1')
api_v1 = Api(
    blueprint,
    version="1.0",
    title="ISPyB",
    description="ISPyB Flask restplus server",
    doc="/doc",
    authorizations=authorizations,
    default="Main",
    default_label="Main",
        )


def init_app(app, **kwargs):
    # pylint: disable=unused-argument
    """
    API extension initialization point.
    """
    #app.route('/swaggerui/<path:path>')(serve_swaggerui_assets)

    # Prevent config variable modification with runtime changes
    api_v1.authorizations = deepcopy(app.config['AUTHORIZATIONS'])
