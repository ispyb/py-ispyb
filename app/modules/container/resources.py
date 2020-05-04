from flask_restx import Namespace, Resource
from app.models import Container as ContainerModel
from app.modules.container.schemas import f_container_schema, ma_container_schema

"""
api = Namespace(
    "Container", description="Container related namespace", path="/container"
)


@api.route("")
class ContainerList(Resource):
    @api.doc(security="apikey")
    def get(self):
        container_list = ContainerModel.query.all()
        return ma_container_schema.dump(container_list)
"""
