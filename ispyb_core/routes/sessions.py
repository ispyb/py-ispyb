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
from datetime import datetime

from flask import request
from flask_restx_patched import Resource, HTTPStatus, abort

from app.extensions.api import api_v1, Namespace
from app.extensions.auth import token_required, authorization_required

from ispyb_core.schemas import session as session_schemas
from ispyb_core.modules import session


__license__ = "LGPLv3+"

log = logging.getLogger(__name__)
api = Namespace("Sessions", description="Session related namespace", path="/sessions")
api_v1.add_namespace(api)


@api.route("", endpoint="sessions")
@api.doc(security="apikey")
class Sessions(Resource):
    """Allows to get all sessions and insert a new one"""

    @token_required
    @authorization_required
    def get(self):
        """Returns list of sessions"""
        return session.get_sessions(request)

    @api.expect(session_schemas.f_schema)
    @api.marshal_with(session_schemas.f_schema, code=201)
    # @api.errorhandler(FakeException)
    # TODO add custom exception handling
    @token_required
    @authorization_required
    def post(self):
        """Adds a new session"""
        log.info("Inserts a new session")

        return session.add_session(api.payload)


@api.route("/<int:session_id>", endpoint="session_by_id")
@api.param("session_id", "Session id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="Session not found.")
class SessionById(Resource):
    """Allows to get/set/delete a session"""

    @api.doc(description="session_id should be an integer ")
    @api.marshal_with(session_schemas.f_schema, skip_none=True, code=HTTPStatus.OK)
    @token_required
    @authorization_required
    def get(self, session_id):
        """Returns a session by sessionId"""
        return session.get_session_by_id(session_id)


@api.route("/<int:session_id>/info", endpoint="session_info_by_id")
@api.param("session_id", "session id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="session not found.")
class SessionInfoById(Resource):
    """Returns full information of a session"""

    @api.doc(description="session_id should be an integer ")
    # @api.marshal_with(session_desc_f_schema)
    @token_required
    @authorization_required
    def get(self, session_id):
        """Returns a full description of a session by sessionId"""
        return session.get_session_info_by_id(session_id)


@api.route("/date", endpoint="sessions_by_date")
@api.doc(security="apikey")
class SessionsByDateBeamline(Resource):
    """Allows to get all sessions by date and beamline"""

    @token_required
    @authorization_required
    def get(self):
        """Returns list of sessions by start_date, end_date and beamline.

        Returns:
            list: list of sessions.
        """

        query_params = request.args.to_dict()
        start_date = query_params.get("start_date")
        end_date = query_params.get("end_date")
        beamline = query_params.get("beamline")

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


# getSessionsByDate(startDate, endDate)
# getSessionsByDateAndBeamline(startDate, endDate, beamline)
# getSessionsByProposalAndDate(startDate, endDate, proposal)
