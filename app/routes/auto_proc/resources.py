"""
ISPyB flask server
"""

from flask_restx import Namespace, Resource

from app.models import AutoProc as AutoProcModel
from app.modules import auto_proc

api = Namespace(
    "Auto processing", description="Auto processing related namespace", path="/autoproc"
)


@api.route("")
class AutoProcList(Resource):
    """Auto processing resource"""

    @api.doc(security="apikey")
    # @token_required
    def get(self):
        """Returns all auto processing results"""
        # app.logger.info('Returns all auto proc results')
        auto_proc_list = auto_proc.schemas.AutoProcModel.query.all()
        return auto_proc.schemas.ma_auto_proc_schema.dump(auto_proc_list)
