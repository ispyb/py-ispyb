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


import importlib

from flask import current_app
from pyispyb.flask_restx_patched import Resource, HTTPStatus
from pyispyb.app.extensions.api import api_v1, Namespace
# from pyispyb.app.extensions.auth import token_required
from pyispyb.core import schemas


__license__ = "LGPLv3+"


api = Namespace("Schemas", description="Schemas related namespace", path="/schemas")
api_v1.add_namespace(api)


@api.route("/available_names", endpoint="available_schemas_names")
class SchemasList(Resource):

    # @token_required
    def get(self):
        """Returns list of available schemas

        Returns:
            list: list of names
        """
        current_app.logger.info("Get all schemas")
        # TODO I guess there is oneliner fancy code that can do this...
        result = []
        for item in dir(schemas):
            if not item.startswith("__"):
                result.append(item)

        return result


@api.route("/<string:name>", endpoint="schema_by_name")
@api.param("name", "name (string)")
@api.doc(description="name should be a string")
class Schemas(Resource):

    # @token_required
    def get(self, name):
        """Returns json schema

        Args:
            name (string): schema name

        Returns:
            json: schema as json
        """
        try:
            schemas_module = importlib.import_module("pyispyb.core.schemas." + name)
            return getattr(schemas_module, "json_schema")
        except Exception as ex:
            return (
                "Unable to return schema with name %s (%s)" % (name, str(ex)),
                HTTPStatus.NOT_FOUND,
            )
