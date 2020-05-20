# encoding: utf-8
#
#  Project: py-ispyb
#  https://github.com/ispyb/py-ispyb
#
#  This file is part of py-ispyb software.
#
#  py-ispyb is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  py-ispyb is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with MXCuBE. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"


from app.models import BeamLineSetup as BeamLineSetupModel
from app.modules.beam_line_setup.schemas import (
    f_beam_line_setup_schema,
    ma_beam_line_setup_schema,
)


def get_beamline_setup_list():
    beam_line_setup_list = BeamLineSetupModel.query.all()
    return ma_beam_line_setup_schema.dump(beam_line_setup_list)
