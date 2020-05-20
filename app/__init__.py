# encoding: utf-8
# pylint: disable=no-member
#
#  Project: py-ispyb
#  https://github.com/ispyb/py-ispyb
#
#  This file is part of py-ispyb software.
#
#  py-ispyb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-ispyb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with MXCuBE. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"


import os
import sys

from flask import Flask
from flask_cors import CORS


CONFIG_NAME_MAPPER = {
    "development": "config.DevelopmentConfig",
    "testing": "config.TestingConfig",
    "production": "config.ProductionConfig",
}


def create_app(flask_config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """
    app = Flask(__name__, **kwargs)
    CORS(app)
    # TODO configure CORS via config file

    env_flask_config_name = os.getenv("FLASK_CONFIG")
    if flask_config_name is None:
        flask_config_name = env_flask_config_name
    if flask_config_name is None:
        flask_config_name = "testing"

    app.logger.debug("Starting ISPyB server in %s mode" % flask_config_name)
    try:
        app.config.from_object(CONFIG_NAME_MAPPER[flask_config_name])
    except ImportError:
        app.logger.error(  # pylint: disable=no-member
            "Unabled to start the ISPyB server with configuration %s"
            % flask_config_name
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
