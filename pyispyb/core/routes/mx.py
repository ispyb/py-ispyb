
__license__ = "LGPLv3+"


import os
from pyispyb.core.modules.proposal import find_proposal_id
from flask_restx import Resource

from pyispyb.app.extensions.api import api_v1, Namespace, legacy_api, http_exceptions
from pyispyb.app.extensions.auth.decorators import proposal_authorization_required, authentication_required, permission_required
from pyispyb.core.modules import mx
from flask import send_file


api = Namespace(
    "MX", description="MX related namespace", path="/mx"
)

api_v1.add_namespace(api)


@api.route("/proposal/<int:proposal_id>/datacollection/<int:datacollection_id>/crystalsnaphot/<int:snapshot_id>")
@legacy_api.route("/<token>/proposal/<proposal_id>/mx/datacollection/<datacollection_id>/crystalsnaphot/<int:snapshot_id>/get")
@api.doc(security="apikey")
class CrystalSnapshot(Resource):

    @authentication_required
    @permission_required("any", ["own_proposal", "all_proposals"])
    @proposal_authorization_required
    def get(self, proposal_id, datacollection_id, snapshot_id, **kwargs):
        """Get crystal snapshot for datacollection.

        Args:
            proposal_id (str): proposal id or name
            datacollection_id (str): data collection id
            snapshot_id (str): crystal snaphot id
        """
        if snapshot_id < 1 or snapshot_id > 4:
            http_exceptions.abort(400, "snapshot_id should be between 1 and 4.")
        proposal_id = find_proposal_id(proposal_id)
        path = mx.get_crystal_snapshots(proposal_id, datacollection_id)
        if path and f"xtalSnapshotFullPath{snapshot_id}" in path:
            path = path[f"xtalSnapshotFullPath{snapshot_id}"]
        if path and os.path.isfile(path):
            return send_file(path, mimetype='image/png')
        else:
            http_exceptions.abort(404, "no snapshot found.")
