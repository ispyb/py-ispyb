from flask_restx import Namespace, Resource

# from ispyb.auth import token_required
from app.extensions import db
from app.models import Person as PersonModel
from app.modules.person.schemas import f_person_schema, ma_person_schema

api = Namespace("Person", description="Person", path="/person")


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


@api.route("")
class PersonList(Resource):
    """Allows to get all persons"""

    @api.doc(security="apikey")
    # @token_required
    def get(self):
        """Returns all persons"""
        # app.logger.info("Return all person")
        return get_all_persons()

    @api.expect(f_person_schema)
    @api.marshal_with(f_person_schema, code=201)
    def post(self):
        """Adds a new person"""
        # app.logger.info("Insert new person")
        try:
            person = PersonModel(**api.payload)
            db.session.add(person)
            db.session.commit()
        except Exception as ex:
            print(ex)
            # app.logger.exception(str(ex))
            db.session.rollback()
        # json_data = request.form['data']
        # print(json_data)
        # data = ma_proposal_schema.load(json_data)


@api.route("/<int:person_id>")
class Person(Resource):
    """Allows to get/set/delete a person"""

    @api.doc(description="person_id should be an integer ")
    @api.marshal_with(f_person_schema)
    # @token_required
    def get(self, person_id):
        """Returns a person by personId"""
        return get_person_by_id(person_id)

    """
    #@ns.doc(parser=parser)
    @ns.expect(f_proposal_schema)
    def post(self, prop_id):
        json_data = request.form['data']
        print(json_data)
        data = ma_proposal_schema.load(json_data)

    """
