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

from pyispyb import config

__license__ = "LGPLv3+"


CONFIG_NAME_MAPPER = {
    "dev": "DevelopmentConfig",
    "test": "TestingConfig",
    "prod": "ProductionConfig",
}

def create_app(config_path=None, run_mode="dev", **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """

    app = Flask(__name__, **kwargs)
    CORS(app)
    # TODO configure CORS via config file

    env_config_path = os.getenv("ISPYB_CONFIG")
    if config_path is None:
        config_path = env_config_path
    if config_path is None:
        config_path = "ispyb_core_config.yml"

    app.logger.debug("Starting ISPyB server in %s mode" % run_mode)

    try:
        config_obj = getattr(config, CONFIG_NAME_MAPPER[run_mode])
        app.config.from_object(config_obj(config_path))
    except ImportError as ex:
        app.logger.error(  # pylint: disable=no-member
            "Unabled to start the ISPyB server with configuration %s (%s)" % (
                config_path,
                str(ex))
        )
        app.logger.error(str(ex))
        sys.exit(1)
        raise

    from pyispyb.app import extensions

    extensions.init_app(app)

    service_module = importlib.import_module("pyispyb." + app.config["SERVICE_NAME"])
    service_module.init_app(app)

    from pyispyb.app import routes

    routes.init_app(app)

    # import ispyb_service_connector
    # ispyb_service_connector.check_service_connection(app.config["SERVICE_CONNECTIONS"])

    app.logger.debug("ISPyB server started")
    return app