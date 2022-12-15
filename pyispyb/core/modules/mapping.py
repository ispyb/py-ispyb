import io
import gzip
import json

import matplotlib as mpl
import matplotlib.cm as cm
import numpy as np
from PIL import Image
from sqlalchemy import func
from sqlalchemy.orm import joinedload
from ispyb import models

from ...config import settings
from ...app.extensions.database.definitions import with_authorization
from ...app.extensions.database.utils import Paged, page, with_metadata
from ...app.extensions.database.middleware import db
from ..schemas import mapping as schema


def get_maps(
    skip: int,
    limit: int,
    xrfFluorescenceMappingId: int = None,
    dataCollectionId: int = None,
    blSampleId: int = None,
    withAuthorization: bool = True,
) -> Paged[models.XRFFluorescenceMapping]:
    metadata = {
        "url": func.concat(
            f"{settings.api_root}/mapping/",
            models.XRFFluorescenceMapping.xrfFluorescenceMappingId,
        ),
        "blSubSampleId": models.DataCollection.blSubSampleId,
        "blSampleId": models.DataCollectionGroup.blSampleId,
    }

    query = (
        db.session.query(models.XRFFluorescenceMapping, *metadata.values())
        .join(models.XRFFluorescenceMappingROI)
        .options(joinedload(models.XRFFluorescenceMapping.XRFFluorescenceMappingROI))
        .join(models.GridInfo)
        .options(joinedload(models.XRFFluorescenceMapping.GridInfo))
        .join(models.DataCollection)
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
        .group_by(models.XRFFluorescenceMapping.xrfFluorescenceMappingId)
        .order_by(models.XRFFluorescenceMapping.xrfFluorescenceMappingId)
    )

    if xrfFluorescenceMappingId:
        query = query.filter(
            models.XRFFluorescenceMapping.xrfFluorescenceMappingId
            == xrfFluorescenceMappingId
        )

    if dataCollectionId:
        query = query.filter(models.DataCollection.dataCollectionId == dataCollectionId)

    if blSampleId:
        query = query.filter(models.DataCollectionGroup.blSampleId == blSampleId)

    if withAuthorization:
        query = with_authorization(query, joinBLSession=False)

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = with_metadata(query.all(), list(metadata.keys()))

    return Paged(total=total, results=results, skip=skip, limit=limit)


def get_map_rois(
    skip: int,
    limit: int,
    xrfFluorescenceMappingROIId: int,
    blSampleId: int = None,
    withAuthorization: bool = True,
) -> Paged[models.XRFFluorescenceMappingROI]:
    query = (
        db.session.query(models.XRFFluorescenceMappingROI)
        .join(models.BLSample)
        .join(models.Crystal)
        .join(models.Protein)
        .join(models.Proposal)
        .group_by(models.XRFFluorescenceMappingROI.xrfFluorescenceMappingROIId)
        .order_by(models.XRFFluorescenceMappingROI.xrfFluorescenceMappingROIId)
    )

    if xrfFluorescenceMappingROIId:
        query = query.filter(
            models.XRFFluorescenceMappingROI.xrfFluorescenceMappingROIId
            == xrfFluorescenceMappingROIId
        )

    if blSampleId:
        query = query.filter(models.DataCollectionGroup.blSampleId == blSampleId)

    if withAuthorization:
        query = with_authorization(query)

    total = query.count()
    query = page(query, skip=skip, limit=limit)
    results = query.all()

    return Paged(total=total, results=results, skip=skip, limit=limit)


def shape_map(map_: schema.Map) -> np.ndarray:
    """Shapes a 1d map array into the correct 2d image

    Reorders the data if needbe for snaked collection
    Reshapes if the data was collected vertically

    Returns:
        data (ndarray): The XRF map data
    """
    if map_.dataFormat == "json+gzip":
        data = gunzip_json(map_.data)
        data = np.array(data)
    else:
        data = np.array(map_.data)

    # TODO: Catch raise
    if map_.GridInfo.orientation == "vertical":
        data = data.reshape(int(map_.GridInfo.steps_x), int(map_.GridInfo.steps_y))
        data = np.rot90(data)
        data = np.flipud(data)
    else:
        data = data.reshape(int(map_.GridInfo.steps_y), int(map_.GridInfo.steps_x))

    # For snaked collection every other row is reversed
    if map_.GridInfo.snaked:
        data[1::2, :] = data[1::2, ::-1]

    return data


def generate_map_image(map_: schema.Map, image_format: str = "PNG") -> io.BytesIO:
    """Generates a PIL Image from an XRF map

    -1 placeholder values are converted to a transparent pixel

    Returns:
        image (io.Bytes): Bytes of PIL Image
    """
    data = shape_map(map_)
    norm = mpl.colors.Normalize(vmin=map_.min, vmax=map_.max)

    colourmap = map_.colourMap or "viridis"
    if not hasattr(cm, colourmap):
        colourmap = "viridis"

    cmap = getattr(cm, colourmap or "viridis")

    m = cm.ScalarMappable(norm=norm, cmap=cmap)
    img_data = m.to_rgba(data, bytes=True, alpha=map_.opacity)

    mask = data == -1
    img_data[mask, :] = [255, 255, 255, 0]

    image = Image.fromarray(img_data, "RGBA")
    img_io = io.BytesIO()
    image.save(img_io, image_format, quality=100)
    img_io.seek(0)

    return img_io


def generate_histogram(map_):
    """Generates a histogram of map data

    Args:
        map_(dict): An XRF map from the metadata handler

    Returns:
        data: (dict(list)): The histogram, bins, and widths
    """
    data = shape_map(map_)
    ndata = np.array(data)
    rdata = np.where(ndata == -1, 0, ndata)

    try:
        hist, bins = np.histogram(rdata, bins=50)
        center = (bins[:-1] + bins[1:]) / 2
        width = np.diff(bins)

    # TODO: This should not happen
    except (OverflowError, ValueError):
        hist = []
        center = []
        width = []

    return {
        "xrfFluorescenceMappingId": map_.xrfFluorescenceMappingId,
        "hist": hist.tolist(),
        "bins": center.tolist(),
        "width": width.tolist(),
    }


def gunzip_json(bytes_obj: str):
    """Un gzips a bytes object and load into json

    Returns:
        data(dict): The decoded json as a python object
    """
    if not bytes_obj:
        return []

    in_ = io.BytesIO()
    in_.write(bytes_obj)
    in_.seek(0)
    with gzip.GzipFile(fileobj=in_, mode="rb") as fo:
        gunzipped_bytes_obj = fo.read()

    return json.loads(gunzipped_bytes_obj.decode())
