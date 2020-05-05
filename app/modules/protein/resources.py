from flask_restx import Namespace, Resource
from app.models import Protein as ProteinModel
from app.modules.protein.schemas import f_protein_schema, ma_protein_schema


def get_protein_list():
    protein_list = ProteinModel.query.all()
    return ma_protein_schema.dump(protein_list)
