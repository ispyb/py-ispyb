"""ISPyB flask server"""

from app.extensions.api import api_v1


def init_app(app, **kwargs):
    return

    # from . import resources

    # api_v1.add_namespace(resources.api)
