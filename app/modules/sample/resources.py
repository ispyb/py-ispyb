from flask_restx import Namespace, Resource

from app.models import BLSample as SampleModel
from app.modules.sample.schemas import f_sample_schema,  ma_sample_schema


api = Namespace('Sample', description='Sample related namespace', path='/sample')


@api.route("")
class SampleList(Resource):

    @api.doc(security="apikey")
    def get(self):
        sample_list = SampleModel.query.all()
        return ma_sample_schema.dump(sample_list)
