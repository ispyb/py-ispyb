from typing import List, Optional, Literal
from pydantic import BaseModel, conlist, root_validator
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from pyispyb.core.schemas.laboratories import Laboratory
from pyispyb.core import models
from datetime import datetime

PydanticPerson = sqlalchemy_to_pydantic(
    models.Person, exclude={"personId", "laboratoryId", "recordTimeStamp"}
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
PydanticSessionHasPerson = sqlalchemy_to_pydantic(
    models.SessionHasPerson, exclude={"sessionId", "personId"}
)


class Person(PydanticPerson):
    # At least siteId or login required to be able to check for existing Person in DB (to update or create)
    siteId: Optional[int] = None
    login: Optional[str] = None

    # https://github.com/samuelcolvin/pydantic/issues/506
    @root_validator()
    def check_siteId_or_login(cls, values):
        if (values.get("siteId") is None) and (values.get("login") is None):
            raise ValueError("either siteId or login is required")
        return values

    class Config:
        orm_mode = True


class PersonSessionOptions(PydanticSessionHasPerson):
    role: Optional[
        Literal[
            "Local Contact",
            "Local Contact 2",
            "Staff",
            "Team Leader",
            "Co-Investigator",
            "Principal Investigator",
            "Alternate Contact",
        ]
    ]


class PersonLaboratory(Person):
    laboratory: Laboratory
    # Optional section to be used in Session_has_Person
    session_options: Optional[PersonSessionOptions]


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
    # persons related to sessions is optional
    persons: Optional[List[PersonLaboratory]]

    class Config:
        orm_mode = True


class PydanticProposal(BaseModel):
    proposal: Proposal
    sessions: Optional[List[Session]]
    proteins: Optional[List[Protein]]


class UserPortalProposalSync(PydanticProposal):
    pass
