import logging
from fastapi import HTTPException, Depends
from ...modules import userportalsync as crud
from ...schemas import userportalsync as schema
from ....dependencies import permission
from ..responses import Message
from ....app.base import AuthenticatedAPIRouter

router = AuthenticatedAPIRouter(
    prefix="/webservices/userportalsync",
    tags=["Webservices - User portal sync"],
    dependencies=[Depends(permission("uportal_sync"))],
)

logger = logging.getLogger("ispyb")


@router.post(
    "/sync_proposal",
    response_model=Message,
    responses={400: {"description": "The input data is not following the schema"}},
)
def sync_proposal(
    proposal: schema.UserPortalProposalSync,
):
    """Create/Update a proposal from the User Portal and all its related entities"""
    try:
        execution_time = crud.sync_proposal(proposal=proposal)
        proposal_dict = proposal.dict()
        return {
            "message": f"The proposal {proposal_dict['proposal']['proposalCode']}"
            f"-{proposal_dict['proposal']['proposalNumber']} has been synchronized in {execution_time}"
        }

    except Exception as e:
        logging.debug(e)
        raise HTTPException(status_code=400, detail=str(e))
