select
    (
        select
            count(*)
        from
            Proposal,
            ProposalHasPerson,
            Person
        where
            Proposal.proposalId = :proposalId
            and Proposal.proposalId = ProposalHasPerson.proposalId
            and Person.personId = ProposalHasPerson.personId
            and Person.login = :login
    ) + (
        select
            count(*)
        from
            Proposal,
            Person
        where
            Proposal.proposalId = :proposalId
            and Person.personId = Proposal.personId
            and Person.login = :login
    ) as is_authorized