from typing import List, Optional
from pydantic import BaseModel, conlist
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from pyispyb.core import models
from datetime import datetime

PydanticPerson = sqlalchemy_to_pydantic(
    models.Person, exclude={"personId", "laboratoryId", "recordTimeStamp"}
)
PydanticLaboratory = sqlalchemy_to_pydantic(
    models.Laboratory, exclude={"laboratoryId", "recordTimeStamp"}
)
PydanticProposal = sqlalchemy_to_pydantic(
    models.Proposal, exclude={"proposalId", "personId", "bltimeStamp"}
)
PydanticSession = sqlalchemy_to_pydantic(
    models.BLSession, exclude={"sessionId", "proposalId", "bltimeStamp"}
)
PydanticProtein = sqlalchemy_to_pydantic(
    models.Protein, exclude={"proteinId", "proposalId", "personId", "bltimeStamp"}
)


class Person(PydanticPerson):
    # At least siteId required to be able to check for existing Person in DB (to update or create)
    siteId: int

    class Config:
        orm_mode = True


class Laboratory(PydanticLaboratory):
    # laboratoryExtPk required to be able to check for existing Laboratory in DB (to update or create)
    laboratoryExtPk: int

    class Config:
        orm_mode = True


class PersonLaboratory(Person):
    laboratory: Laboratory


class Proposal(PydanticProposal):
    # proposalCode and proposalNumber required
    proposalCode: str
    proposalNumber: str
    # Here we need minimum 1 Person to be related to the Proposal (foreign key constraint)
    persons: conlist(PersonLaboratory, min_items=1)

    class Config:
        orm_mode = True


class Protein(PydanticProtein):
    person: PersonLaboratory

    class Config:
        orm_mode = True


class Session(PydanticSession):
    # expSessionPk required to be able to check for existing session in DB (to update or create)
    expSessionPk: int
    lastUpdate: Optional[datetime]
    persons: Optional[List[PersonLaboratory]]

    class Config:
        orm_mode = True


class PydanticProposal(BaseModel):
    proposal: Proposal
    sessions: Optional[List[Session]]
    proteins: Optional[List[Protein]]


class UserPortalProposalSync(PydanticProposal):
    pass
