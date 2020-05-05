from flask_restx import Namespace, Resource
from app.models import Screening as ScreeningModel
from app.modules.screening.schemas import f_screening_schema, ma_screening_schema

api = Namespace(
    "Screening", description="Screening related namespace", path="/screening"
)


@api.route("")
class ScreeningList(Resource):
    @api.doc(security="apikey")
    def get(self):
        screening_list = ScreeningModel.query.all()
        return ma_screening_schema.dump(screening_list)
