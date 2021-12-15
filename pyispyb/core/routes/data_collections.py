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

import os
from flask import request, send_file, abort

from pyispyb.flask_restx_patched import Resource, HTTPStatus

from pyispyb.app.extensions.api import api_v1, Namespace
from pyispyb.app.extensions.auth.decorators import proposal_authorization_required, session_authorization_required, authentication_required, permission_required

from pyispyb.core.schemas import data_collection as data_collection_schemas
from pyispyb.core.schemas import data_collection_group as data_collection_group_schemas
from pyispyb.core.modules import data_collection


__license__ = "LGPLv3+"


api = Namespace(
    "Data collections",
    description="Data collection related namespace",
    path="/data_collections",
)
api_v1.add_namespace(api)


@api.route("/groups/infos/session/<int:session_id>", endpoint="data_collection_groups_infos")
@api.doc(security="apikey")
class DataColletionGroupsInfos(Resource):
    """Allows to get all data_collections"""

    @authentication_required
    @permission_required
    @session_authorization_required
    def get(self, session_id):
        """Returns list of data_collections"""
        query_dict = request.args.to_dict()
        return data_collection.get_data_collections_groups_infos(session_id)


@api.route("")
@api.doc(security="apikey")
class DataColletions(Resource):
    """Allows to get all data_collections"""

    @authentication_required
    @permission_required
    @api.marshal_list_with(data_collection_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    def get(self):
        """Returns list of data_collections"""
        # TODO implement authorization
        query_dict = request.args.to_dict()
        return data_collection.get_data_collections(query_dict)

    @authentication_required
    @permission_required
    @api.expect(data_collection_schemas.f_schema)
    @api.marshal_with(data_collection_schemas.f_schema, code=201)
    def post(self):
        """Adds a new session"""
        # TODO implement authorization
        return data_collection.add_data_collection(api.payload)


@api.route("/<int:data_collection_id>")
@api.param("data_collection_id", "Data collection id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="data collection not found.")
class DataCollectionById(Resource):
    """Allows to get/set/delete a data_collection"""

    @authentication_required
    @permission_required
    @api.doc(description="data_collection_id should be an integer ")
    @api.marshal_with(
        data_collection_schemas.f_schema,
        skip_none=False,
        code=HTTPStatus.OK,
    )
    def get(self, data_collection_id):
        """Returns a data_collection by data_collectionId"""
        # TODO implement authorization
        return data_collection.get_data_collection_by_id(data_collection_id)


@api.route("/<int:data_collection_id>/snapshot/<int:snapshot_index>")
@api.param("data_collection_id", "data_collection_id (integer)")
@api.param("snapshot_index", "snapshot_index (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="data collection not found.")
class DataCollectionSnapshot(Resource):
    """Allows to download snapshots associated to the data collection"""

    @authentication_required
    @permission_required
    @api.doc(description="data_collection_id and snapshot_id should be an integer")
    def get(self, data_collection_id, snapshot_index):
        """Downloads data collection attribute by id and attribute_name"""
        # TODO implement authorization
        data_collection_dict = data_collection.get_data_collection_by_id(
            data_collection_id
        )
        if data_collection_dict:
            snapshot_path = data_collection_dict.get(
                "xtalSnapshotFullPath%d" % snapshot_index)
            if snapshot_path:
                if os.path.exists(snapshot_path):
                    return send_file(
                        snapshot_path,
                        attachment_filename=os.path.basename(snapshot_path),
                        as_attachment=True
                    )
                else:
                    abort(
                        HTTPStatus.NOT_FOUND,
                        "File %s do not exist" % snapshot_path
                    )
            else:
                abort(
                    HTTPStatus.NOT_FOUND,
                    "No file name associated with xtalSnapshotFullPath%d" % snapshot_index
                )


@api.route("/<int:data_collection_id>/file")
@api.param("data_collection_id", "data_collection_id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="data collection not found.")
class DataCollectionFile(Resource):
    """Allows to download files associated to the data collection"""

    @authentication_required
    @permission_required
    @api.doc(description="data_collection_id should be an integer ")
    def get(self, data_collection_id):
        # TODO implement authorization
        """Downloads data collection attribute by id and attribute_name"""
        data_collection_dict = data_collection.get_data_collection_by_id(
            data_collection_id
        )
        if data_collection_dict:
            query_dict = request.args.to_dict()
            if "attribute_name" in query_dict:
                attribute_file_path = data_collection_dict.get(
                    query_dict["attribute_name"]
                )
                if attribute_file_path:
                    if os.path.exists(attribute_file_path):
                        return send_file(
                            attribute_file_path,
                            attachment_filename=os.path.basename(
                                attribute_file_path),
                            as_attachment=True
                        )
                    else:
                        abort(
                            HTTPStatus.NOT_FOUND,
                            "File %s do not exist" % attribute_file_path
                        )
                else:
                    abort(
                        HTTPStatus.NOT_FOUND,
                        "No file associated with attribute %s" %
                        query_dict["attribute_name"]
                    )

            else:
                abort(
                    HTTPStatus.NOT_FOUND,
                    "No attribute_name in query parameters"
                )


@api.route("/groups")
@api.doc(security="apikey")
class DataCollectionGroups(Resource):
    """Allows to get all data collection groups and add a new one"""

    @authentication_required
    @permission_required
    @api.marshal_list_with(data_collection_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    def get(self):
        """Returns list of data_collection_groups"""
        # TODO implement authorization
        return data_collection.get_data_collection_groups(request)

    @authentication_required
    @permission_required
    @api.expect(data_collection_group_schemas.f_schema)
    @api.marshal_with(data_collection_group_schemas.f_schema, code=201)
    def post(self):
        """Adds a new session"""
        # TODO implement authorization
        return data_collection.add_data_collection_group(api.payload)


@api.route("/groups/<int:data_collection_group_id>")
@api.param("data_collection_group_id", "data_collection group_id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="data collection group not found.")
class DataCollectionGroupById(Resource):
    """Allows to get/set/delete a data collection group"""

    @authentication_required
    @permission_required
    @api.doc(description="data_collection_group_id should be an integer ")
    @api.marshal_with(
        data_collection_group_schemas.f_schema,
        skip_none=False,
        code=HTTPStatus.OK,
    )
    def get(self, data_collection_group_id):
        """Returns a data_collection group by dataCollection_group_id"""
        # TODO implement authorization
        return data_collection.get_data_collection_group_by_id(data_collection_group_id)
