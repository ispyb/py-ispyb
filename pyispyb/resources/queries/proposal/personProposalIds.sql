select
    proposalId
from
    Proposal,
    Person
where
    Proposal.personId = Person.personId
    and Person.login = :login;