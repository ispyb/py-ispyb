select
    Movie.micrographSnapshotFullPath as movie_thumbnail,
    MotionCorrection.micrographSnapshotFullPath as motion_correction_thumbnail,
    MotionCorrection.driftPlotFullPath as motion_correction_drift,
    CTF.spectraImageThumbnailFullPath as ctf_thumbnail
from
    Movie,
    MotionCorrection,
    CTF,
    DataCollection,
    DataCollectionGroup,
    BLSession
WHERE
    Movie.movieId = :movieId
    and Movie.dataCollectionId = DataCollection.dataCollectionId
    and DataCollection.dataCollectionGroupId = DataCollectionGroup.dataCollectionGroupId
    and DataCollectionGroup.sessionId = BLSession.sessionId
    and BLSession.proposalId = :proposalId
    and MotionCorrection.movieId = Movie.movieId
    and CTF.motionCorrectionId = MotionCorrection.motionCorrectionId