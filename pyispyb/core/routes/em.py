
__license__ = "LGPLv3+"


from pyispyb.flask_restx_patched import Resource

from pyispyb.app.extensions.api import api_v1, Namespace, legacy_api
from pyispyb.app.extensions.auth.decorators import proposal_authorization_required, authentication_required, permission_required, session_authorization_required
from pyispyb.core.modules import em
from flask import send_file, abort


api = Namespace(
    "EM", description="EM related namespace", path="/em"
)

api_v1.add_namespace(api)

############################
#          MOVIES          #
############################


@api.route("/proposal/<int:proposal_id>/datacollection/<int:dataCollection_id>/movies", endpoint="em_movies")
@legacy_api.route("/<token>/proposal/<proposal_id>/em/datacollection/<dataCollection_id>/movie/all")
@api.doc(security="apikey")
class Movies(Resource):

    @authentication_required
    @permission_required
    @proposal_authorization_required
    def get(self, proposal_id, dataCollection_id, **kwargs):
        return em.get_movies_data_by_dataCollection_id(proposal_id, dataCollection_id)


@api.route("/proposal/<int:proposal_id>/movie/<int:movie_id>/thumbnail", endpoint="em_movie_thumbnail")
@legacy_api.route("/<token>/proposal/<proposal_id>/em/datacollection/<dataCollectionId>/movie/<movie_id>/thumbnail")
@api.doc(security="apikey")
class MovieThumbnail(Resource):

    @authentication_required
    @permission_required
    @proposal_authorization_required
    def get(self, proposal_id, movie_id, **kwargs):
        path = em.get_movie_thumbnails(proposal_id, movie_id)
        if path:
            path = path["movie_thumbnail"]
        if path:
            return send_file(path, mimetype='image/png')
        else:
            abort(404)


@api.route("/proposal/<int:proposal_id>/movie/<int:movie_id>/thumbnail/motioncorrection", endpoint="em_movie_motioncorrection_thumbnail")
@legacy_api.route("/<token>/proposal/<proposal_id>/em/datacollection/<dataCollectionId>/movie/<movie_id>/motioncorrection/thumbnail")
@api.doc(security="apikey")
class MovieMotionCorrectionThumbnail(Resource):

    @authentication_required
    @permission_required
    @proposal_authorization_required
    def get(self, proposal_id, movie_id, **kwargs):
        path = em.get_movie_thumbnails(proposal_id, movie_id)
        if path:
            path = path["motion_correction_thumbnail"]
        if path:
            return send_file(path, mimetype='image/png')
        else:
            abort(404)


@api.route("/proposal/<int:proposal_id>/movie/<int:movie_id>/thumbnail/ctf", endpoint="em_movie_ctf_thumbnail")
@legacy_api.route("/<token>/proposal/<proposal_id>/em/datacollection/<dataCollectionId>/movie/<movie_id>/ctf/thumbnail")
@api.doc(security="apikey")
class MovieCTFThumbnail(Resource):

    @authentication_required
    @permission_required
    @proposal_authorization_required
    def get(self, proposal_id, movie_id, **kwargs):
        path = em.get_movie_thumbnails(proposal_id, movie_id)
        if path:
            path = path["ctf_thumbnail"]
        if path:
            return send_file(path, mimetype='image/png')
        else:
            abort(404)


@api.route("/proposal/<int:proposal_id>/movie/<int:movie_id>/plot/motioncorrectiondrift", endpoint="em_movies_thumbnail")
@legacy_api.route("/<token>/proposal/<proposal_id>/em/datacollection/<dataCollectionId>/movie/<movie_id>/motioncorrection/drift")
@api.doc(security="apikey")
class MovieMotionCorrectionDrift(Resource):

    @authentication_required
    @permission_required
    @proposal_authorization_required
    def get(self, proposal_id, movie_id, **kwargs):
        path = em.get_movie_thumbnails(proposal_id, movie_id)
        if path:
            path = path["motion_correction_drift"]
        if path:
            return send_file(path, mimetype='image/png')
        else:
            abort(404)

############################
#          STATS           #
############################


@api.route("/session/<int:session_id>/stats", endpoint="em_stats_session")
@legacy_api.route("/<token>/proposal/<proposal>/em/session/<session_id>/stats")
@api.doc(security="apikey")
class StatsSession(Resource):

    @authentication_required
    @permission_required
    @session_authorization_required
    def get(self, session_id, **kwargs):
        return em.get_stats_by_session_id(session_id)


@api.route("/proposal/<int:proposal_id>/data_collections/<string:data_collections_ids>/stats", endpoint="em_stats_data_collections")
@api.doc(security="apikey")
class StatsDataCollectionIds(Resource):

    @authentication_required
    @permission_required
    @proposal_authorization_required
    def get(self, proposal_id, data_collections_ids):
        return em.get_stats_by_data_collections_ids(proposal_id, data_collections_ids)


@api.route("/proposal/<int:proposal_id>/data_collections_group/<string:data_collections_group_id>/stats", endpoint="em_stats_data_collections_group")
@api.doc(security="apikey")
class StatsDataCollectionGroupId(Resource):

    @authentication_required
    @permission_required
    @proposal_authorization_required
    def get(self, proposal_id, data_collections_group_id, **kwargs):
        return em.get_stats_by_data_collections_group_id(proposal_id, data_collections_group_id)

############################
#     DATA COLLECTION      #
############################


@api.route("/proposal/<int:proposal_id>/session/<int:session_id>/data_collection_groups", endpoint="em_data_collections_groups")
@legacy_api.route("/<token>/proposal/<proposal_id>/em/datacollection/session/<session_id>/list")
@api.doc(security="apikey")
class DataCollectionGroup(Resource):

    @authentication_required
    @permission_required
    @proposal_authorization_required
    def get(self, proposal_id, session_id, **kwargs):
        return em.get_data_collections_groups(proposal_id, session_id)
