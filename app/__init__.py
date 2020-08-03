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
#  along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


import os
import sys
import importlib

from flask import Flask
from flask_cors import CORS


__license__ = "LGPLv3+"


CONFIG_NAME_MAPPER = {
    "ispyb_core_dev": "ispyb_core_config.DevelopmentConfig",
    "ispyb_core_test": "ispyb_core_config.TestingConfig",
    "ispyb_core_prod": "ispyb_core_config.ProductionConfig",

    "ispyb_ssx_dev": "ispyb_ssx_config.DevelopmentConfig",
    "ispyb_ssx_test": "ispyb_ssx_config.TestingConfig",
    "ispyb_ssx_prod": "ispyb_ssx_config.ProductionConfig",
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
        flask_config_name = "ispyb_core_test"

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

    service_module = importlib.import_module(app.config["SERVICE"])
    service_module.init_app(app)

    from . import routes

    routes.init_app(app)

    #import ispyb_service_connector
    #ispyb_service_connector.check_service_connection(app.config["SERVICE_CONNECTIONS"])

    app.logger.debug("ISPyB server started")
    return app
