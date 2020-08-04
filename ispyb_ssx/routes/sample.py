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

# from app.extensions import db
from app.extensions.api import api_v1, Namespace
from app.extensions.auth import token_required, write_permission_required

from ispyb_ssx.schemas import loaded_sample as loaded_sample_schemas
from ispyb_ssx.schemas import crystal_slurry as crystal_slurry_schemas
from ispyb_ssx.modules import loaded_sample

from ispyb_service_connector import get_ispyb_resource


__license__ = "LGPLv3+"


log = logging.getLogger(__name__)
api = Namespace("Sample", description="Sample related namespace", path="/sample")
api_v1.add_namespace(api)


@api.route("")
@api.doc(security="apikey")
class LoadedSample(Resource):
    """Loaded sample resource"""

    # @token_required
    def get(self):
        """Returns all loaded samples"""
        # app.logger.info("Return all data collections")
        return loaded_sample.get_all_loaded_samples()

    # @token_required
    @api.expect(loaded_sample_schemas.loaded_sample_f_schema)
    @api.marshal_with(loaded_sample_schemas.loaded_sample_f_schema, code=201)
    def post(self):
        """Adds a new loaded sample"""
        # app.logger.info("Insert new data collection")
        loaded_sample.add_loaded_sample(api.payload)


@api.route("/crystal_slurry")
@api.doc(security="apikey")
class CrystalSlurry(Resource):
    """Crystal slurry resource"""

    # @token_required
    def get(self):
        """Returns all crystal slurry"""
        # app.logger.info("Return all data collections")
        return loaded_sample.get_all_crystal_slurry()

    # @token_required
    @api.expect(crystal_slurry_schemas.crystal_slurry_f_schema)
    # @api.marshal_with(crystal_slurry_schemas.crystal_slurry_f_schema, code=201)
    def post(self):
        """Adds a new crystal slury"""
        status_code, result = loaded_sample.add_crystal_slurry(api.payload)
        if status_code >= 400:
            api.abort(HTTPStatus.NOT_ACCEPTABLE, result)
        # return status_code, result


# return get_ispyb_resource("ispyb_core", "schemas/available_names")
