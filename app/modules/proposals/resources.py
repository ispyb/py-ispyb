"""
ISPyB flask server
"""

from flask_restx import Namespace, Resource

#from ispyb.auth import token_required
#from ispyb.apis import person as person_api
from app.models import Proposal as ProposalModel
from app.modules.proposals.schemas import f_proposal_schema, ma_proposal_schema

api = Namespace('Proposal', description='Proposal related namespace', path='/prop')

def get_all_proposals():
    """Returns all proposals"""
    proposals = ProposalModel.query.all()
    return ma_proposal_schema.dump(proposals, many=True)

def get_proposal_by_id(proposal_id):
    """Returns proposal by id"""
    proposal = ProposalModel.query.filter_by(proposalId=proposal_id).first()
    return ma_proposal_schema.dump(proposal)

#
#def get_proposals_by_login_name(login_name):
#    """Returns proposals by a login name
#    """
#    person_id = person_api.get_person_id_by_login(login_name)
#    #TODO this is not nice...
#    proposal = ProposalModel.query.filter_by(personId=person_id)
#    return ma_proposal_schema.dump(proposal, many=True)

@api.route("")
class ProposalList(Resource):
    """Allows to get all proposals"""

    @api.doc(security="apikey")
    @api.marshal_list_with(f_proposal_schema)
    #@token_required
    def get(self):
        """Returns all proposals"""
        #app.logger.info("Return all proposals")
        return get_all_proposals()

    @api.expect(f_proposal_schema)
    @api.marshal_with(f_proposal_schema, code=201)
    def post(self):
        """Adds a new proposal"""
        #app.logger.info("Insert new proposal")
        try:
            proposal = ProposalModel(**api.payload)
            db.session.add(proposal)
            db.session.commit()
        except Exception as ex:
            print(ex)
            #app.logger.exception(str(ex))
            db.session.rollback()
        #json_data = request.form['data']
        #print(json_data)
        #data = ma_proposal_schema.load(json_data)


@api.route("/<int:prop_id>")
#@api.param("prop_id", "Proposal id")
class Proposal(Resource):
    """Allows to get/set/delete a proposal"""

    @api.doc(description='prop_id should be an integer ')
    @api.marshal_with(f_proposal_schema)
    #@token_required
    def get(self, prop_id):
        """Returns a proposal by proposalId"""
        return get_proposal_by_id(prop_id)
    
    """
    #@api.doc(parser=parser)
    @api.expect(f_proposal_schema)
    def post(self, prop_id):
        json_data = request.form['data']
        print(json_data)
        data = ma_proposal_schema.load(json_data)

    """
@api.route("/login_name/<string:login_name>")
#@api.param("prop_id", "Proposal id")
class ProposalByLogin(Resource):
    """Allows to get proposal by person login name"""

    @api.doc(description='login_name should be a string')
    @api.marshal_with(f_proposal_schema)
    #@token_required
    def get(self, login_name):
        """Returns a proposal by login"""
        #app.logger.info("Returns all proposals for user with login name %s" % login_name)
        return get_proposals_by_login_name(login_name)
