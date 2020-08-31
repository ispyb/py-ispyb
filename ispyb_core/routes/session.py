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
from app.extensions.auth import token_required, write_permission_required

from ispyb_core.models import BLSession as Session
from ispyb_core.schemas import session as session_schemas
from ispyb_core.modules import session


__license__ = "LGPLv3+"

log = logging.getLogger(__name__)
api = Namespace("Session", description="Session related namespace", path="/session")
api_v1.add_namespace(api)

@api.route("")
@api.doc(security="apikey")
class Sessions(Resource):
    """Allows to get all sessions and insert a new one"""

    #@api.marshal_list_with(_schemas.session_f_schema, skip_none=True, code=HTTPStatus.OK)
    #TODO Define model with JSON Schema 
    @token_required
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
        offset = request.args.get("offset", type=int)
        limit = request.args.get("limit", type=int)

        # TODO add decorator @paginate
        return session.get_sessions(offset, limit), HTTPStatus.OK

    @api.expect(session_schemas.session_f_schema)
    @api.marshal_with(session_schemas.session_f_schema, code=201)
    #@api.errorhandler(FakeException)
    #TODO add custom exception handling
    @token_required
    @write_permission_required
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


@api.route("/params")
@api.doc(security="apikey")
class SessionssByParams(Resource):
    """Allows to get sessions by query parametes"""

    @api.marshal_with(session_schemas.session_f_schema)
    @token_required
    def get(self):
        """Returns sessions by query parameters"""
        return session.get_sessions_by_params(request.args)


