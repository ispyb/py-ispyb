"""ISPyB flask server"""
import logging

from app.extensions import db
from app.models import Proposal as ProposalModel
from app.modules import person
from app.modules.proposal.schemas import f_proposal_schema, ma_proposal_schema


log = logging.getLogger(__name__)


def get_all_proposals():
    """Returns all proposals"""
    proposals = ProposalModel.query.all()
    return ma_proposal_schema.dump(proposals, many=True)


def get_proposal_by_id(proposal_id):
    """Returns proposal by id"""
    proposal = ProposalModel.query.filter_by(proposalId=proposal_id).first()
    return ma_proposal_schema.dump(proposal)


def get_proposals_by_login_name(login_name):
    """Returns proposals by a login name
    """
    person_id = person.get_person_id_by_login(login_name)
    # TODO this is not nice...
    proposal = ProposalModel.query.filter_by(personId=person_id)
    return ma_proposal_schema.dump(proposal, many=True)

def add_proposal(proposal_dict):
    try:
        proposal = ProposalModel(proposal_dict)
        db.session.add(proposal)
        db.session.commit()
    except Exception as ex:
        print(ex)
        # app.logger.exception(str(ex))
        db.session.rollback()
