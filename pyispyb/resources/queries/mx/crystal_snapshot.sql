select
    DataCollection.xtalSnapshotFullPath1,
    DataCollection.xtalSnapshotFullPath2,
    DataCollection.xtalSnapshotFullPath3,
    DataCollection.xtalSnapshotFullPath4
from
    DataCollection,
    DataCollectionGroup,
    BLSession
WHERE
    DataCollection.dataCollectionId = :dataCollectionId
    and DataCollection.dataCollectionGroupId = DataCollectionGroup.dataCollectionGroupId
    and DataCollectionGroup.sessionId = BLSession.sessionId
    and BLSession.proposalId = :proposalId