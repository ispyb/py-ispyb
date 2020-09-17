# encoding: utf-8
#
#  Project: py-ispyb
#  https://github.com/ispyb/py-ispyb
#
#  This file is part of py-ispyb software.
#
#  py-ispyb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-ispyb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.

import logging

from flask import request
from flask_restx_patched import Resource, HTTPStatus

from app.extensions.api import api_v1, Namespace
from app.extensions.auth import token_required, roles_required

from ispyb_core.models import BLSession as Session
from ispyb_core.schemas import session as session_schemas
from ispyb_core.modules import session


__license__ = "LGPLv3+"

log = logging.getLogger(__name__)
api = Namespace("Sessions", description="Session related namespace", path="/sessions")
api_v1.add_namespace(api)

session_desc_f_schema = session_schemas.session_f_schema



@api.route("")
@api.doc(security="apikey")
class Sessions(Resource):
    """Allows to get all sessions and insert a new one"""

    #@token_required
    def get(self):
        """Returns list of sessions

        /ispyb/api/v1/sessions: returns all sessions
        /ispyb/api/v1/sessions?limit=10: returns first 10 sessions
        /ispyb/api/v1/sessions?offset=10: returns sessions 10..30
        (default limit defined in config.py)
        /ispyb/api/v1/sessions?offset=10&limit=10: returns 10 sessions
        starting from index 10

        Returns:
            list: list of sessions.
        """

        # TODO add decorator @paginate
        return session.get_sessions(request.args), HTTPStatus.OK

    @api.expect(session_schemas.session_f_schema)
    @api.marshal_with(session_schemas.session_f_schema, code=201)
    #@api.errorhandler(FakeException)
    #TODO add custom exception handling
    @token_required
    @roles_required(["manager", "admin"])
    def post(self):
        """Adds a new session"""
        log.info("Inserts a new session")

        #with 
        result = session.add_session(api.payload)
        if result:
            return result, HTTPStatus.OK
        else:
            return
            {"message": "Unable to add new session"},
            HTTPStatus.NOT_ACCEPTABLE     



@api.route("/<int:session_id>")
@api.param("session_id", "Session id (integer)")
@api.doc(security="apikey")
@api.response(
    code=HTTPStatus.NOT_FOUND, description="Session not found.",
)
class SessionById(Resource):
    """Allows to get/set/delete a session"""

    @api.doc(description="session_id should be an integer ")
    @api.marshal_with(session_schemas.session_f_schema, skip_none=True, code=HTTPStatus.OK)
    @token_required
    def get(self, session_id):
        """Returns a session by sessionId"""
        result = session.get_session_by_id(session_id)
        if result:
            return result, HTTPStatus.OK
        else:
            api.abort(HTTPStatus.NOT_FOUND, "Session not found")

@api.route("/<int:session_id>/info")
@api.param("session_id", "session id (integer)")
@api.doc(security="apikey")
@api.response(
    code=HTTPStatus.NOT_FOUND, description="session not found.",
)
class SessionInfoById(Resource):
    """Returns full information of a session"""

    @api.doc(description="session_id should be an integer ")
    #@api.marshal_with(session_desc_f_schema)
    @token_required
    def get(self, session_id):
        """Returns a full description of a session by sessionId"""
        result = session.get_session_info_by_id(session_id)
        if result:
            return result, HTTPStatus.OK
        else:
            api.abort(HTTPStatus.NOT_FOUND, "session not found")

