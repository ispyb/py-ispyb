from flask_restx import Namespace, Resource
from app.models import Crystal as CrystalModel
from app.modules.crystal.schemas import f_crystal_schema, ma_crystal_schema


def get_crystal_list():
    crystal_list = CrystalModel.query.all()
    return ma_crystal_schema.dump(crystal_list)
