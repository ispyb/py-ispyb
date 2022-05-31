import copy
import logging
import time
from typing import Any
from datetime import datetime, timezone
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
    # Using the same sqlalchemy engine from pyispyb.app.extensions.database.session
    # Creating a different Session since nothing should be committed until the end of the UserPortalSync process
    # session.flush is used everywhere to get new auto-increment IDs
    session = Session(engine)

    # Initialize UserPortalSync class
    user_portal_sync = UserPortalSync(session)

    # Get full proposal dict
    full_dict = proposal.dict()
    # Get source entity dicts
    source_proposal = full_dict.pop("proposal")
    source_proposal_persons = source_proposal.pop("persons")
    source_sessions = full_dict.pop("sessions")
    source_proteins = full_dict.pop("proteins")

    try:
        # Process the proposal Persons
        user_portal_sync.process_persons(source_proposal_persons, "proposal")
        # At this point all Person/Laboratory entities related to the proposal have been either updated or created

        # Process the Proposal
        # The first Person in the list will be the one having the relation to the proposal table
        user_portal_sync.process_proposal(source_proposal, source_proposal_persons[0])
        # At this point the Proposal entity has been either updated or created, and we have a proposalID

        # Process sessions
        user_portal_sync.process_sessions(source_sessions)

        # Process proteins
        user_portal_sync.process_proteins(source_proteins)

        session.commit()
    except Exception as e:
        logger.debug(f"sync_proposal exception: {e}")
        session.rollback()
    finally:
        session.close()
    took = round(time.time() - start, 3)
    return took


class UserPortalSync(object):
    def __init__(self, session):
        self.session = session
        self.proposalId = None
        # List of persons to be checked/added to ProposalHasPerson table
        self.proposal_person_ids = []
        # List of persons to be checked/added to Session_has_Person table
        self.session_person_ids = []
        # Dict of sessionIds with related personIds to be checked/added to Session_has_Person table
        self.session_ids = {}

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
        # Second add/update here the relations between proposalId and personId (proposalHasPerson)
        self.process_proposal_has_person()

    def process_proposal_has_person(self):
        # First check the entry in ProposalHasPerson does not exist already in DB
        # if that is the case create it
        for personId in self.proposal_person_ids:
            proposal_person = (
                self.session.query(models.ProposalHasPerson)
                .filter(models.ProposalHasPerson.personId == personId)
                .filter(models.ProposalHasPerson.proposalId == self.proposalId)
                .first()
            )
            if not proposal_person:
                # Add the relation
                proposal_has_person = models.ProposalHasPerson(
                    personId=personId, proposalId=self.proposalId
                )
                self.session.add(proposal_has_person)
                # Flush to get the new proposalId
                self.session.flush()
                logger.debug(
                    f"ProposalHasPerson with proposalId {self.proposalId} and {personId} added in DB"
                )
            else:
                logger.debug(
                    f"ProposalHasPerson with proposalId {self.proposalId} and {personId} already in DB"
                )

    def check_proposal(
        self, sourceProposal: dict[str, Any], sourceProposer: dict[str, Any]
    ) -> dict[str, Any]:
        """Updates the proposal if it needed and exists on the DB"""
        target_proposals = self.get_ispyb_proposals()
        to_add_proposal = []
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
                logger.debug(
                    f"Proposal with code {tar['proposalCode']}{tar['proposalNumber']} found in DB with proposalId {tar['proposalId']}"
                )
                # Set the proposalId to be used to link other entities (sessions, proteins, etc)
                self.proposalId = tar["proposalId"]
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
        logger.debug(
            f"Proposal with code {proposal.proposalCode}{proposal.proposalNumber}"
            f"does not exist. Creating it"
        )
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

    def add_person(
        self, sourcePerson: dict[str, Any], laboratoryId=None, person_type: str = None
    ) -> int:
        """Add a new person together with relation to a laboratory if passed."""
        # Make a deep copy to session_options original values from self.session_ids, so they are not removed
        copy_source_person = copy.deepcopy(sourcePerson)
        if person_type == "session":
            if copy_source_person["session_options"]:
                copy_source_person.pop("session_options")
        else:
            # session_options always None for Person related to Proposal, so it can be removed
            del copy_source_person["session_options"]
        if laboratoryId:
            copy_source_person["laboratoryId"] = laboratoryId
        person = models.Person(**copy_source_person)
        self.session.add(person)
        # Flush to get the new personId
        self.session.flush()
        # Add the personId to a list to be used later to create the relation to proposalHasPerson/Session_has_Person
        if person_type == "proposal":
            self.proposal_person_ids.append(person.personId)
        elif person_type == "session":
            person_ids = dict()
            person_ids["personId"] = person.personId
            person_ids["login"] = person.login
            person_ids["siteId"] = person.siteId
            self.session_person_ids.append(person_ids)
        return person.personId

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

    def add_laboratory(self, sourceLaboratory: dict[str, Any]) -> int:
        """Add a new laboratory."""
        laboratory = models.Laboratory(**sourceLaboratory)
        self.session.add(laboratory)
        # Flush to get the new laboratoryId
        self.session.flush()
        return laboratory.laboratoryId

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

    @timed
    def process_persons(self, sourcePersons: dict[str, Any], person_type: str = None):
        """Process the creation or update of Persons"""
        # First check to update persons existing in the DB
        to_add_persons = self.check_persons(sourcePersons, person_type)
        # Second add new persons
        if to_add_persons:
            self.create_persons(to_add_persons, person_type)

    def create_persons(self, sourcePersons: dict[str, Any], person_type: str = None):
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
                ) or (
                    tar_lab["name"] == src_lab["name"]
                    and tar_lab["city"] == src_lab["city"]
                    and tar_lab["country"] == src_lab["country"]
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

            self.add_person(new_person, laboratory_id, person_type)

    def check_persons(self, sourcePersons, person_type: str = None) -> dict[str, Any]:
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
                    logger.debug(
                        f"Person with personId {tar['personId']} already in DB"
                    )

                    if person_type == "proposal":
                        # Add personId to proposal_person_ids list
                        self.proposal_person_ids.append(tar["personId"])
                    elif person_type == "session":
                        person_ids = {}
                        # Add personids to session_person_ids list
                        person_ids["personId"] = tar["personId"]
                        person_ids["login"] = tar["login"]
                        person_ids["siteId"] = tar["siteId"]
                        self.session_person_ids.append(person_ids)
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

    @timed
    def process_proteins(self, sourceProteins: dict[str, Any]):
        """Process the creation or update of Proteins"""
        # Check if proteins exist the DB
        self.check_proteins(sourceProteins)

    def check_proteins(self, sourceProteins):
        """Check Protein entities to see if they exist already, if not it creates a new one."""
        for protein in sourceProteins:
            prot = (
                self.session.query(models.Protein)
                .filter(models.Protein.proposalId == self.proposalId)
                .filter(models.Protein.acronym == protein["acronym"])
                .first()
            )
            if not prot:
                logger.debug(
                    f"Protein with acronym {protein['acronym']} "
                    f"for Proposal {self.proposalId} does not exist. Creating it"
                )
                self.add_protein(protein)
            else:
                # If there is not any macromolecule with that acronym
                # and proposalId then it will be created
                logger.debug(
                    f"Protein with acronym {protein['acronym']} found in DB for proposalId {self.proposalId}"
                )
                del protein["person"]
                self.session.query(models.Protein).filter(
                    models.Protein.proposalId == self.proposalId
                ).filter(models.Protein.acronym == protein["acronym"]).update(protein)
                self.session.flush()

    def add_protein(self, sourceProtein) -> int:
        """Add a new Protein.
        Here we assume the person related to the protein will be always a proposal participant
        meaning the person is already on the DB or pending to be commited
        """
        pers = (
            self.session.query(models.Person)
            .options(joinedload(models.Person.Laboratory))
            .filter(models.Person.siteId == sourceProtein["person"]["siteId"])
            .first()
        )
        if pers:
            """Add a new protein."""
            del sourceProtein["person"]
            protein = models.Protein(**sourceProtein)
            protein.proposalId = self.proposalId
            protein.personId = pers.personId
            self.session.add(protein)
            # Flush to get the new proteinId
            self.session.flush()
            return protein.proteinId

    @timed
    def process_sessions(self, sourceSessions: dict[str, Any]):
        """Process the creation or update of Sessions"""
        # First process the sessions
        self.check_sessions(sourceSessions)
        # Second process the relation between sessions and persons (Session_has_Person)
        self.process_session_has_person()

    def process_session_has_person(self):
        # Iterate over all the session_ids
        for session_id in self.session_ids:
            self.session_person_ids = []
            # Create/Update new persons if needed first
            self.process_persons(self.session_ids[session_id], "session")
            # Check if the entry in Session_has_Person does not exist already in DB
            for dict_person in self.session_person_ids:
                session_person = (
                    self.session.query(models.SessionHasPerson)
                    .filter(models.SessionHasPerson.sessionId == session_id)
                    .filter(models.SessionHasPerson.personId == dict_person["personId"])
                    .first()
                )

                role = None
                remote = 0
                person_found_in_session = None
                for p in self.session_ids[session_id]:
                    if (
                        p["login"] == dict_person["login"]
                        or p["siteId"] == dict_person["siteId"]
                    ):
                        person_found_in_session = p
                        break

                try:
                    # Get the session options (role, remote)
                    session_options = person_found_in_session["session_options"]
                    if session_options:
                        if session_options["role"]:
                            role = session_options["role"]
                        if session_options["remote"]:
                            remote = session_options["remote"]
                except KeyError as e:
                    logger.debug(f"session_options not found for : {e}")

                if not session_person:
                    # Add the relation between sessionId and personId
                    session_has_person = models.SessionHasPerson(
                        sessionId=session_id,
                        personId=dict_person["personId"],
                        role=role,
                        remote=remote,
                    )
                    self.session.add(session_has_person)
                    self.session.flush()
                    logger.debug(
                        f"Session_has_Person with sessionId {session_id} and personId {dict_person['personId']} added in DB"
                    )
                else:
                    # Update the Session_has_Person relation with the JSON values
                    self.session.query(models.SessionHasPerson).filter(
                        models.SessionHasPerson.personId == dict_person["personId"]
                    ).filter(models.SessionHasPerson.sessionId == session_id).update(
                        {"role": role, "remote": remote}
                    )
                    self.session.flush()
                    logger.debug(
                        f"Session_has_Person with sessionId {session_id} and personId {dict_person['personId']} already in DB"
                    )

    def check_sessions(self, sourceSessions):
        """Check Session entities to see if they exist already, if not it creates a new one."""
        for session in sourceSessions:
            # Get the session persons
            session_persons = session.pop("persons")
            # Check first if session is already on DB
            sess = (
                self.session.query(models.BLSession)
                .filter(models.BLSession.proposalId == self.proposalId)
                .filter(models.BLSession.expSessionPk == session["expSessionPk"])
                .first()
            )
            if not sess:
                # Creates the session if it does not exist
                logger.debug(
                    f"Session with expSessionPk {session['expSessionPk']} "
                    f"for Proposal {self.proposalId} does not exist. Creating it"
                )
                sessionId = self.add_session(session)
                # Set the new session id with the related session persons
                self.session_ids[sessionId] = session_persons
            else:
                # if the session already exist we just update all the values
                logger.debug(
                    f"Session with expSessionPk {session['expSessionPk']} found in DB for proposalId {self.proposalId}"
                )
                self.session.query(models.BLSession).filter(
                    models.BLSession.proposalId == self.proposalId
                ).filter(
                    models.BLSession.expSessionPk == session["expSessionPk"]
                ).update(
                    session
                )
                self.session.flush()
                # Set the session id with the related session persons
                self.session_ids[sess.sessionId] = session_persons

    def add_session(self, sourceSession) -> int:
        """Add a new Session"""
        if not sourceSession["lastUpdate"]:
            """
            When adding a new session, if lastUpdate is not present, set as now()
            Needed for backward compatibility with the Java API, since it does not
            like lastUpdate = 0000-00-00 00:00:00
            """
            now = datetime.now()
            now = now.replace(tzinfo=timezone.utc)
            sourceSession["lastUpdate"] = now
        session = models.BLSession(**sourceSession)
        session.proposalId = self.proposalId
        self.session.add(session)
        # Flush to get the new sessionId
        self.session.flush()
        return session.sessionId
