from typing import Optional
import datetime

from pydantic import BaseModel, Field

from pyispyb.core.schemas.validators import WordDashSpace


class LaboratoryBase(BaseModel):
    name: str = WordDashSpace(title="Laboratory Name")
    address: str = Field(title="Address")
    city: str = Field(title="City")
    postcode: str = Field(title="Post Code")
    country: str = Field(title="Country")


class Laboratory(LaboratoryBase):
    # laboratoryId: int

    class Config:
        orm_mode = True


class PersonBase(BaseModel):
    givenName: str = Field(title="First Name")
    familyName: str = Field(title="Surname")
    emailAddress: Optional[str] = Field(title="Email Address", nullable=True)
    phoneNumber: Optional[str] = Field(title="Phone Number", nullable=True)

    Laboratory: Optional[Laboratory]


class Person(PersonBase):
    # personId: int

    class Config:
        title = "Contact Person"
        orm_mode = True


class LabContactBase(BaseModel):
    proposalId: int
    cardName: str = Field(
        title="Card Name", description="The name for this lab contact"
    )
    defaultCourrierCompany: Optional[str] = Field(
        title="Courrier Company", nullable=True
    )
    courierAccount: Optional[str] = Field(title="Account No.", nullable=True)
    billingReference: Optional[str] = Field(title="Billing Reference", nullable=True)
    dewarAvgCustomsValue: Optional[int] = Field(title="Avg Customs Value", unit="Eur")
    dewarAvgTransportValue: Optional[int] = Field(
        title="Avg Transport Value", unit="Eur"
    )

    Person: Person


class LabContactCreate(LabContactBase):
    pass


class LabContact(LabContactBase):
    labContactId: int
    personId: int
    recordTimeStamp: datetime.datetime = Field(
        description="Time lab contact was created"
    )

    class Config:
        orm_mode = True
