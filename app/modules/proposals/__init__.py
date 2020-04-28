from app.extensions.api import api_v1


def init_app(app, **kwargs):
    # pylint: disable=unused-argument,unused-import
    """
    Init proposals module.
    """
    #api_v1.add_oauth_scope('proposals:read', "Provide access to proposals")
    #api_v1.add_oauth_scope('proposals:write', "Provide write access to proposals details")

    # Touch underlying modules
    #Move moduels to app/extensions/db
    from app import models
    from . import resources

    api_v1.add_namespace(resources.api)

