from flask_restplus import Namespace, Resource
from ispyb import app, api, db
from ispyb.models import Person as PersonModel
from ispyb.schemas import f_person_schema,  ma_person_schema
from ispyb.auth import token_required

ns = Namespace('Person', description='Person', path='/person')

def get_all_persons():
    """Returns all person"""
    person = PersonModel.query.all()
    return ma_person_schema.dump(person, many=True)

def get_person_by_id(person_id):
    """Returns person by id"""
    person = PersonModel.query.filter_by(personId=person_id).first()
    return ma_person_schema.dump(person)

#def get_propsoal_by_person(person):
#    person = PersonMode.query.filter_by
#    proposal = ProposalMode.query.filter()

@ns.route("")
class PersonList(Resource):
    """Allows to get all persons"""

    @ns.doc(security="apikey")
    #@token_required
    def get(self):
        """Returns all proposals"""
        app.logger.info("Return all person")
        return get_all_persons()

    @ns.expect(f_person_schema)
    @ns.marshal_with(f_person_schema, code=201)
    def post(self):
        """Adds a new person"""
        app.logger.info("Insert new person")
        try:
            person = PersonModel(**api.payload)
            db.session.add(person)
            db.session.commit()
        except Exception as ex:
            print(ex)
            app.logger.exception(str(ex))
            db.session.rollback()
        #json_data = request.form['data']
        #print(json_data)
        #data = ma_proposal_schema.load(json_data)


@ns.route("/<int:person_id>")
class Person(Resource):
    """Allows to get/set/delete a person"""

    @ns.doc(description='person_id should be an integer ')
    @ns.marshal_with(f_person_schema)
    #@token_required
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
