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

from flask import request
from flask_restx_patched import Resource, HTTPStatus

from app.extensions.api import api_v1, Namespace
from app.extensions.auth import token_required, roles_required

from ispyb_core.schemas import person as person_schemas
from ispyb_core.schemas import lab_contact as lab_contact_schemas
from ispyb_core.modules import contacts


__license__ = "LGPLv3+"


api = Namespace("Contacts", description="Contact related namespace", path="/contacts")
api_v1.add_namespace(api)


@api.route("/persons")
class Persons(Resource):
    """Allows to get all persons"""

    @api.doc(security="apikey")
    @token_required
    def get(self):
        """Returns all persons"""
        # app.logger.info("Return all person")
        return contacts.get_persons(request.args)

    @api.expect(person_schemas.person_f_schema)
    @api.marshal_with(person_schemas.person_f_schema, code=201)
    @roles_required(["manager", "admin"])
    def post(self):
        return


@api.route("/person/<int:person_id>")
class Person(Resource):
    """Allows to get/set/delete a person"""

    @api.doc(description="person_id should be an integer ")
    @api.marshal_with(person_schemas.person_f_schema)
    @token_required
    def get(self, person_id):
        """Returns a person by personId"""
        params = {"personId" : person_id}
        return contacts.get_person_by_params(params)

@api.route("/lab_contacts")
@api.doc(security="apikey")
class LabContacts(Resource):
    """Allows to get all local contacts"""

    @token_required
    def get(self):
        """Returns list of local contacts

        Returns:
            list: list of local contacts.
        """
        return contacts.get_lab_contacts(request.args), HTTPStatus.OK

    @api.expect(lab_contact_schemas.lab_contact_f_schema)
    @api.marshal_with(lab_contact_schemas.lab_contact_f_schema, code=201)
    # @api.errorhandler(FakeException)
    # TODO add custom exception handling
    @token_required
    @roles_required(["manager", "admin"])
    def post(self):
        """Adds a new lab contact"""
        result = contacts.add_lab_contact(api.payload)
        if result:
            return result, HTTPStatus.OK
        else:
            return
            {"message": "Unable to add new lab contact"},
            HTTPStatus.NOT_ACCEPTABLE
