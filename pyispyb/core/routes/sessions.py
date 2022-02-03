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
from pyispyb.core.modules.proposal import findProposalId
from pyispyb.flask_restx_patched import Resource

from pyispyb.app.extensions.api import api_v1, Namespace, legacy_api
from pyispyb.app.extensions.auth.decorators import proposal_authorization_required, authentication_required, permission_required

from pyispyb.core.modules import session


__license__ = "LGPLv3+"

log = logging.getLogger(__name__)
api = Namespace(
    "Sessions", description="Session related namespace", path="/sessions")
api_v1.add_namespace(api)


@api.route("")
@legacy_api.route("/<token>/session/list")
class SessionsInfos(Resource):
    @authentication_required
    @permission_required("any", ["own_sessions", "all_sessions"])
    def get(self, **kwargs):
        """Returns list of sessions associated to user"""
        if "all_sessions" in request.user['roles']:
            return session.get_session_infos_manager()
        return session.get_session_infos_login(request.user['sub'])


@api.route("/date/<string:startDate>/<string:endDate>")
@legacy_api.route("/<token>/proposal/session/date/<startDate>/<endDate>/list")
class SessionsInfosProposalDates(Resource):
    @authentication_required
    @permission_required("any", ["own_sessions", "all_sessions"])
    def get(self, startDate, endDate, **kwargs):
        """Returns list of sessions associated to user in between the two dates"""
        if "all_sessions" in request.user['roles']:
            return session.get_session_infos_manager_dates(startDate, endDate)
        return session.get_session_infos_login_dates(request.user['sub'], startDate, endDate)


@api.route("/proposal/<int:proposal_id>")
@legacy_api.route("/<token>/proposal/<proposal_id>/session/list")
class SessionsInfosProposal(Resource):
    @authentication_required
    @permission_required("any", ["own_proposal", "all_proposals"])
    @proposal_authorization_required
    def get(self, proposal_id, **kwargs):
        """Returns list of sessions associated to user and proposal"""
        proposal_id = findProposalId(proposal_id)
        if "all_sessions" in request.user['roles']:
            return session.get_session_infos_manager_proposal(proposal_id)
        return session.get_session_infos_login_proposal(request.user['sub'], proposal_id)
