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

import logging
import datetime
import importlib

import time
#import gevent
#from gevent import monkey
#monkey.patch_all()


from flask import current_app

__license__ = "LGPLv3+"


log = logging.getLogger(__name__)


class UserOfficeLink:
    """Allows to retrieve information from the user office"""

    def __init__(self):
        self.site_user_office = None

    def init_app(self, app):
        module_name = app.config["USER_OFFICE_LINK_MODULE"]
        class_name = app.config["USER_OFFICE_LINK_CLASS"]
        cls = getattr(importlib.import_module(module_name), class_name)
        self.site_user_office = cls()
        self.site_user_office.init_app(app)

        #self.sync_polling = gevent.spawn_later(
        #    10,
        #    self.sync_with_user_office,
        #    app
        #)

    def sync_with_user_office(self):
        self.site_user_office.sync_all()

    def update_proposal(self, code, number):
        self.site_user_office.update_proposal(code, number)

user_office_link = UserOfficeLink()