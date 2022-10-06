import logging
import os
from typing import Any, Optional

from sqlalchemy import func
from ispyb import models

from ...app.extensions.database.definitions import (
    with_authorization,
)
from ...app.extensions.database.utils import Paged, page, with_metadata
from ...app.extensions.database.middleware import db
from .events import get_events
from ..schemas import datacollections as schema
from ...config import settings

logger = logging.getLogger(__name__)


def get_datacollection_diffraction_image_path(
    dataCollectionId: int,
    snapshot: bool = False,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> Optional[str]:
    query = (
        db.session.query(
            (
                models.Image.jpegThumbnailFileFullPath
                if snapshot
                else models.Image.jpegFileFullPath
            ).label("imagePath")
        )
        .filter(models.Image.imageNumber == 1)
        .filter(models.Image.dataCollectionId == dataCollectionId)
        .join(models.DataCollection)
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
    )

    query = with_authorization(query, beamLineGroups, joinBLSession=False)
    first_image = query.first()

    if first_image:
        return first_image.imagePath


def get_datacollection_snapshot_path(
    dataCollectionId: int,
    imageId: int = 1,
    snapshot: bool = False,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> Optional[str]:
    datacollections = get_events(
        dataCollectionId=dataCollectionId,
        beamLineGroups=beamLineGroups,
        skip=0,
        limit=1,
    )
    try:
        dc = datacollections.first["Item"]
    except IndexError:
        return None

    images = [
        "xtalSnapshotFullPath1",
        "xtalSnapshotFullPath2",
        "xtalSnapshotFullPath3",
        "xtalSnapshotFullPath4",
    ]

    image_path: str = getattr(dc, images[imageId - 1])
    if image_path is None:
        return None

    if snapshot:
        ext = os.path.splitext(image_path)[1][1:].strip()
        image_path = image_path.replace(f".{ext}", f"t.{ext}")

    if settings.path_map:
        image_path = settings.path_map + image_path

    if not os.path.exists(image_path):
        logger.warning(
            f"{images[imageId - 1]} [{image_path}] for dataCollectionId {dataCollectionId} does not exist on disk"
        )
        return None

    return image_path


def get_datacollection_attachments(
    skip: int,
    limit: int,
    dataCollectionId: Optional[int] = None,
    dataCollectionGroupId: Optional[int] = None,
    dataCollectionFileAttachmentId: Optional[int] = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> Paged[models.DataCollectionFileAttachment]:
    metadata = {
        "url": func.concat(
            f"{settings.api_root}/datacollections/attachments/",
            models.DataCollectionFileAttachment.dataCollectionFileAttachmentId,
        )
    }

    query = (
        db.session.query(models.DataCollectionFileAttachment, *metadata.values())
        .join(models.DataCollection)
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
        .group_by(models.DataCollectionFileAttachment.dataCollectionFileAttachmentId)
    )

    if dataCollectionId:
        query = query.filter(
            models.DataCollectionFileAttachment.dataCollectionId == dataCollectionId
        )

    if dataCollectionGroupId:
        query = query.filter(
            models.DataCollectionGroup.dataCollectionGroupId == dataCollectionGroupId
        )

    if dataCollectionFileAttachmentId:
        query = query.filter(
            models.DataCollectionFileAttachment.dataCollectionFileAttachmentId
            == dataCollectionFileAttachmentId
        )

    if beamLineGroups:
        query = with_authorization(query, beamLineGroups, joinBLSession=False)

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))

    for result in results:
        result._metadata["fileName"] = os.path.basename(result.fileFullPath)

    return Paged(total=total, results=results, skip=skip, limit=limit)


def get_per_image_analysis(
    skip: int,
    limit: int,
    dataCollectionId: Optional[int] = None,
    dataCollectionGroupId: Optional[int] = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> Paged[schema.PerImageAnalysis]:
    query = (
        db.session.query(
            models.ImageQualityIndicators.imageNumber,
            models.ImageQualityIndicators.totalIntegratedSignal,
            models.ImageQualityIndicators.method2Res,
            models.ImageQualityIndicators.goodBraggCandidates,
        )
        .join(
            models.DataCollection,
            models.ImageQualityIndicators.dataCollectionId
            == models.DataCollection.dataCollectionId,
        )
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
    )

    if dataCollectionId:
        query = query.filter(models.DataCollection.dataCollectionId == dataCollectionId)

    if dataCollectionGroupId:
        query = query.filter(
            models.DataCollectionGroup.dataCollectionGroupId == dataCollectionGroupId
        )

    query = with_authorization(query, beamLineGroups, joinBLSession=False)
    query = page(query, skip=skip, limit=limit)
    total = query.count()

    results = {"dataCollectionId": dataCollectionId}
    for row in [r._asdict() for r in query.all()]:
        for key in [
            "imageNumber",
            "totalIntegratedSignal",
            "method2Res",
            "goodBraggCandidates",
        ]:
            if key not in results:
                results[key] = []
            results[key].append(row[key])

    return Paged(total=total, results=[results], skip=skip, limit=limit)
