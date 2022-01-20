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
from datetime import datetime

from flask import request
from pyispyb.flask_restx_patched import Resource, HTTPStatus, abort

from pyispyb.app.extensions.api import api_v1, Namespace, legacy_api
from pyispyb.app.extensions.auth.decorators import proposal_authorization_required, session_authorization_required, authentication_required, permission_required

from pyispyb.core.schemas import session as session_schemas
from pyispyb.core.modules import session


__license__ = "LGPLv3+"

log = logging.getLogger(__name__)
api = Namespace(
    "Sessions", description="Session related namespace", path="/sessions")
api_v1.add_namespace(api)


@api.route("", endpoint="sessions")
@api.doc(security="apikey")
class Sessions(Resource):
    @authentication_required
    @permission_required
    def get(self):
        """Returns list of sessions"""
        # TODO implement authorization
        return session.get_sessions(request)

    @authentication_required
    @permission_required
    @api.expect(session_schemas.f_schema)
    @api.marshal_with(session_schemas.f_schema, code=201)
    def post(self):
        """Adds a new session"""
        log.info("Inserts a new session")
        # TODO implement authorization
        return session.add_session(api.payload)


@api.route("/infos", endpoint="sessions_infos")
@legacy_api.route("/<token>/session/list")
@api.doc(security="apikey")
class SessionsInfos(Resource):
    @authentication_required
    @permission_required
    def get(self, **kwargs):
        """Returns list of sessions"""
        return session.get_session_infos_login(request.user['sub'])


@api.route("/proposal/<int:proposal_id>/infos", endpoint="sessions_infos_proposal")
@legacy_api.route("/<token>/proposal/<proposal_id>/session/list")
@api.doc(security="apikey")
class SessionsInfosProposal(Resource):
    @authentication_required
    @permission_required
    @proposal_authorization_required
    def get(self, proposal_id, **kwargs):
        """Returns list of sessions"""
        return session.get_session_infos_login_proposal(request.user['sub'], proposal_id)


@api.route("/<int:session_id>", endpoint="session_by_id")
@api.param("session_id", "Session id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.FOUND, description="Session found :)", model=session_schemas.f_schema)
@api.response(code=HTTPStatus.NOT_FOUND, description="Session not found :(")
class SessionById(Resource):
    """Allows to get/set/delete a session"""

    @authentication_required
    @permission_required
    @session_authorization_required
    @api.doc(description="session_id should be an integer ")
    @api.marshal_with(session_schemas.f_schema, skip_none=True, code=HTTPStatus.OK)
    def get(self, session_id):
        """Returns a session by sessionId"""
        return session.get_session_by_id(session_id)

    @authentication_required
    @permission_required
    @session_authorization_required
    @api.expect(session_schemas.f_schema)
    @api.marshal_with(session_schemas.f_schema, code=HTTPStatus.CREATED)
    def put(self, session_id):
        """Fully updates session with session_id"""
        return session.update_session(session_id, api.payload)

    @authentication_required
    @permission_required
    @session_authorization_required
    @api.expect(session_schemas.f_schema)
    @api.marshal_with(session_schemas.f_schema, code=HTTPStatus.CREATED)
    def patch(self, session_id):
        """Partially updates session with id sessionId"""
        return session.patch_session(session_id, api.payload)

    @authentication_required
    @permission_required
    @session_authorization_required
    def delete(self, session_id):
        """Deletes a session by sessionId"""
        return session.delete_session(session_id)


@api.route("/date", endpoint="sessions_by_date")
@api.doc(security="apikey")
class SessionsByDateBeamline(Resource):
    """Allows to get all sessions by date and beamline"""

    @authentication_required
    @permission_required
    def get(self):
        """Returns list of sessions by start_date, end_date and beamline."""
        # TODO implement authorization
        query_dict = request.args.to_dict()
        start_date = query_dict.get("start_date")
        end_date = query_dict.get("end_date")
        beamline = query_dict.get("beamline")

        if start_date is None and end_date is None:
            abort(
                HTTPStatus.NOT_ACCEPTABLE, "No start_date or end_date argument provided"
            )

        if start_date:
            try:
                start_date = datetime.strptime(start_date, "%Y%m%d")
            except ValueError as ex:
                abort(
                    HTTPStatus.NOT_ACCEPTABLE,
                    "start_date should be in YYYYMMDD format (%s)" % str(ex),
                )

        if end_date:
            try:
                end_date = datetime.strptime(end_date, "%Y%m%d")
            except ValueError as ex:
                abort(
                    HTTPStatus.NOT_ACCEPTABLE,
                    "end_date should be in YYYYMMDD format (%s)" % str(ex),
                )

        return session.get_sessions_by_date(start_date, end_date, beamline)
