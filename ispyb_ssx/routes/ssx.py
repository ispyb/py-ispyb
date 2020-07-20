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

"""

Example routes:

"""

import logging
from flask import request, current_app
from flask_restx._http import HTTPStatus

from flask_restx_patched import Resource

#from app.extensions import db
from app.extensions.api import api_v1, Namespace
from app.extensions.auth import token_required, write_permission_required

#from ispyb_core.models import Proposal
#from ispyb_core.schemas import proposal as proposal_schemas
#from ispyb_core.modules import proposal
from ispyb_service_connector import get_ispyb_resource


__license__ = "LGPLv3+"


log = logging.getLogger(__name__)
api = Namespace("SSX", description="SSX related namespace", path="/main")
api_v1.add_namespace(api)


@api.route("")
@api.doc(security="apikey")
class SSX(Resource):
    """Allows to get all proposals"""

    #@api.marshal_list_with(proposal_schemas.proposal_f_schema, skip_none=True, code=HTTPStatus.OK)
    #TODO Define model with JSON Schema 
    #@token_required
    def get(self):
        """Returns...

        Returns:
            list: list of ssx slury crystals.
        """
        

        # TODO add decorator @paginate
        return get_ispyb_resource("ispyb_core", "schemas/available_names")