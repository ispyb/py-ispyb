"""Project: py-ispyb.

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


from flask import current_app
from pyispyb.app.extensions.user_office_link.AbstractUserOfficeLink import AbstractUserOfficeLink


class DummyUserOfficeLink(AbstractUserOfficeLink):
    
    def init_app(self, app):
        """Initializes user office class.

        Args:
            app (flask app): Flask app
        """
        return
    
    def sync_all(self):
        """Main method to sync with user office"""
        print("Sync with user office")

    def update_proposal(self, code, number):
        """Updates proposal based on the code and number.

        Args:
            code (str): MX, SAXS, mxihr, etc
            number (int): proposals number
        """
        print("Update proposal %s%d" %(code, number))
