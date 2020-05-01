from flask_restx import Namespace, Resource
from app.models import Detector as DetectorModel
from app.modules.detector.schemas import f_detector_schema, ma_detector_schema

api = Namespace("Detector", description="Detector related namespace", path="/detector")


@api.route("")
class DetectorList(Resource):
    @api.doc(security="apikey")
    def get(self):
        detector_list = DetectorModel.query.all()
        return ma_detector_schema.dump(detector_list)
