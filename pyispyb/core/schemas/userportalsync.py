from typing import List
from pydantic import BaseModel, conlist
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from pyispyb.core import models


PydanticPerson = sqlalchemy_to_pydantic(
    models.Person, exclude={"personId", "recordTimeStamp"}
)
PydanticLaboratory = sqlalchemy_to_pydantic(
    models.Laboratory, exclude={"laboratoryId", "recordTimeStamp"}
)
PydanticProposal = sqlalchemy_to_pydantic(
    models.Proposal, exclude={"proposalId", "personId", "bltimeStamp"}
)
PydanticSession = sqlalchemy_to_pydantic(
    models.BLSession, exclude={"sessionId", "proposalId", "bltimeStamp", "lastUpdate"}
)
PydanticProtein = sqlalchemy_to_pydantic(models.Protein)


class Person(PydanticPerson):
    class Config:
        orm_mode = True


class PersonLaboratory(Person):
    laboratory: PydanticLaboratory


class Protein(PydanticProtein):
    class Config:
        orm_mode = True


class Session(PydanticSession):
    class Config:
        orm_mode = True


class PydanticProposal(BaseModel):
    proposal: PydanticProposal
    # Here we need minimum 1 Person to be related to the Proposal (foreign key constraint)
    persons: conlist(PersonLaboratory, min_items=1)
    sessions: List[Session]
    proteins: List[Protein]


class UserPortalProposalSync(PydanticProposal):
    pass
