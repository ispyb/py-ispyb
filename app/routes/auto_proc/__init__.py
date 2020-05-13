"""
ISPyB flask server
"""

from flask_restx import Namespace, Resource

from app.extensions.api import api_v1
from app.modules import auto_proc


api = Namespace(
    "Auto processing", description="Auto processing related namespace", path="/autoproc"
)

api_v1.add_namespace(api)


@api.route("")
class AutoProcList(Resource):
    """Auto processing resource"""

    @api.doc(security="apikey")
    # @token_required
    def get(self):
        """Returns all auto processing results"""
        # app.logger.info('Returns all auto proc results')
        auto_proc.get_auto_proc_list()
