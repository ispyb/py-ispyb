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


import importlib

from flask_restx_patched import Resource, HTTPStatus
from app.extensions.api import api_v1, Namespace
from app.extensions.auth import token_required
from app import schemas

api = Namespace("Schemas", description="Schemas related namespace", path="/schemas")
api_v1.add_namespace(api)


@api.route("/available_names")
class SchemasList(Resource):

    #@token_required
    def get(self):
        """Returns list of available schemas

        Returns:
            list: list of names
        """

        #TODO I guess there is oneliner fancy code that can do this...
        result = []
        for item in dir(schemas):
            if not item.startswith('__'):
                result.append(item)

        return result


@api.route("/<string:name>")
@api.param("name", "name (string)")
@api.doc(description="name should be a string")
class Schemas(Resource):

    #@token_required
    def get(self, name):
        """Returns json schema

        Args:
            name (string): schema name

        Returns:
            json: schema as json
        """
        try:
            schemas_module = importlib.import_module("app.schemas." + name)
            return getattr(schemas_module, "%s_json_schema" % name) 
        except Exception as ex:
            return "Unable to return schema with name %s (%s)" % (name, str(ex)), HTTPStatus.NOT_FOUND
