"""ISPyB flask server"""

from app.models import Person as PersonModel
from app.modules.person.schemas import f_person_schema, ma_person_schema


def get_all_persons():
    """Returns all person"""
    person = PersonModel.query.all()
    return ma_person_schema.dump(person, many=True)


def get_person_by_id(person_id):
    """Returns person by id"""
    person = PersonModel.query.filter_by(personId=person_id).first()
    return ma_person_schema.dump(person)


def get_person_id_by_login(login_name):
    person = PersonModel.query.filter_by(login=login_name).first()
    return person.personId


def find_person_by_logn(self, login, beamline=None):
    return

