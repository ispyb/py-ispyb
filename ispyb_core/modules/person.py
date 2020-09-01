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
#  along with py-ispyb. If not, see <http://www.gnu.org/licenses/>.


__license__ = "LGPLv3+"


from ispyb_core.models import Person as PersonModel
from ispyb_core.schemas.person import person_f_schema, person_ma_schema


def get_all_persons():
    """Returns all person"""
    person = PersonModel.query.all()
    return person_ma_schema.dump(person, many=True)


def get_person_by_id(person_id):
    """Returns person by id"""
    person = PersonModel.query.filter_by(personId=person_id).first()
    return person_ma_schema.dump(person)[0]


def get_person_id_by_login(login_name):
    """Gets person id by login name

    Args:
        login_name (str): user login name

    Returns:
        int: int
    """
    person_id = None
    try:
        person = PersonModel.query.filter_by(login=login_name).first()
        person_id = person.personId
    except BaseException as ex:
        print("Unable to get person id with login name %s (%s)" % (login_name, str(ex)))
    finally:
        return person_id
