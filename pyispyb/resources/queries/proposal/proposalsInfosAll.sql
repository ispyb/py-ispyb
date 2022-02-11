select
    distinct p.proposalId as Proposal_proposalId,
    p.proposalType as Proposal_proposalType,
    p.personId as Proposal_personId,
    p.title as Proposal_title,
    p.proposalCode as Proposal_proposalCode,
    p.proposalNumber as Proposal_proposalNumber
from
    Proposal as p;