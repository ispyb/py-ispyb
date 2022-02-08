select
    proposalId
from
    Proposal
where
    proposalId = :name
    or UPPER(concat(proposalCode, proposalNumber)) = UPPER(:name)