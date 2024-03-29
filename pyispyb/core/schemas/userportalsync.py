from typing import List, Optional, Literal
from pydantic import BaseModel, conlist, root_validator
from pydantic_sqlalchemy import sqlalchemy_to_pydantic
from pyispyb.core.schemas.laboratories import LaboratoryCreate
from ispyb import models
from datetime import datetime

PydanticPerson = sqlalchemy_to_pydantic(
    models.Person, exclude={"personId", "laboratoryId", "recordTimeStamp"}
)
PydanticProposal = sqlalchemy_to_pydantic(
    models.Proposal, exclude={"proposalId", "personId", "bltimeStamp"}
)
PydanticSession = sqlalchemy_to_pydantic(
    models.BLSession, exclude={"sessionId", "proposalId", "bltimeStamp", "comments"}
)

"""
Excluding _global field to avoid a Pydantic RuntimeWarning
RuntimeWarning: fields may not start with an underscore, ignoring "_global"
"""
PydanticProtein = sqlalchemy_to_pydantic(
    models.Protein,
    exclude={"proteinId", "proposalId", "personId", "bltimeStamp", "_global"},
)
PydanticSessionHasPerson = sqlalchemy_to_pydantic(
    models.SessionHasPerson, exclude={"sessionId", "personId"}
)
PydanticLabContact = sqlalchemy_to_pydantic(
    models.LabContact,
    exclude={"labContactId", "proposalId", "personId", "recordTimeStamp"},
)


class UPPerson(PydanticPerson):
    # At least login or externalId required to be able to check for existing Person in DB (to update or create)
    login: Optional[str] = None
    externalId: Optional[int] = None

    # https://github.com/samuelcolvin/pydantic/issues/506
    @root_validator()
    def check_login_or_externalId(cls, values):
        if (values.get("login") is None) and (values.get("externalId") is None):
            raise ValueError(
                "either login or externalId is required for a Person entity"
            )
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


class PersonProposalLaboratory(UPPerson):
    laboratory: Optional[LaboratoryCreate]


class PersonSessionLaboratory(UPPerson):
    laboratory: Optional[LaboratoryCreate]
    # Optional section to be used in Session_has_Person
    session_options: Optional[PersonSessionOptions]


class UPLabContact(PydanticLabContact):
    # Person is required for a LabContact
    person: PersonProposalLaboratory
    # Make dewarAvgCustomsValue and dewarAvgTransportValue optional fields
    # Somehow they are required by default
    dewarAvgCustomsValue: Optional[int]
    dewarAvgTransportValue: Optional[int]

    class Config:
        orm_mode = True


class UPProposal(PydanticProposal):
    # proposalCode and proposalNumber required
    proposalCode: str
    proposalNumber: str
    # externailId is an optional Integer and conversions to bynary 16 are done internally
    externalId: Optional[int] = None
    # Here we need minimum 1 Person to be related to the Proposal (foreign key constraint)
    persons: conlist(PersonProposalLaboratory, min_items=1)
    # LabContacts are always related to a proposal
    labcontacts: Optional[List[UPLabContact]]

    class Config:
        orm_mode = True


class UPProtein(PydanticProtein):
    # It may sync by checking protein acronym and proposalId in DB
    acronym: str
    # Can also use externalId to be able to check for existing protein in DB (to update or create)
    externalId: Optional[int]
    person: PersonProposalLaboratory

    class Config:
        orm_mode = True


class UPSession(PydanticSession):
    # expSessionPk or externalId to be able to check for existing session in DB (to update or create)
    # The expSessionPk field might be deprecated later
    expSessionPk: Optional[int]
    externalId: Optional[int]
    lastUpdate: Optional[datetime]
    # persons related to sessions is optional
    persons: Optional[List[PersonSessionLaboratory]]

    @root_validator()
    def check_expSessionPk_or_externalId(cls, values):
        if (values.get("expSessionPk") is None) and (values.get("externalId") is None):
            raise ValueError(
                "either expSessionPk or externalId is required for a Session entity"
            )
        return values

    class Config:
        orm_mode = True


class PydanticProposal(BaseModel):
    proposal: UPProposal
    sessions: Optional[List[UPSession]]
    proteins: Optional[List[UPProtein]]


class UserPortalProposalSync(PydanticProposal):
    pass
