import logging
import os

from ispyb import models

from ...app.extensions.database.definitions import (
    with_authorization,
)
from ...app.extensions.database.utils import Paged, page
from ...app.extensions.database.middleware import db
from ..schemas import em as schema

logger = logging.getLogger(__name__)


def get_micrograph_snapshot_path(movieId: int) -> str:
    query = (
        db.session.query(models.MotionCorrection.micrographSnapshotFullPath)
        .filter(models.MotionCorrection.movieId == movieId)
        .join(models.DataCollection)
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
    )

    query = with_authorization(query, joinBLSession=False)
    path = query.scalar()

    if path:
        if os.path.exists(path):
            return path
        logger.warning(
            f"Micrograph image {path} for movie {movieId} does not exist on disk"
        )
    return None


def get_fft_thumbnail_path(movieId: int) -> str:
    query = (
        db.session.query(models.CTF.fftTheoreticalFullPath)
        .select_from(models.MotionCorrection)
        .filter(models.MotionCorrection.movieId == movieId)
        .join(models.CTF)
        .join(models.DataCollection)
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
    )

    query = with_authorization(query, joinBLSession=False)
    path = query.scalar()

    if path:
        if os.path.exists(path):
            return path
        logger.warning(
            f"Micrograph image {path} for movie {movieId} does not exist on disk"
        )
    return None


def get_movies(skip: int, limit: int, dataCollectionId: int) -> Paged[schema.FullMovie]:
    query = (
        db.session.query(models.MotionCorrection, models.CTF, models.Movie)
        .join(
            models.MotionCorrection,
            models.MotionCorrection.movieId == models.Movie.movieId,
        )
        .join(models.CTF)
        .join(
            models.DataCollection,
            models.DataCollection.dataCollectionId
            == models.MotionCorrection.dataCollectionId,
        )
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
        .order_by(models.MotionCorrection.imageNumber)
        .group_by(models.Movie.movieId)
    )

    if dataCollectionId:
        query = query.filter(models.Movie.dataCollectionId == dataCollectionId)

    total = query.count()
    query = with_authorization(query, joinBLSession=False)
    query = page(query, skip=skip, limit=limit)
    results = query.all()

    return Paged(total=total, results=results, skip=skip, limit=limit)
