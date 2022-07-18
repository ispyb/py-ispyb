select
    distinct p.proposalId as Proposal_proposalId,
    p.proposalType as Proposal_proposalType,
    p.personId as Proposal_personId,
    p.title as Proposal_title,
    p.proposalCode as Proposal_proposalCode,
    p.proposalNumber as Proposal_proposalNumber
from
    (
        select
            Proposal.*
        from
            Proposal,
            Person
        where
            Proposal.personId = Person.personId
            and Person.login = :login
        union
        select
            Proposal.*
        from
            Proposal,
            Person,
            BLSession,
            Session_has_Person
        where
            Person.login = :login
            and Session_has_Person.personId = Person.personId
            and BLSession.sessionId = Session_has_Person.sessionId
            and Proposal.proposalId = BLSession.proposalId
    ) as p