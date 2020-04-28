# encoding: utf-8
"""
API extension
=============
"""

from copy import deepcopy

from flask import current_app

from flask_restx import Api, Namespace
#from .namespace import Namespace
from .http_exceptions import abort

authorizations = {"apikey": {"type": "apiKey", "in": "header", "name": "X-API-KEY"}}
api_v1 = Api( # pylint: disable=invalid-name
    version="1.0",
    title="ISPyB",
    description="ISPyB Flask restplus server",
    doc="/doc",
    authorizations=authorizations,
    default="Main",
    default_label="Main",
        )


def serve_swaggerui_assets(path):
    """
    Swagger-UI assets serving route.
    """
    if not current_app.debug:
        import warnings
        warnings.warn(
            "/swaggerui/ is recommended to be served by public-facing server (e.g. NGINX)"
        )
    from flask import send_from_directory
    return send_from_directory('../static/', path)


def init_app(app, **kwargs):
    # pylint: disable=unused-argument
    """
    API extension initialization point.
    """
    app.route('/swaggerui/<path:path>')(serve_swaggerui_assets)

    # Prevent config variable modification with runtime changes
    api_v1.authorizations = deepcopy(app.config['AUTHORIZATIONS'])
