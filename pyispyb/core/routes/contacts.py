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

from pyispyb.core.schemas import person as person_schemas
from pyispyb.core.schemas import lab_contact as lab_contact_schemas
from pyispyb.core.schemas import laboratory as laboratory_schemas
from pyispyb.core.modules import contacts


__license__ = "LGPLv3+"


api = Namespace("Contacts", description="Contact related namespace", path="/contacts")
api_v1.add_namespace(api)


@api.route("/persons", endpoint="persons")
@api.doc(security="apikey")
class Persons(Resource):
    """Allows to get all persons"""

    @token_required
    @authorization_required
    def get(self):
        """Returns all persons"""
        return contacts.get_persons(request)

    @api.expect(person_schemas.f_schema)
    @api.marshal_with(person_schemas.f_schema, code=201)
    @token_required
    @authorization_required
    def post(self):
        return contacts.add_person(api.payload)


@api.route("/persons/<int:person_id>", endpoint="person_by_id")
@api.doc(security="apikey")
class PersonById(Resource):
    """Allows to get/set/delete a person"""

    @api.doc(description="person_id should be an integer ")
    @api.marshal_with(person_schemas.f_schema)
    @token_required
    @authorization_required
    def get(self, person_id):
        """Returns a person by personId"""
        params = {"personId": person_id}
        return contacts.get_person_by_params(params)

    @api.expect(person_schemas.f_schema)
    @api.marshal_with(person_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def put(self, person_id):
        """Fully updates person with id person_id"""
        return contacts.update_person(person_id, api.payload)

    @api.expect(person_schemas.f_schema)
    @api.marshal_with(person_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, person_id):
        """Partially updates person with id person_id"""
        return contacts.patch_person(person_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, person_id):
        """Deletes person by person_id"""
        return contacts.delete_person(person_id)


@api.route("/lab_contacts", endpoint="lab_contacts")
@api.doc(security="apikey")
class LabContacts(Resource):
    """Allows to get all local contacts"""

    @token_required
    @authorization_required
    def get(self):
        """Returns list of local contacts."""
        return contacts.get_lab_contacts(request), HTTPStatus.OK

    @api.expect(lab_contact_schemas.f_schema)
    @api.marshal_with(lab_contact_schemas.f_schema, code=201)
    @token_required
    @authorization_required
    def post(self):
        """Adds a new lab contact"""
        return contacts.add_lab_contact(api.payload)


@api.route("/lab_contacts/<int:lab_contact_id>", endpoint="lab_contact_by_id")
@api.doc(security="apikey")
class LabContactById(Resource):
    """Allows to get/set/delete a lab_contact"""

    @api.doc(description="lab_contact_id should be an integer ")
    @api.marshal_with(lab_contact_schemas.f_schema)
    @token_required
    @authorization_required
    def get(self, lab_contact_id):
        """Returns a lab contact by lab_contact_id"""
        params = {"labContactId": lab_contact_id}
        return contacts.get_lab_contact_by_params(params)

    @api.expect(lab_contact_schemas.f_schema)
    @api.marshal_with(lab_contact_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def put(self, lab_contact_id):
        """Fully updates person with id lab_contact_id"""
        return contacts.update_lab_contact(lab_contact_id, api.payload)

    @api.expect(lab_contact_schemas.f_schema)
    @api.marshal_with(lab_contact_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, lab_contact_id):
        """Partially updates person with id lab_contact_id"""
        return contacts.patch_lab_contact(lab_contact_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, lab_contact_id):
        """Deletes lab contact by lab_contact_id"""
        return contacts.delete_lab_contact(lab_contact_id)


@api.route("/labs", endpoint="labs")
@api.doc(security="apikey")
class Laboratories(Resource):

    """Allows to get all laboratory items"""

    @token_required
    @authorization_required
    def get(self):
        """Returns all laboratory entries."""
        return contacts.get_laboratories(request)

    @api.expect(laboratory_schemas.f_schema)
    @api.marshal_with(laboratory_schemas.f_schema, code=201)
    @token_required
    @authorization_required
    def post(self):
        """Adds a new laboratory"""
        return contacts.add_laboratory(api.payload)


@api.route("/labs/<int:laboratory_id>", endpoint="laboratory_by_id")
@api.param("laboratory_id", "laboratory_id id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="Laboratory not found.")
class LaboratoryById(Resource):

    """Allows to get/set/delete a laboratory item"""

    @api.doc(description="lab_id should be an integer ")
    @api.marshal_with(laboratory_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    @token_required
    @authorization_required
    def get(self, laboratory_id):
        """Returns a laboratory by laboratoryId"""
        return contacts.get_laboratory_by_id(laboratory_id)

    @api.expect(laboratory_schemas.f_schema)
    @api.marshal_with(laboratory_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def put(self, laboratory_id):
        """Fully updates laboratory with id laboratory_id."""
        return contacts.update_laboratory(laboratory_id, api.payload)

    @api.expect(laboratory_schemas.f_schema)
    @api.marshal_with(laboratory_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, laboratory_id):
        """Partially updates laboratory with id laboratory_id."""
        return contacts.patch_laboratory(laboratory_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, laboratory_id):
        """Deletes laboratory by laboratory_id."""
        return contacts.delete_laboratory(laboratory_id)
