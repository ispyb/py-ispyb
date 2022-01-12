select
    (
        select
            count(*)
        from
            BLSession,
            Session_has_Person,
            Person
        where
            BLSession.sessionId = :sessionId
            and BLSession.sessionId = Session_has_Person.sessionId
            and Person.personId = Session_has_Person.personId
            and Person.login = :login
    ) + (
        select
            count(*)
        from
            BLSession,
            Proposal,
            Person
        where
            BLSession.sessionId = :sessionId
            and Proposal.proposalId = BLSession.proposalId
            and Person.personId = Proposal.personId
            and Person.login = :login
    ) as isAuthorized