from flask_restx import Namespace, Resource
from app.models import BeamLineSetup as BeamLineSetupModel
from app.modules.beam_line_setup.schemas import f_beam_line_setup_schema,  ma_beam_line_setup_schema

api = Namespace('BeamLineSetup', description='BeamLineSetup related namespace', path='/beam_line_setup')

@api.route("")
class BeamLineSetupList(Resource):
    @api.doc(security="apikey")
    def get(self):
        beam_line_setup_list = BeamLineSetupModel.query.all()
        return ma_beam_line_setup_schema.dump(beam_line_setup_list)
