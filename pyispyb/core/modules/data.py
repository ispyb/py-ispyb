import logging
import math
import os
from typing import Optional, Tuple

from fabio.cbfimage import CbfImage
import h5grove
from h5grove.content import DatasetContent
from h5grove.utils import get_array_stats
import h5py
from ispyb import models
import numpy as np

from ...config import settings
from ...core.modules.events import get_events
from ...core.modules.processings import get_processing_attachments
from ..schemas import data as schema

logger = logging.getLogger(__name__)


def get_image(
    dataCollectionId: int,
    imageNumber: int,
    header: bool = False,
) -> np.ndarray:
    datacollections = get_events(dataCollectionId=dataCollectionId, skip=0, limit=1)
    try:
        dc: models.DataCollection = datacollections.first["Item"]
    except IndexError:
        return None

    if imageNumber > dc.numberOfImages:
        logger.warning(
            f"Requested image {imageNumber} which is greater than total {dc.numberOfImages}"
        )
        return None

    file_path = os.path.join(dc.imageDirectory, dc.fileTemplate)
    if settings.path_map:
        file_path = settings.path_map + file_path

    ext = get_file_ext(dc.fileTemplate)
    if ext in ["h5", "H5", "hdf5", "HDF5"]:
        if not os.path.exists(file_path):
            return None

        _header, data = HDF5FormatHandler.preload(
            path=file_path, imageNumber=imageNumber
        )

    elif ext in ["cbf", "CBF"]:
        file_path = file_path % imageNumber
        if "%" in file_path:
            file_path = file_path.format(imageNumber)

        if not os.path.exists(file_path):
            logger.warning(
                f"Requested image {imageNumber} for dataCollection: {dataCollectionId} with path {file_path} does not exist on disk"
            )
            return None

        _header, data = CBFFormatHandler.preload(path=file_path)

    if header:
        return _header

    return data


def get_image_histogram(
    dataCollectionId: int,
    imageNumber: int,
) -> schema.ImageHistogram:
    data = get_image(dataCollectionId, imageNumber)
    if data is None:
        return None

    hist, bins = _compute_histogram(data)

    return {
        "values": hist.astype(np.float32).tolist(),
        "bins": bins,
        "shape": hist.shape,
        "max": np.max(hist).item() if hist.size > 0 else 0,
    }


class CBFFormatHandler:
    @staticmethod
    def preload(path: str) -> Tuple[dict, np.ndarray, bytes]:
        cbf_image = CbfImage(fname=path)
        float_data = cbf_image.data.astype(np.float32)

        parsed_ext_hdr, braggy_hdr = CBFFormatHandler._parse_header(
            cbf_image, float_data
        )

        img_hdr = {}
        img_hdr["parsed_ext_hdr"] = parsed_ext_hdr
        img_hdr["braggy_hdr"] = braggy_hdr

        return img_hdr, float_data.flatten()

    @staticmethod
    def _parse_header(cbf_image: CbfImage, np_array: np.ndarray) -> Tuple[dict, dict]:
        height, width = cbf_image.shape

        hdr = cbf_image.header
        parsed_ext_hdr = {}
        braggy_hdr = {}

        _ext_hdr = hdr.get("_array_data.header_contents", "").split("\r\n")
        for data in _ext_hdr:
            # Ignore empty lines coming from multiple line-breaks
            if data == "":
                continue

            key_value = data.strip("#").strip().split()

            key = key_value[0].strip(":").strip()
            value = " ".join(key_value[1:])
            parsed_ext_hdr[key] = value
        try:
            w = float(parsed_ext_hdr.get("Wavelength", "0").strip("A "))
            d = float(parsed_ext_hdr.get("Detector_distance", "0").strip("m "))

            bcx, bcy = parsed_ext_hdr["Beam_xy"].split(",")
            bcx, bcy = float(bcx.strip("pixels() ")), float(bcy.strip("pixels() "))

            px_size_x, px_size_y = parsed_ext_hdr.get("Pixel_size", "0").split("x")
            px_size_x, px_size_y = (
                float(px_size_x.strip("m ")),
                float(px_size_y.strip("m ")),
            )

            dr = math.sqrt((px_size_x * width) ** 2 + (px_size_y * height) ** 2) / 2

            # Remove invalid values (-1)
            clean_np_array = np_array[np_array >= 0]

            braggy_hdr = {
                "wavelength": w,
                "detector_distance": d,
                "beam_cx": bcx,
                "beam_cy": bcy,
                "beam_ocx": (width / 2) - bcx,
                "beam_ocy": (height / 2) - bcy,
                "detector_radius": dr,
                "pixel_size_x": px_size_x,
                "pixel_size_y": px_size_y,
                "img_width": width,
                "img_height": height,
                "pxxpm": 1 / px_size_x,
                "pxypm": 1 / px_size_y,
                **get_array_stats(
                    clean_np_array if clean_np_array.size > 0 else np_array
                ),
            }
        except (KeyError, IndexError):
            logging.info("Could not create Braggy header from CBF header")

        return parsed_ext_hdr, braggy_hdr


class HDF5FormatHandler:
    @staticmethod
    def preload(
        path: str,
        imageNumber: int,
    ) -> Tuple[dict, np.ndarray, bytes]:
        h5path, image_index = HDF5FormatHandler._find_path(path, imageNumber)
        if not h5path:
            return None, None

        with h5py.File(path, "r") as h5file:
            data = _get_dataset_data(h5file, h5path, str(image_index))

        np_array = data.astype(np.float32)
        img_hdr = HDF5FormatHandler._get_hdr(path, np_array)

        return img_hdr, np_array

    @staticmethod
    def _get_hdr(path: str, np_array: np.ndarray) -> dict[str, dict]:
        with h5py.File(path, "r") as h5file:
            wavelength = _get_instrument_param(h5file, "beam/incident_wavelength")
            detector = _get_instrument_param(h5file, "detector/detector_distance")

            pixel_size_x = _get_instrument_param(h5file, "detector/x_pixel_size")
            pixel_size_y = _get_instrument_param(h5file, "detector/y_pixel_size")
            width = _get_instrument_param(
                h5file, "detector/detectorSpecific/x_pixels_in_detector"
            )
            height = _get_instrument_param(
                h5file, "detector/detectorSpecific/y_pixels_in_detector"
            )

            beam_cx = _get_instrument_param(h5file, "detector/beam_center_x")
            beam_cy = _get_instrument_param(h5file, "detector/beam_center_y")

        # Remove invalid values (SATURATION VALUES)
        clean_np_array = np_array[np_array != np.max(np_array)]

        braggy_hdr = {
            "wavelength": wavelength,
            "detector_distance": detector,
            "beam_cx": beam_cx,
            "beam_cy": beam_cy,
            "beam_ocx": (width / 2) - beam_cx,
            "beam_ocy": (height / 2) - beam_cy,
            "detector_radius": (width * pixel_size_x) / 2,
            "pixel_size_x": pixel_size_x,
            "pixel_size_y": pixel_size_y,
            "img_width": width,
            "img_height": height,
            "pxxpm": 1 / pixel_size_x,
            "pxypm": 1 / pixel_size_y,
            **get_array_stats(clean_np_array if clean_np_array.size > 0 else np_array),
        }

        return {"braggy_hdr": braggy_hdr}

    @staticmethod
    def _find_path(path: str, imageNumber: int) -> Tuple[str, int]:
        """Lookup correct entry for requested imageNumber"""
        with h5py.File(path, "r") as h5file:
            dset_content = h5grove.create_content(h5file, "/entry/data")
            for child in dset_content.metadata()["children"]:
                child_path = "/entry/data/" + child["name"]
                image_nr_low = _get_dataset_attr(h5file, child_path)["image_nr_low"]
                image_nr_high = _get_dataset_attr(h5file, child_path)["image_nr_high"]

                if imageNumber >= image_nr_low and imageNumber <= image_nr_high:
                    image_index = imageNumber - image_nr_low.item()
                    logger.info(
                        f"Found imageNumber `{imageNumber}` in `{path}` with path `{child_path}` index `{image_index}`"
                    )

                    return child_path, image_index

        logger.warning(
            f"Could not find requested imageNumber `{imageNumber}` in `{path}` (max imageNumber `{image_nr_high}`)"
        )
        return None, None


def _get_dataset_attr(h5file: h5py.File, dset_path: str):
    dset_content = h5grove.create_content(h5file, dset_path)
    assert isinstance(dset_content, DatasetContent)  # nosec
    return dset_content.attributes()


def _get_dataset_data(
    h5file: h5py.File, dset_path: str, selection: Optional[str] = None
):
    dset_content = h5grove.create_content(h5file, dset_path)
    assert isinstance(dset_content, DatasetContent)  # nosec
    return dset_content.data(selection)


def _get_instrument_param(h5file: h5py.File, param_path: str):
    data = _get_dataset_data(h5file, f"/entry/instrument/{param_path}")
    assert isinstance(data, np.generic)  # nosec
    return data.item()


def _compute_histogram(data: np.ndarray) -> Tuple[np.ndarray, list]:
    std = 3 * np.std(data)
    mean = np.mean(data)
    clean_data = data[data < mean + std]

    if clean_data.size == 0:
        return np.ndarray([]), []

    hist, bins = np.histogram(
        clean_data.flatten(),
        bins=np.arange(np.min(clean_data), np.max(clean_data), 1)
        if np.max(clean_data) <= 300
        else 300,
    )
    return hist, bins.tolist()


def get_file_ext(file_name: str):
    _, ext = os.path.splitext(file_name)
    return ext[1:]  # Remove leading dot


def get_h5_file(
    dataCollectionId: Optional[int] = None,
    autoProcProgramAttachmentId: Optional[int] = None,
    robotActionId: Optional[int] = None,
):
    """Find the relevant hdf5 file from the parameters"""

    # Direct datacollection hdf5
    if dataCollectionId is not None:
        datacollections = get_events(dataCollectionId=dataCollectionId, skip=0, limit=1)
        dc = datacollections.first["Item"]
        return os.path.join(dc.imageDirectory, dc.fileTemplate)

    #  Directly from autoprocprogramattachmentid
    elif autoProcProgramAttachmentId is not None:
        attachments = get_processing_attachments(
            autoProcProgramAttachmentId=autoProcProgramAttachmentId, skip=0, limit=1
        )
        attachment = attachments.first
        ext = get_file_ext(attachment.fileName).lower()
        if attachment.fileType == "Result" and ext in ["h5", "hdf5"]:
            return attachment.fileFullPath

    # From a sample action
    elif robotActionId is not None:
        sampleactions = get_events(robotActionId, skip=0, limit=1)
        sampleaction = sampleactions.first
        return sampleaction.resultFilePath

    return None


def get_h5_path_mapped(**kwargs) -> str:
    file_path = get_h5_file(**kwargs)
    if file_path:
        if settings.path_map:
            return settings.path_map + file_path
