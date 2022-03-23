"""
Project: py-ispyb.

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

from flask import request
from pyispyb.core.modules.proposal import find_proposal_id
from flask_restx import Resource


from pyispyb.app.extensions.api import api_v1, Namespace, legacy_api
from pyispyb.app.extensions.auth.decorators import authentication_required, permission_required

from pyispyb.core.modules import session


__license__ = "LGPLv3+"

log = logging.getLogger(__name__)
api = Namespace(
    "Sessions", description="Session related namespace", path="/sessions")
api_v1.add_namespace(api)


@api.route("")
@api.doc(security="apikey")
@legacy_api.route("/<token>/session/list")
class SessionsInfos(Resource):
    @authentication_required
    @permission_required("any", ["own_sessions", "all_sessions"])
    def get(self, **kwargs):
        """Get all sessions that user is allowed to access."""
        if "all_sessions" in request.user['permissions']:
            return session.get_session_infos_all()
        return session.get_session_infos_login(request.user['username'])


@api.route("/date/<string:start_date>/<string:end_date>")
@api.doc(security="apikey")
@legacy_api.route("/<token>/proposal/session/date/<start_date>/<end_date>/list")
class SessionsInfosProposalDates(Resource):
    @authentication_required
    @permission_required("any", ["own_sessions", "all_sessions"])
    def get(self, start_date, end_date, **kwargs):
        """Get all sessions between two dates that user is allowed to access.

        Args:
            start_date (str): start date
            end_date (str): end date
        """
        if "all_sessions" in request.user['permissions']:
            return session.get_session_infos_all_dates(start_date, end_date)
        return session.get_session_infos_login_dates(
            request.user['username'], start_date, end_date)


@api.route("/proposal/<proposal_id>")
@api.doc(security="apikey")
@legacy_api.route("/<token>/proposal/<proposal_id>/session/list")
class SessionsInfosProposal(Resource):
    @authentication_required
    @permission_required("any", ["own_sessions", "all_sessions"])
    def get(self, proposal_id, **kwargs):
        """Get all sessions for proposal that user is allowed to access.

        Args:
            proposal_id (str): proposal id or name
        """
        proposal_id = find_proposal_id(proposal_id)
        if "all_sessions" in request.user['permissions']:
            return session.get_session_infos_all_proposal(proposal_id)
        return session.get_session_infos_login_proposal(
            request.user['username'], proposal_id)
