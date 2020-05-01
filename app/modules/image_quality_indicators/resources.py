from flask_restx import Namespace, Resource
from app.models import ImageQualityIndicator as ImageQualityIndicatorsModel
from app.modules.image_quality_indicators.schemas import (
    f_image_quality_indicators_schema,
    ma_image_quality_indicators_schema,
)

api = Namespace(
    "ImageQualityIndicators",
    description="ImageQualityIndicators related namespace",
    path="/image_quality_indicators",
)


@api.route("")
class ImageQualityIndicatorsList(Resource):
    @api.doc(security="apikey")
    def get(self):
        image_quality_indicators_list = ImageQualityIndicatorsModel.query.all()
        return ma_image_quality_indicators_schema.dump(image_quality_indicators_list)
