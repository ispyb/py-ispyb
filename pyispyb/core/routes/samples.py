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

from flask import request
from pyispyb.flask_restx_patched import Resource, HTTPStatus

from pyispyb.app.extensions.api import api_v1, Namespace
from pyispyb.app.extensions.auth import token_required, authorization_required

from pyispyb.core.schemas import sample as sample_schemas
from pyispyb.core.schemas import crystal as crystal_schemas
from pyispyb.core.schemas import protein as protein_schemas
from pyispyb.core.schemas import diffraction_plan as diffraction_plan_schemas
from pyispyb.core.modules import sample, crystal, diffraction_plan, protein


__license__ = "LGPLv3+"


api = Namespace("Samples", description="Sample related namespace", path="/samples")
api_v1.add_namespace(api)


@api.route("", endpoint="samples")
@api.doc(security="apikey")
class Sample(Resource):
    """Sample resource"""

    @token_required
    @authorization_required
    def get(self):
        """Returns all sample items"""
        return sample.get_samples(request)

    @token_required
    @api.expect(sample_schemas.f_schema)
    @api.marshal_with(sample_schemas.f_schema, code=201)
    def post(self):
        """Adds a new sample item"""
        return sample.add_sample(api.payload)


@api.route("/<int:sample_id>", endpoint="sample_by_id")
@api.param("sample_id", "Sample id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="Sample not found.")
class SampleById(Resource):
    """Allows to get/set/delete a sample item"""

    @api.doc(description="sample_id should be an integer ")
    @api.marshal_with(sample_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    @token_required
    @authorization_required
    def get(self, sample_id):
        """Returns a sample by sampleId"""
        return sample.get_sample_by_id(sample_id)

    @api.expect(sample_schemas.f_schema)
    @api.marshal_with(sample_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def put(self, sample_id):
        """Fully updates sample with sample_id"""
        return sample.update_sample(sample_id, api.payload)

    @api.expect(sample_schemas.f_schema)
    @api.marshal_with(sample_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, sample_id):
        """Partially updates sample with id sampleId"""
        return sample.patch_sample(sample_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, sample_id):
        """Deletes a sample by sampleId"""
        return sample.delete_sample(sample_id)


@api.route("/crystals", endpoint="crystals")
@api.doc(security="apikey")
class Crystals(Resource):
    """Crystal resource"""

    @token_required
    @authorization_required
    def get(self):
        """Returns all crystal items"""
        return crystal.get_crystals(request)

    @api.expect(crystal_schemas.f_schema)
    @api.marshal_with(crystal_schemas.f_schema, code=201)
    @token_required
    @authorization_required
    def post(self):
        """Adds a new crystal item"""
        return crystal.add_crystal(api.payload)


@api.route("/crystals/<int:crystal_id>", endpoint="crystal_by_id")
@api.param("crystal_id", "Crystal id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="Crystal not found.")
class CrystalById(Resource):
    """Allows to get/set/delete a crystal item"""

    @api.doc(description="crystal_id should be an integer ")
    @api.marshal_with(crystal_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    @token_required
    @authorization_required
    def get(self, crystal_id):
        """Returns a crystal by crystalId"""
        return crystal.get_crystal_by_id(crystal_id)

    @api.expect(crystal_schemas.f_schema)
    @api.marshal_with(crystal_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def put(self, crystal_id):
        """Fully updates crystal with crystal_id"""
        return crystal.update_crystal(crystal_id, api.payload)

    @api.expect(crystal_schemas.f_schema)
    @api.marshal_with(crystal_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, crystal_id):
        """Partially updates crystal with id crystalId"""
        return crystal.patch_crystal(crystal_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, crystal_id):
        """Deletes a crystal by crystalId"""
        return crystal.delete_crystal(crystal_id)


@api.route("/proteins", endpoint="proteins")
@api.doc(security="apikey")
class Proteins(Resource):
    """Proteins resource"""

    @token_required
    @authorization_required
    def get(self):
        """Returns all protein items"""
        return protein.get_proteins(request)

    @api.expect(protein_schemas.f_schema)
    @api.marshal_with(protein_schemas.f_schema, code=201)
    @token_required
    @authorization_required
    def post(self):
        """Adds a new protein item"""
        return protein.add_protein(api.payload)


@api.route("/proteins/<int:protein_id>", endpoint="protein_by_id")
@api.param("protein_id", "protein id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="protein not found.")
class ProteinById(Resource):
    """Allows to get/set/delete a protein"""

    @api.doc(description="protein_id should be an integer ")
    @api.marshal_with(protein_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    @token_required
    @authorization_required
    def get(self, protein_id):
        """Returns a protein by proteinId"""
        return protein.get_protein_by_id(protein_id)

    @api.expect(protein_schemas.f_schema)
    @api.marshal_with(protein_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def put(self, protein_id):
        """Fully updates protein with proteinId"""
        return protein.update_protein(protein_id, api.payload)

    @api.expect(protein_schemas.f_schema)
    @api.marshal_with(protein_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, protein_id):
        """Partially updates protein with proteinId"""
        return protein.patch_protein(protein_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, protein_id):
        """Deletes a protein by proteinId"""
        return protein.delete_protein(protein_id)


@api.route("/diffraction_plans", endpoint="diffraction_plans")
@api.doc(security="apikey")
class DiffractionPlans(Resource):
    """Allows to get all diffraction_plans and insert a new one"""

    @token_required
    @authorization_required
    def get(self):
        """Returns list of diffraction_plans"""
        return diffraction_plan.get_diffraction_plans(request)

    @api.expect(diffraction_plan_schemas.f_schema)
    @api.marshal_with(diffraction_plan_schemas.f_schema, code=201)
    @token_required
    @authorization_required
    def post(self):
        """Adds a new diffraction_plan"""
        return diffraction_plan.add_diffraction_plan(api.payload)


@api.route(
    "/diffraction_plans/<int:diffraction_plan_id>", endpoint="diffraction_plan_by_id"
)
@api.param("diffraction_plan_id", "diffraction_plan id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="diffraction_plan not found.")
class DiffractionPlanById(Resource):
    """Allows to get/set/delete a diffraction_plan"""

    @api.doc(description="diffraction_plan_id should be an integer ")
    @api.marshal_with(
        diffraction_plan_schemas.f_schema, skip_none=False, code=HTTPStatus.OK
    )
    @token_required
    @authorization_required
    def get(self, diffraction_plan_id):
        """Returns a diffraction_plan by diffraction_planId"""
        return diffraction_plan.get_diffraction_plan_by_id(diffraction_plan_id)

    @api.expect(diffraction_plan_schemas.f_schema)
    @api.marshal_with(diffraction_plan_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def put(self, diffraction_plan_id):
        """Fully updates diffraction_plan with diffraction_plan_id"""
        return diffraction_plan.update_diffraction_plan(
            diffraction_plan_id, api.payload
        )

    @api.expect(diffraction_plan_schemas.f_schema)
    @api.marshal_with(diffraction_plan_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, diffraction_plan_id):
        """Partially updates diffraction_plan with id diffraction_planId"""
        return diffraction_plan.patch_diffraction_plan(diffraction_plan_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, diffraction_plan_id):
        """Deletes a diffraction_plan by diffraction_planId"""
        return diffraction_plan.delete_diffraction_plan(diffraction_plan_id)
