# encoding: utf-8
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

from datetime import datetime, timedelta
from suds.client import Client
from suds.transport.http import HttpAuthenticated


from pyispyb.app.extensions.user_office_link.AbstractUserOfficeLink import AbstractUserOfficeLink
from pyispyb.core.modules import proposal 


class SmisLink(AbstractUserOfficeLink):
    
    def init_app(self, app):
        """Initializes user office class.

        Args:
            app (flask app): Flask app
        """
        http_auth = HttpAuthenticated(
            username=app.config.get("SMIS_USERNAME"),
            password=app.config.get("SMIS_PASSWORD")
            )
        self.smis_ws = Client(
            app.config.get("SMIS_WS_URL"),
            transport=http_auth,
            cache=None,
            timeout=180
            )

    def sync_all(self):
        # Get 1 month old proposals
        print("sync proposals")
        past_str = datetime.strftime(datetime.now() - timedelta(days=30), '%d/%m/%YYYY')
        now_str = datetime.strftime(datetime.now(), "%d/%m/%YYYY")
        smis_proposals = self.smis_ws.service.findNewMXProposalPKs(past_str, now_str)
        current_proposals = proposal.get_db_proposals()

        print(smis_proposals)
        print(current_proposals)
        print("Done!")