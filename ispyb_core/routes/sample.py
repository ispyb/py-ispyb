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


from flask_restx_patched import Resource, HTTPStatus

from app.extensions.api import api_v1, Namespace
from app.extensions.auth import token_required

from ispyb_core.schemas import sample as sample_schemas
from ispyb_core.schemas import crystal as crystal_schemas
from ispyb_core.modules import sample, crystal


__license__ = "LGPLv3+"


api = Namespace(
    "Samples",
    description="Sample related namespace",
    path="/samples",
)
api_v1.add_namespace(api)


@api.route("")
@api.doc(security="apikey")
class Sample(Resource):
    """Sample resource"""

    @token_required
    def get(self):
        """Returns all sample items"""
        return sample.get_sample_list()

    @token_required
    @api.expect(sample_schemas.sample_f_schema)
    @api.marshal_with(sample_schemas.sample_f_schema, code=201)
    def post(self):
        """Adds a new sample item"""
        # sample_module.(**api.payload)
        return


@api.route("/<int:sample_id>")
@api.param("sample_id", "Sample id (integer)")
@api.doc(security="apikey")
@api.response(
    code=HTTPStatus.NOT_FOUND,
    description="Sample not found.",
)
class SampleById(Resource):
    """Allows to get/set/delete a sample item"""

    @api.doc(description="sample_id should be an integer ")
    @api.marshal_with(
        sample_schemas.sample_f_schema, skip_none=True, code=HTTPStatus.OK
    )
    # @token_required
    def get(self, sample_id):
        """Returns a sample by sampleId"""
        result = sample.get_sample_by_id(sample_id)
        if result:
            return result, HTTPStatus.OK
        else:
            api.abort(HTTPStatus.NOT_FOUND, "Sample with id %d not found" % sample_id)


@api.route("/crystals")
@api.doc(security="apikey")
class Crystal(Resource):
    """Crystal resource"""

    # @token_required
    def get(self):
        """Returns all crystal items"""
        return crystal.get_crystal_list()

    # @token_required
    @api.expect(crystal_schemas.crystal_f_schema)
    @api.marshal_with(crystal_schemas.crystal_f_schema, code=201)
    def post(self):
        """Adds a new crystal item"""
        # sample_module.(**api.payload)
        return


@api.route("/crystals/<int:crystal_id>")
@api.param("crystal_id", "Crystal id (integer)")
@api.doc(security="apikey")
@api.response(
    code=HTTPStatus.NOT_FOUND,
    description="Crystal not found.",
)
class CrystalById(Resource):
    """Allows to get/set/delete a crystal item"""

    @api.doc(description="crystal_id should be an integer ")
    @api.marshal_with(
        crystal_schemas.crystal_f_schema, skip_none=True, code=HTTPStatus.OK
    )
    # @token_required
    def get(self, crystal_id):
        """Returns a crystal by crystalId"""
        result = crystal.get_crystal_by_id(crystal_id)
        if result:
            return result, HTTPStatus.OK
        else:
            api.abort(
                HTTPStatus.NOT_FOUND, "Crystal with id %s not found" % str(crystal_id)
            )
