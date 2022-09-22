import os
from typing import Any, Optional

from sqlalchemy import func
from ispyb import models

from ...app.extensions.database.definitions import (
    with_beamline_groups,
)
from ...app.extensions.database.utils import Paged, page, with_metadata
from ...app.extensions.database.middleware import db
from .events import get_events
from ...config import settings


def get_datacollection_snapshot_path(
    dataCollectionId: int, imageId: int = 1, snapshot: bool = False
) -> Optional[str]:
    datacollections = get_events(dataCollectionId=dataCollectionId, skip=0, limit=1)
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

    if os.path.exists(image_path):
        return image_path

    return None


def get_datacollection_attachments(
    skip: int,
    limit: int,
    dataCollectionId: Optional[int] = None,
    dataCollectionFileAttachmentId: Optional[int] = None,
    beamlineGroups: Optional[dict[str, Any]] = None,
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
    )

    if dataCollectionId:
        query = query.filter(
            models.DataCollectionFileAttachment.dataCollectionId == dataCollectionId
        )

    if dataCollectionFileAttachmentId:
        query = query.filter(
            models.DataCollectionFileAttachment.dataCollectionFileAttachmentId
            == dataCollectionFileAttachmentId
        )

    if beamlineGroups:
        query = with_beamline_groups(query, beamlineGroups, joinBLSession=False)

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))

    for result in results:
        result._metadata["fileName"] = os.path.basename(result.fileFullPath)

    return Paged(total=total, results=results, skip=skip, limit=limit)
