# encoding: utf-8
"""
Logging adapter
---------------
"""
import logging

DEFAULT_LOG_FORMAT = "%(asctime)s |%(levelname)-5s| %(message)s"


class Logging(object):
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        if app.config.get("LOG_FILENAME"):
            fh = logging.FileHandler(app.config["LOG_FILENAME"])
            if app.config.get("LOG_FORMAT"):
                log_format = app.config["LOG_FORMAT"]
            else:
                log_format = DEFAULT_LOG_FORMAT
            fh.setFormatter(logging.Formatter(log_format))
            app.logger.addHandler(fh)
