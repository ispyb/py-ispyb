"""
Project: py-ispyb
https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.
"""


__license__ = "LGPLv3+"

import logging


class Logging(object):
    """
    This is a helper extension, which adjusts logging configuration for the
    application.
    """

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        """
        Common Flask interface to initialize the logging according to the
        application configuration.
        """
        # We don't need the default Flask's loggers when using our invoke tasks
        # since we set up beautiful colorful loggers globally.
        for handler in list(app.logger.handlers):
            app.logger.removeHandler(handler)
        app.logger.propagate = True

        if app.debug:
            logging.getLogger('flask_oauthlib').setLevel(logging.DEBUG)
            app.logger.setLevel(logging.DEBUG)

        # We don't need the default SQLAlchemy loggers when using our invoke
        # tasks since we set up beautiful colorful loggers globally.
        # NOTE: This particular workaround is for the SQLALCHEMY_ECHO mode,
        # when all SQL commands get printed (without these lines, they will get
        # printed twice).
        sqla_logger = logging.getLogger('sqlalchemy.engine.base.Engine')
        for hdlr in list(sqla_logger.handlers):
            sqla_logger.removeHandler(hdlr)
        sqla_logger.addHandler(logging.NullHandler())
