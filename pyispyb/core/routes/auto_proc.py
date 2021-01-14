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

from pyispyb.core.schemas import auto_proc as auto_proc_schemas
from pyispyb.core.schemas import auto_proc_program as auto_proc_program_schemas
from pyispyb.core.schemas import (
    auto_proc_program_attachment as auto_proc_program_attachment_schemas,
)
#from pyispyb.core.schemas import (
#    auto_proc_program_message as auto_proc_program_message_schemas,
#)
from pyispyb.core.schemas import auto_proc_status as auto_proc_status_schemas
from pyispyb.core.modules import auto_proc


__license__ = "LGPLv3+"


api = Namespace(
    "Auto processing", description="Auto processing related namespace", path="/autoproc"
)

api_v1.add_namespace(api)


@api.route("", endpoint="auto_procs")
@api.doc(security="apikey")
class AutoProcs(Resource):
    """Allows to get all auto proc entries"""

    @token_required
    @authorization_required
    def get(self):
        """Returns auto proc entries"""
        return auto_proc.get_auto_procs(request)

    @api.expect(auto_proc_schemas.f_schema)
    @api.marshal_with(auto_proc_schemas.f_schema, code=201)
    # @api.errorhandler(FakeException)
    # TODO add custom exception handling
    @token_required
    @authorization_required
    def post(self):
        """Adds a new auto proc"""
        return auto_proc.add_auto_proc(api.payload)


@api.route("/<int:auto_proc_id>", endpoint="auto_proc_by_id")
@api.param("auto_proc_id", "auto_proc id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="auto_proc not found.")
class AutoProcById(Resource):

    """Allows to get/set/delete a auto_proc"""

    @api.doc(description="auto_proc_id should be an integer ")
    @api.marshal_with(auto_proc_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    @token_required
    @authorization_required
    def get(self, auto_proc_id):
        """Returns a auto_proc by auto_procId"""
        return auto_proc.get_auto_proc_by_id(auto_proc_id)


@api.route("/status", endpoint="auto_proc_status")
@api.doc(security="apikey")
class AutoProcStatus(Resource):
    """Allows to get all auto proc status entries"""

    @token_required
    @authorization_required
    def get(self):
        """Returns all auto_proc_status entries"""
        return auto_proc.get_auto_proc_status(request)

    @api.expect(auto_proc_program_schemas.f_schema)
    @api.marshal_with(auto_proc_program_schemas.f_schema, code=201)
    # @api.errorhandler(FakeException)
    # TODO add custom exception handling
    @token_required
    @authorization_required
    def post(self):
        """Adds a new auto proc program"""
        return auto_proc.add_auto_proc_status(api.payload)


@api.route("/status/<int:status_id>", endpoint="auto_proc_status_by_id")
@api.param("status_id", "status id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="auto_proc_status not found.")
class AutoProcStatusById(Resource):

    """Allows to get/set/delete a auto_proc_status"""

    @api.doc(description="status_id should be an integer ")
    @api.marshal_with(
        auto_proc_status_schemas.f_schema, skip_none=False, code=HTTPStatus.OK
    )
    @token_required
    @authorization_required
    def get(self, status_id):
        """Returns a auto_proc by auto_procId"""
        return auto_proc.get_auto_proc_status_by_id(status_id)


@api.route("/programs", endpoint="auto_proc_programs")
@api.doc(security="apikey")
class AutoProcPrograms(Resource):
    """Allows to get all auto proc program entries"""

    @token_required
    @authorization_required
    def get(self):
        """Returns all auto_proc_program entries"""
        return auto_proc.get_auto_proc_programs(request)

    @api.expect(auto_proc_program_schemas.f_schema)
    @api.marshal_with(auto_proc_program_schemas.f_schema, code=201)
    @token_required
    @authorization_required
    def post(self):
        """Adds a new auto proc program"""

        return auto_proc.add_auto_proc_program(api.payload)


@api.route("/programs/<int:program_id>", endpoint="program_by_id")
@api.param("program_id", "program id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="auto_proc_program not found.")
class AutoProcProgramById(Resource):

    """Allows to get/set/delete a auto_proc_program"""

    @api.doc(description="program_id should be an integer ")
    @api.marshal_with(
        auto_proc_program_schemas.f_schema, skip_none=False, code=HTTPStatus.OK
    )
    @token_required
    @authorization_required
    def get(self, program_id):
        """Returns a auto_proc by auto_procId"""
        return auto_proc.get_auto_proc_program_by_id(program_id)


@api.route("/programs/attachments", endpoint="auto_proc_program_attachments")
@api.doc(security="apikey")
class AutoProcProgramAttachments(Resource):
    """Allows to get all auto proc program attachment entries"""

    @token_required
    @authorization_required
    def get(self):
        """Returns all auto_proc_program attachemnt entries"""
        return auto_proc.get_auto_proc_program_attachments(request)

    @api.expect(auto_proc_program_attachment_schemas.f_schema)
    @api.marshal_with(auto_proc_program_attachment_schemas.f_schema, code=201)
    @token_required
    @authorization_required
    def post(self):
        """Adds a new auto proc program"""
        return auto_proc.add_auto_proc_program_attachment(api.payload)


@api.route("/programs/attachments/<int:attachment_id>", endpoint="attachment_by_id")
@api.param("attachment_id", "attachment id (integer)")
@api.doc(security="apikey")
@api.response(
    code=HTTPStatus.NOT_FOUND, description="auto_proc_program_attachment not found."
)
class AutoProcProgramAttachmentById(Resource):

    """Allows to get/set/delete a auto_proc_program"""

    @api.doc(description="attachment_id should be an integer ")
    @api.marshal_with(
        auto_proc_program_attachment_schemas.f_schema,
        skip_none=False,
        code=HTTPStatus.OK,
    )
    @token_required
    @authorization_required
    def get(self, attachment_id):
        """Returns a auto_proc by attachment_id"""
        return auto_proc.get_auto_proc_program_attachment_by_id(attachment_id)
