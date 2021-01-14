"""
Project: py-ispyb.

https://github.com/ispyb/py-ispyb

This file is part of py-ispyb software.

py-ispyb is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

py-ispyb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.
"""

import logging
from datetime import datetime

from flask import request
from pyispyb.flask_restx_patched import Resource, HTTPStatus, abort

from pyispyb.app.extensions.api import api_v1, Namespace
from pyispyb.app.extensions.auth import token_required, authorization_required

from pyispyb.core.schemas import beamline_setup as beamline_setup_schemas
from pyispyb.core.schemas import robot_action as robot_action_schemas
from pyispyb.core.schemas import detector as detector_schemas
from pyispyb.core.modules import beamline_setup, robot_action, detector


__license__ = "LGPLv3+"

log = logging.getLogger(__name__)
api = Namespace("Beamline", description="Beamline related namespace", path="/beamline")
api_v1.add_namespace(api)


@api.route("/setups", endpoint="beamline_setup")
@api.doc(security="apikey")
class BeamlineSetups(Resource):
    """Allows to get all beamline_setups and insert a new one"""

    @token_required
    @authorization_required
    def get(self):
        """Returns list of beamline_setups"""
        return beamline_setup.get_beamline_setups(request)

    @api.expect(beamline_setup_schemas.f_schema)
    @api.marshal_with(beamline_setup_schemas.f_schema, code=201)
    @token_required
    @authorization_required
    def post(self):
        """Adds a new beamline_setup"""
        log.info("Inserts a new beamline_setup")
        return beamline_setup.add_beamline_setup(api.payload)


@api.route("/setups/<int:beamline_setup_id>", endpoint="beamline_setup_by_id")
@api.param("beamline_setup_id", "beamline_setup id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="beamline_setup not found.")
class BeamlineSetupById(Resource):
    """Allows to get/set/delete a beamline_setup"""

    @api.doc(description="beamline_setup_id should be an integer ")
    @api.marshal_with(
        beamline_setup_schemas.f_schema, skip_none=False, code=HTTPStatus.OK
    )
    @token_required
    @authorization_required
    def get(self, beamline_setup_id):
        """Returns a beamline_setup by beamline_setupId"""
        return beamline_setup.get_beamline_setup_by_id(beamline_setup_id)

    @api.expect(beamline_setup_schemas.f_schema)
    @api.marshal_with(beamline_setup_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def put(self, beamline_setup_id):
        """Fully updates beamline_setup with beamline_setup_id"""
        return beamline_setup.update_beamline_setup(beamline_setup_id, api.payload)

    @api.expect(beamline_setup_schemas.f_schema)
    @api.marshal_with(beamline_setup_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, beamline_setup_id):
        """Partially updates beamline_setup with id beamline_setupId"""
        return beamline_setup.patch_beamline_setup(beamline_setup_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, beamline_setup_id):
        """Deletes a beamline_setup by beamline_setupId"""
        return beamline_setup.delete_beamline_setup(beamline_setup_id)


@api.route("/robot_actions", endpoint="robot_actions")
@api.doc(security="apikey")
class RobotActions(Resource):
    """Allows to get robot action db items and insert a new one"""

    @token_required
    @authorization_required
    def get(self):
        """Returns list of robot_actions"""
        return robot_action.get_robot_actions(request)

    @api.expect(robot_action_schemas.f_schema)
    @api.marshal_with(robot_action_schemas.f_schema, code=201)
    # @api.errorhandler(FakeException)
    # TODO add custom exception handling
    @token_required
    @authorization_required
    def post(self):
        """Adds a new robot_action"""
        return robot_action.add_robot_action(api.payload)


@api.route("/robot_actions/<int:robot_action_id>", endpoint="robot_action_by_id")
@api.param("robot_action_id", "robot_action id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="robot_action not found.")
class RobotActionById(Resource):
    """Allows to get/set/delete a robot_action"""

    @api.doc(description="robot_action_id should be an integer ")
    @api.marshal_with(
        robot_action_schemas.f_schema, skip_none=False, code=HTTPStatus.OK
    )
    @token_required
    @authorization_required
    def get(self, robot_action_id):
        """Returns a robot_action by robot_action_id"""
        return robot_action.get_robot_action_by_id(robot_action_id)

    @api.expect(robot_action_schemas.f_schema)
    @api.marshal_with(robot_action_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def put(self, robot_action_id):
        """Fully updates robot_action with robot_action_id"""
        return robot_action.update_robot_action(robot_action_id, api.payload)

    @api.expect(robot_action_schemas.f_schema)
    @api.marshal_with(robot_action_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, robot_action_id):
        """Partially updates robot_action with robot_action_id"""
        return robot_action.patch_robot_action(robot_action_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, robot_action_id):
        """Deletes a robot_action by robot_action_id"""
        return robot_action.delete_robot_action(robot_action_id)


@api.route("/detectors", endpoint="detectors")
@api.doc(security="apikey")
class Detectors(Resource):
    """Allows to get all detectors and insert a new one"""

    @token_required
    @authorization_required
    def get(self):
        """Returns list of detectors"""
        return detector.get_detectors(request)

    @api.expect(detector_schemas.f_schema)
    @api.marshal_with(detector_schemas.f_schema, code=201)
    # @api.errorhandler(FakeException)
    # TODO add custom exception handling
    @token_required
    @authorization_required
    def post(self):
        """Adds a new detector"""
        log.info("Inserts a new detector")
        return detector.add_detector(api.payload)


@api.route("/detectors/<int:detector_id>", endpoint="detector_by_id")
@api.param("detector_id", "detector id (integer)")
@api.doc(security="apikey")
@api.response(code=HTTPStatus.NOT_FOUND, description="detector not found.")
class DetectorById(Resource):
    """Allows to get/set/delete a detector"""

    @api.doc(description="detector_id should be an integer ")
    @api.marshal_with(detector_schemas.f_schema, skip_none=False, code=HTTPStatus.OK)
    @token_required
    @authorization_required
    def get(self, detector_id):
        """Returns a detector by detectorId"""
        return detector.get_detector_by_id(detector_id)

    @api.expect(detector_schemas.f_schema)
    @api.marshal_with(detector_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def put(self, detector_id):
        """Fully updates detector with detector_id"""
        return detector.update_detector(detector_id, api.payload)

    @api.expect(detector_schemas.f_schema)
    @api.marshal_with(detector_schemas.f_schema, code=HTTPStatus.CREATED)
    @token_required
    @authorization_required
    def patch(self, detector_id):
        """Partially updates detector with id detectorId"""
        return detector.patch_detector(detector_id, api.payload)

    @token_required
    @authorization_required
    def delete(self, detector_id):
        """Deletes a detector by detectorId"""
        return detector.delete_detector(detector_id)
