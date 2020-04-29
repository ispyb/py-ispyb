from flask_restx import Namespace, Resource
from app.models import EnergyScan as EnergyScanModel
from app.modules.energy_scan.schemas import f_energy_scan_schema,  ma_energy_scan_schema

api = Namespace('EnergyScan', description='EnergyScan related namespace', path='/energy_scan')

@api.route("")
class EnergyScanList(Resource):
    @api.doc(security="apikey")
    def get(self):
        energy_scan_list = EnergyScanModel.query.all()
        return ma_energy_scan_schema.dump(energy_scan_list)
