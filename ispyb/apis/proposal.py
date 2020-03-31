from flask import request
from flask_restplus import Namespace, Resource
from ispyb import app, api, db
from ispyb.models import Proposal as ProposalModel
from ispyb.schemas import f_proposal_schema,  ma_proposal_schema
from ispyb.auth import token_required

ns = Namespace('Proposal', description='Proposal related namespace', path='prop')

#parser = api.parser()
#parser.add_argument('task', type=str, required=True, help='The task details', location='form')

@ns.route("/")
class ProposalList(Resource):
    """Allows to get all proposals"""

    @ns.doc(security="apikey")
    #@token_required
    def get(self):
        """Returns all proposals"""
        app.logger.info("Return all proposals")
        proposals = ProposalModel.query.all()
        return ma_proposal_schema.dump(proposals, many=True)

    @ns.expect(f_proposal_schema)
    @ns.marshal_with(f_proposal_schema, code=201)
    def post(self):
        """Adds a new proposal"""
        app.logger.info("Insert new proposal")
        try:
            proposal = ProposalModel(**api.payload)
            print(dir(proposal))
            db.session.add(proposal)
            db.session.commit()
        except Exception as ex:
            print(ex)
            app.logger.exception(str(ex))
            db.session.rollback()
        #json_data = request.form['data']
        #print(json_data)
        #data = ma_proposal_schema.load(json_data)


@ns.route("/<int:prop_id>")
#@ns.param("prop_id", "Proposal id")
class Proposal(Resource):
    """Allows to get/set/delete a proposal"""

    @ns.doc(description='prop_id should be an integer ')
    @ns.marshal_with(f_proposal_schema)
    #@token_required
    def get(self, prop_id):
        """Returns a proposal by proposalId"""
        proposal= ProposalModel.query.filter_by(proposalId=prop_id).first()
        return ma_proposal_schema.dump(proposal)

    
    """
    #@ns.doc(parser=parser)
    @ns.expect(f_proposal_schema)
    def post(self, prop_id):
        json_data = request.form['data']
        print(json_data)
        data = ma_proposal_schema.load(json_data)

    """
