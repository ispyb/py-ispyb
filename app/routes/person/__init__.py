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


__license__ = "LGPLv3+"


from flask_restx import Namespace, Resource

from app.extensions import db
from app.extensions.api import api_v1
from app.modules import person

api = Namespace("Person", description="Person", path="/person")
api_v1.add_namespace(api)


@api.route("")
class PersonList(Resource):
    """Allows to get all persons"""

    @api.doc(security="apikey")
    # @token_required
    def get(self):
        """Returns all persons"""
        # app.logger.info("Return all person")
        return person.get_all_persons()

    @api.expect(person.schemas.f_person_schema)
    @api.marshal_with(person.schemas.f_person_schema, code=201)
    def post(self):
        return


@api.route("/<int:person_id>")
class Person(Resource):
    """Allows to get/set/delete a person"""

    @api.doc(description="person_id should be an integer ")
    @api.marshal_with(person.schemas.f_person_schema)
    # @token_required
    def get(self, person_id):
        """Returns a person by personId"""
        return person.get_person_by_id(person_id)

    """
    #@ns.doc(parser=parser)
    @ns.expect(f_proposal_schema)
    def post(self, prop_id):
        json_data = request.form['data']
        print(json_data)
        data = ma_proposal_schema.load(json_data)

    """
