from flask_restx import Namespace, Resource
from app.models import RobotAction as RobotActionModel
from app.modules.robot_action.schemas import (
    f_robot_action_schema,
    ma_robot_action_schema,
)

api = Namespace(
    "RobotAction", description="RobotAction related namespace", path="/robot_action"
)


@api.route("")
class RobotActionList(Resource):
    @api.doc(security="apikey")
    def get(self):
        robot_action_list = RobotActionModel.query.all()
        return ma_robot_action_schema.dump(robot_action_list)
