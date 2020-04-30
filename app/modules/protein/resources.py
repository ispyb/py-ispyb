from flask_restx import Namespace, Resource
from app.models import Protein as ProteinModel
from app.modules.protein.schemas import f_protein_schema,  ma_protein_schema

api = Namespace('Protein', description='Protein related namespace', path='/protein')

@api.route("")
class ProteinList(Resource):
    @api.doc(security="apikey")
    def get(self):
        protein_list = ProteinModel.query.all()
        return ma_protein_schema.dump(protein_list)
