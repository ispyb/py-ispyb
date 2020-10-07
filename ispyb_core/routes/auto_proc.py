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


from flask_restx_patched import Resource

from app.extensions.api import api_v1, Namespace
from app.extensions.auth import token_required

from ispyb_core.modules import auto_proc


__license__ = "LGPLv3+"


api = Namespace(
    "Auto processing", description="Auto processing related namespace", path="/autoproc"
)

api_v1.add_namespace(api)


@api.route("")
class AutoProcList(Resource):
    """Auto processing resource"""

    @api.doc(security="apikey")
    # @token_required
    def get(self):
        """Returns all auto processing results"""
        # app.logger.info('Returns all auto proc results')
        auto_proc.get_auto_proc_list()
