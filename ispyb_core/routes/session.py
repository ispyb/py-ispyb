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


from flask_restx_patched import Resource, HTTPStatus

from app.extensions.api import api_v1, Namespace
from app.extensions.auth import token_required

from ispyb_core.modules import session


__license__ = "LGPLv3+"


api = Namespace("Sessions", description="Session related namespace", path="/sessions")
api_v1.add_namespace(api)


@api.route("")
class Sessions(Resource):
    @api.doc(security="apikey")
    def get(self):
        return session.get_all_sessions()


@api.route("<int:proposal_id>")
@api.param("proposal_id", "Proposal id (integer)")
@api.doc(description="proposal_id should be an integer ")
# @token_required
class SessionsByProposalList(Resource):
    def get(self, proposal_id):
        """Returns all proposal shippings"""
        return session.get_proposal_sessions(proposal_id)
