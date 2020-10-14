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
from logging.config import dictConfig

DEFAULT_LOG_FORMAT = "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': DEFAULT_LOG_FORMAT,
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

class Logging(object):
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        return
        for handler in list(app.logger.handlers):
            app.logger.removeHandler(handler)
        app.logger.propagate = True

        if app.debug:
            logging.getLogger('flask_oauthlib').setLevel(logging.DEBUG)
            app.logger.setLevel(logging.DEBUG)

        """
        if app.config.get("LOG_FILENAME"):
            fh = logging.FileHandler(app.config["LOG_FILENAME"])
            if app.config.get("LOG_FORMAT"):
                log_format = app.config["LOG_FORMAT"]
            else:
                log_format = DEFAULT_LOG_FORMAT
            fh.setFormatter(logging.Formatter(log_format))
            app.logger.addHandler(fh)
        """
