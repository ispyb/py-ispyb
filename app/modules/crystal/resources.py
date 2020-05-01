"""
ISPyB flask server
"""

from flask_restx import Namespace, Resource

# from ispyb.auth import token_required

api = Namespace("Crystal", description="Crystal related namespace", path="/crystal")


@api.route("/")
class CrystalList(Resource):
    """Crystal list resource"""

    @api.doc(security="apikey")
    # @token_required
    def get(self):
        """Returns all crystal records"""
        return "TODO"
