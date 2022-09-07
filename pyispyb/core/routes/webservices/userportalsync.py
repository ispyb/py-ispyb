import logging
from fastapi import HTTPException, status, Depends
from fastapi.responses import Response, JSONResponse
from ...modules import userportalsync as crud
from ...schemas import userportalsync as schema
from ....dependencies import permission
from .base import router


logger = logging.getLogger("ispyb")


@router.post(
    "/userportalsync/sync_proposal",
    response_model=schema.UserPortalProposalSync,
)
def sync_proposal(
    proposal: schema.UserPortalProposalSync,
    depends: bool = Depends(permission("uportal_sync")),
):
    """Create/Update a proposal from the User Portal and all its related entities"""
    try:
        execution_time = crud.sync_proposal(proposal=proposal)
        proposal_dict = proposal.dict()
        return JSONResponse(
            status_code=200,
            content={
                "message": f"The proposal {proposal_dict['proposal']['proposalCode']}"
                f"-{proposal_dict['proposal']['proposalNumber']} has been synchronized in {execution_time}"
            },
        )
    except Exception as e:
        logging.debug(e)
        raise HTTPException(status_code=500, detail=str(e))


@router.get(
    "/userportalsync/sync_proposal/schema",
    status_code=status.HTTP_200_OK,
)
def get_user_portal_sync_schema() -> str:
    """
    Return the User Portal Sync JSON schema
    It may be called by external User Portal applications to test/validate data
    """
    return Response(
        schema.UserPortalProposalSync.schema_json(indent=2),
        media_type="application/json",
    )
