import logging
import time
from typing import Any
from sqlalchemy.orm import Session, joinedload
from pyispyb.core import models
from pyispyb.app.extensions.database.session import engine
from ..schemas import userportalsync as schema
from pyispyb.app.utils import timed

logger = logging.getLogger("ispyb")


def sync_proposal(proposal: schema.UserPortalProposalSync) -> time:
    """
    Initialize a transactional session to be able to rollback if something goes wrong
    https://docs.sqlalchemy.org/en/14/orm/session_transaction.html
    """
    start = time.time()
    session = Session(engine)

    # Initialize UserPortalSync class
    user_portal_sync = UserPortalSync(session)

    # Get full proposal dict
    full_dict = proposal.dict()
    # Get source entity dicts
    source_proposal = full_dict.pop("proposal")
    source_persons = full_dict.pop("persons")

    try:
        # Process the Persons
        user_portal_sync.process_persons(source_persons)
        # At this point all Persons have been either updated or created

        # Process the Proposal
        # The first Person in the list will be the one having the relation to the proposal table
        # For now ignoring the update if the person list changes the order
        user_portal_sync.process_proposal(source_proposal, source_persons[0])

        session.commit()
    except Exception as e:
        session.rollback()
        logger.debug(e)
    finally:
        session.close()
    took = round(time.time() - start, 3)
    return took


class UserPortalSync(object):
    def __init__(self, session):
        self.session = session
        self.proposalId = None

    def get_ispyb_proposals(self):
        proposals = self.session.query(
            models.Proposal.proposalId,
            models.Proposal.title,
            models.Proposal.proposalCode,
            models.Proposal.proposalNumber,
            models.Proposal.proposalType,
        )
        ispyb_proposals = [p._asdict() for p in proposals.all()]
        return ispyb_proposals

    def get_ispyb_persons(self):
        persons = self.session.query(
            models.Person.personId,
            models.Person.givenName,
            models.Person.familyName,
            models.Person.emailAddress,
            models.Person.phoneNumber,
            models.Person.login,
            models.Person.siteId,
        )
        ispyb_persons = [p._asdict() for p in persons.all()]
        return ispyb_persons

    def get_ispyb_laboratories(self):
        laboratories = self.session.query(
            models.Laboratory.laboratoryId,
            models.Laboratory.laboratoryExtPk,
            models.Laboratory.name,
            models.Laboratory.address,
            models.Laboratory.city,
            models.Laboratory.country,
        )
        ispyb_laboratories = [p._asdict() for p in laboratories.all()]
        return ispyb_laboratories

    @timed
    def process_proposal(
        self, sourceProposal: dict[str, Any], sourcePerson: dict[str, Any]
    ):
        # First check to update proposal existing in the DB
        to_add_proposal = self.check_proposal(sourceProposal, sourcePerson)
        if to_add_proposal:
            self.add_proposal(sourceProposal, sourcePerson)

    def check_proposal(
        self, sourceProposal: dict[str, Any], sourceProposer: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the proposal if it needed and exists on the DB"""
        target_proposals = self.get_ispyb_proposals()
        to_add_proposal = []
        if target_proposals:
            for tar in target_proposals:
                # Iterate over all the target proposals
                # Check if the Proposal already exist in the DB by comparing against the proposalCode and proposalNumber
                if (
                    tar["proposalCode"] is not None
                    and tar["proposalCode"] == sourceProposal["proposalCode"]
                ) and (
                    tar["proposalNumber"] is not None
                    and tar["proposalNumber"] == sourceProposal["proposalNumber"]
                ):
                    update = False
                    # Check which Proposal values should we inspect to see if they changed
                    for k in ["title"]:
                        if tar[k] != sourceProposal[k]:
                            logger.debug(
                                f"Field {k} to update for proposal {tar['proposalId']}"
                            )
                            update = True

                    if update:
                        # Update the existing proposal with new values
                        logger.debug(f"Updating proposal {tar['proposalId']}")
                        self.update_proposal(tar["proposalId"], sourceProposal)
                    break
                else:
                    # New proposal to be added
                    to_add_proposal.append(sourceProposal)
        else:
            to_add_proposal.append(sourceProposal)
        return to_add_proposal

    def add_proposal(
        self, sourceProposal: dict[str, Any], sourceProposer: dict[str, Any]
    ):
        """Add a new proposal."""
        pers = (
            self.session.query(models.Person)
            .filter(models.Person.siteId == sourceProposer["siteId"])
            .first()
        )
        proposal = models.Proposal(**sourceProposal)
        proposal.personId = pers.personId
        self.session.add(proposal)
        # Flush to get the new proposalId
        self.session.flush()
        # Set the proposalId to be used to link other entities (sessions, proteins, etc)
        self.proposalId = proposal.proposalId
        return proposal.proposalId

    def update_proposal(
        self, proposalId: int, sourceProposal: dict[str, Any]
    ) -> models.Proposal:
        """Updates a Proposal entity."""
        prop = (
            self.session.query(models.Proposal)
            .filter(models.Proposal.proposalId == proposalId)
            .first()
        )
        if prop:
            prop.title = sourceProposal["title"]
            # Do not update the proposal until the commit is done
            self.session.flush()
        return prop

    def update_laboratory(
        self, laboratoryId: int, sourceLaboratory: dict[str, Any]
    ) -> models.Laboratory:
        """Updates a Laboratory entity."""
        lab = (
            self.session.query(models.Laboratory)
            .filter(models.Laboratory.laboratoryId == laboratoryId)
            .first()
        )
        if lab:
            lab.name = sourceLaboratory["name"]
            lab.address = sourceLaboratory["address"]
            lab.city = sourceLaboratory["city"]
            lab.country = sourceLaboratory["country"]
            # Do not update the laboratory until the commit is done
            self.session.flush()
        return lab

    def update_person(
        self, personId: int, sourcePerson: dict[str, Any]
    ) -> models.Person:
        """Updates a Person entity."""
        pers = (
            self.session.query(models.Person)
            .options(joinedload(models.Person.Laboratory))
            .filter(models.Person.personId == personId)
            .first()
        )

        if pers:
            pers.givenName = sourcePerson["givenName"]
            pers.familyName = sourcePerson["familyName"]
            pers.emailAddress = sourcePerson["emailAddress"]
            pers.phoneNumber = sourcePerson["phoneNumber"]
            # Do not update the person until the commit is done
            self.session.flush()
        return pers

    def add_person(self, sourcePerson: dict[str, Any], laboratoryId=None) -> int:
        """Add a new person together with relation to a laboratory if passed."""
        if laboratoryId:
            sourcePerson["laboratoryId"] = laboratoryId
        person = models.Person(**sourcePerson)
        self.session.add(person)
        # Flush to get the new personId
        self.session.flush()
        return person.personId

    def add_laboratory(self, sourceLaboratory: dict[str, Any]) -> int:
        """Add a new laboratory."""
        laboratory = models.Laboratory(**sourceLaboratory)
        self.session.add(laboratory)
        # Flush to get the new laboratoryId
        self.session.flush()
        return laboratory.laboratoryId

    @timed
    def process_persons(self, sourcePersons: dict[str, Any]):
        """Process the creation or update of Persons"""
        # First check to update persons existing in the DB
        to_add_persons = self.check_persons(sourcePersons)
        # Second add new persons
        self.create_persons(to_add_persons)

    def create_persons(self, sourcePersons: dict[str, Any]):
        """Process the creation of Persons"""
        for new_person in sourcePersons:
            # Add a new person
            src_lab = new_person.pop("laboratory")
            target_laboratories = self.get_ispyb_laboratories()
            # Check if the laboratory attached to the Person is in ISPyB
            for tar_lab in target_laboratories:
                if (
                    tar_lab["laboratoryExtPk"] is not None
                    and tar_lab["laboratoryExtPk"] == src_lab["laboratoryExtPk"]
                ):
                    update = False
                    laboratory_id = tar_lab["laboratoryId"]
                    # Check which laboratory values should we check to see if they changed
                    for k in ["name", "address", "city", "country"]:
                        if tar_lab[k] != src_lab[k]:
                            logger.debug(
                                f"Field {k} to update for laboratory {laboratory_id}"
                            )
                            update = True

                    if update:
                        # Update the existing laboratory with new values
                        logger.debug(f"Updating {tar_lab['laboratoryId']}")
                        self.update_laboratory(tar_lab["laboratoryId"], src_lab)

                    break

            else:
                # New laboratory to add
                laboratory_id = self.add_laboratory(src_lab)

            self.add_person(new_person, laboratory_id)

    def check_persons(self, sourcePersons) -> dict[str, Any]:
        """Updates person entities if needed and returns only the new ones to be added."""
        target_persons = self.get_ispyb_persons()
        to_add_persons = []
        for src in sourcePersons:
            # Iterate over all the source persons
            for tar in target_persons:
                # Iterate over all the target persons
                # Check if the Person already exist in the DB by comparing against the siteId or login
                if (tar["siteId"] is not None and tar["siteId"] == src["siteId"]) or (
                    tar["login"] is not None and tar["login"] == src["login"]
                ):
                    update = False
                    # Check which Person values should we inspect to see if they changed
                    for k in ["givenName", "familyName", "emailAddress", "phoneNumber"]:
                        if tar[k] != src[k]:
                            logger.debug(
                                f"Field {k} to update for person {tar['personId']}"
                            )
                            update = True

                    if update:
                        # Update the existing person with new values
                        logger.debug(f"Updating person {tar['personId']}")
                        self.update_person(tar["personId"], src)
                    # Check if the person laboratory has changed
                    self.update_person_laboratory(tar["personId"], src)
                    break
            else:
                # New persons to be added
                to_add_persons.append(src)
        return to_add_persons

    def update_person_laboratory(self, personId: int, sourcePerson: dict[str, Any]):
        """Updates person relation to a laboratory if needed.
        Logic is based on the laboratoryExtPk (User Portal laboratory/institution entity ID)
        """
        person = (
            self.session.query(models.Person)
            .options(joinedload(models.Person.Laboratory))
            .filter(models.Person.personId == personId)
            .first()
        )
        src_lab = sourcePerson.pop("laboratory")
        if person.Laboratory.laboratoryExtPk != src_lab["laboratoryExtPk"]:
            logger.debug(f"Updating Laboratory for {personId}")
            # Check if source laboratoryExtPk exists already in ISPyB
            laboratory = (
                self.session.query(models.Laboratory)
                .filter(models.Laboratory.laboratoryExtPk == src_lab["laboratoryExtPk"])
                .first()
            )
            if laboratory:
                # Update person link to laboratory
                logger.debug(f"Updating LaboratoryId for {personId}")
                person.laboratoryId = laboratory.laboratoryId
                self.session.flush()
            else:
                # Add new laboratory a link it to person
                logger.debug(f"Creating and linking a new Laboratory for {personId}")
                laboratory_id = self.add_laboratory(src_lab)
                person.laboratoryId = laboratory_id
                self.session.flush()
