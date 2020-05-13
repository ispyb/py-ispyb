# encoding: utf-8
# pylint: disable=no-member
"""
Example RESTful API Server.
"""
import os
import sys

from flask import Flask


CONFIG_NAME_MAPPER = {
    'development': 'config.DevelopmentConfig',
    'testing': 'config.TestingConfig',
    'production': 'config.ProductionConfig',
}

def create_app(flask_config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """
    app = Flask(__name__, **kwargs)

    env_flask_config_name = os.getenv('FLASK_CONFIG')
    if flask_config_name is None:
        flask_config_name = env_flask_config_name
    if flask_config_name is None:
        flask_config_name = 'testing'

    app.logger.debug("Starting ISPyB server in %s mode" % flask_config_name)
    try:
        app.config.from_object(CONFIG_NAME_MAPPER[flask_config_name])
    except ImportError:
        app.logger.error(  # pylint: disable=no-member
                "Unabled to start the ISPyB server with configuration %s" % flask_config_name
        )
        sys.exit(1)
        raise

    from . import extensions
    extensions.init_app(app)

    from . import modules
    modules.init_app(app)

    from . import routes
    routes.init_app(app)

    app.logger.debug("ISPyB server started")
    return app
