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

from marshmallow_jsonschema import JSONSchema

api = Namespace("Schemas", description="Schemas related namespace", path="/schemas")
api_v1.add_namespace(api)


@api.route("/<string:name>")
@api.param("name", "name (string)")
@api.doc(description="name should be a string")
# @token_required
class Schemas(Resource):
    def get(self, name):
        """Returns empty schema

        Args:
            name (string): schema name

        Returns:
            json: schema as json
        """
        try:
            schemas_module = importlib.import_module("app.schemas." + name)
            ma_schema = getattr(schemas_module, "ma_%s_schema" % name)
            return JSONSchema().dump(ma_schema)
        except Exception as ex:
            return "Unable to return schema with name %s (%s)" % (name, str(ex)), HTTPStatus.NOT_FOUND
