from datetime import datetime, timedelta
import logging
import os
import shutil
import time

from ispyb import models

from ..app.extensions.database.definitions import _proposal, _session
from .base import Simulation


logger = logging.getLogger(__name__)


class SimulateDataCollection(Simulation):
    def _get_container_position(
        self, ses, blsession: str, proposalId: str, beamline: str
    ) -> list[int, int]:
        shipment_name = "Simulation_Shipment"
        shipment = (
            ses.query(models.Shipping)
            .filter(models.Shipping.proposalId == proposalId)
            .filter(models.Shipping.shippingName == shipment_name)
            .first()
        )

        if not shipment:
            logger.debug("Creating shipment")
            shipment = models.Shipping(
                shippingName=shipment_name,
                proposalId=proposalId,
                creationDate=datetime.now(),
            )

            ses.add(shipment)
            ses.commit()

        dewar_name = "Simulation_Dewar"
        dewar = (
            ses.query(models.Dewar.dewarId)
            .filter(models.Dewar.shippingId == shipment.shippingId)
            .filter(models.Dewar.code == dewar_name)
            .first()
        )

        if not dewar:
            logger.debug("Creating dewar")
            dewar = models.Dewar(
                shippingId=shipment.shippingId,
                code=dewar_name,
                dewarStatus="processing",
            )
            ses.add(dewar)
            ses.commit()

        container_name = "Simulation_Container"
        container = (
            ses.query(models.Container.containerId)
            .filter(models.Container.dewarId == dewar.dewarId)
            .filter(models.Container.code == container_name)
            .first()
        )

        if not container:
            logger.debug("Creating container")
            container = models.Container(
                dewarId=dewar.dewarId,
                code=container_name,
                containerType="Box",
                capacity=25,
                bltimeStamp=datetime.now(),
                containerStatus="at facility",
                # beamlineLocation=beamline,
                # sampleChangerLocation=1,
            )
            ses.add(container)
            ses.commit()

            containerhistory = models.ContainerHistory(
                containerId=container.containerId,
                status="at facility",
                location=1,
                beamlineName=beamline,
            )

            ses.add(containerhistory)
            ses.commit()

        samples = (
            ses.query(models.BLSample)
            .filter(models.BLSample.containerId == container.containerId)
            .all()
        )
        max_loc = 0
        for s in samples:
            if int(s.location) > max_loc:
                max_loc = int(s.location)

        return container.containerId, max_loc + 1

    def run(self, beamline: str, experiment: str, delay=0):
        blses: str = self.config["sessions"][beamline]

        if experiment not in self.config["experiments"]:
            raise KeyError(f"No such experiment {experiment}")

        exp = self.config["experiments"][experiment]
        data = os.path.join(self.config["raw_data"], exp["data"])

        if not exp.get("experimentType"):
            raise KeyError(
                f"Experiment `{experiment}` does not specify `experimentType`"
            )

        if not os.path.exists(data):
            raise AttributeError(f"Raw data file: `{data}` does not exist")

        if not exp.get("sample"):
            raise KeyError(f"No sample specified for experiment `{experiment}`")

        if exp["sample"] not in self.config["samples"]:
            raise KeyError(
                f"Experiment sample `{exp['sample']}` is not defined in `samples`"
            )

        sample = self.config["samples"][exp["sample"]]

        with self.session() as ses:
            prop, blsession = (
                ses.query(_proposal, models.BLSession)
                .join(
                    models.Proposal,
                    models.Proposal.proposalId == models.BLSession.proposalId,
                )
                .filter(_session == blses)
                .first()
            )

            blsample = (
                ses.query(models.BLSample)
                .filter(models.BLSample.name == sample["name"])
                .first()
            )

            if not blsample:
                for k in ["component", "name"]:
                    if not sample.get(k):
                        raise KeyError(f"No {k} specified for sample {exp['sample']}")

                if sample["component"] not in self.config["components"]:
                    raise KeyError(
                        f"Sample component {sample['component']} is not defined in `components`"
                    )

                comp = self.config["components"][sample["component"]]
                for k in ["acronym"]:
                    if not comp.get(k):
                        raise KeyError(
                            f"No {k} specified for component {sample['component']}"
                        )

                component = (
                    ses.query(models.Protein)
                    .filter(models.Protein.acronym == comp["acronym"])
                    .first()
                )

                if not component:
                    logger.info(f"Creating component {comp['acronym']}")
                    component = models.Protein(
                        proposalId=blsession.proposalId,
                        acronym=comp.get("acronym"),
                        name=comp.get("name", comp.get("acronym")),
                        sequence=comp.get("sequence"),
                        density=comp.get("density"),
                        molecularMass=comp.get("molecularMass"),
                        description="Simulated component",
                    )
                    ses.add(component)
                    ses.commit()

                crystal = models.Crystal(proteinId=component.proteinId)
                ses.add(crystal)
                ses.commit()

                logger.info(f"Creating sample {sample['name']}")
                containerid, position = self._get_container_position(
                    ses, blses, blsession.proposalId, beamline
                )
                blsample = models.BLSample(
                    name=sample["name"],
                    crystalId=crystal.crystalId,
                    location=position,
                    containerId=containerid,
                )
                ses.add(blsample)
                ses.commit()

            subsampleid = None
            if exp.get("subsample"):
                logger.info("Creating subsample")
                sub = exp["subsample"]

                pos1id = None
                if sub.get("x") and sub.get("y"):
                    pos1 = models.Position(
                        posX=sub["x"],
                        posY=sub["y"],
                    )
                    ses.add(pos1)
                    ses.commit()

                    pos1id = pos1.positionId

                pos2id = None
                if sub.get("x2") and sub.get("y2"):
                    pos2 = models.Position(
                        posX=sub["x2"],
                        posY=sub["y2"],
                    )
                    ses.add(pos2)
                    ses.commit()

                    pos2id = pos2.positionId

                subsample = models.BLSubSample(
                    positionId=pos1id,
                    position2Id=pos2id,
                    blSampleId=blsample.blSampleId,
                    comments="Simulated sample",
                )

                if hasattr(subsample, "type"):
                    subsample.type = sub.get("type")

                ses.add(subsample)
                ses.commit()

                subsampleid = subsample.blSubSampleId

            startTime = datetime.now()
            endTime = datetime.now() + timedelta(minutes=5)

            logger.debug("Creating datacollection group")
            dcg = models.DataCollectionGroup(
                sessionId=blsession.sessionId,
                experimentType=exp["experimentType"],
                blSampleId=blsample.blSampleId,
                startTime=startTime,
                endTime=endTime,
            )
            ses.add(dcg)
            ses.commit()

            logger.debug("Creating datacollection")
            dc = models.DataCollection(
                blSubSampleId=subsampleid,
                dataCollectionGroupId=dcg.dataCollectionGroupId,
                fileTemplate=os.path.basename(exp["data"]),
                imageContainerSubPath=exp.get(
                    "imageContainerSubPath", "1.1/measurement"
                ),
                numberOfImages=exp.get("numberOfImages"),
                wavelength=exp.get("wavelength"),
                exposureTime=exp.get("exposureTime"),
                runStatus="Successful",
                comments="Simulated datacollection",
                startTime=startTime,
                endTime=endTime,
            )

            # Deprecated
            if hasattr(dc, "BLSAMPLEID"):
                dc.BLSAMPLEID = blsample.blSampleId

            ses.add(dc)
            ses.commit()

            if exp.get("grid"):
                logger.debug("Creating gridinfo")
                grid = models.GridInfo(
                    steps_x=exp["grid"]["steps_x"],
                    steps_y=exp["grid"]["steps_y"],
                    dx_mm=exp["grid"]["dx_mm"],
                    dy_mm=exp["grid"]["dy_mm"],
                )

                if hasattr(grid, "snapshot_offsetXPixel"):
                    grid.snapshot_offsetXPixel = exp["grid"]["snapshot_offsetXPixel"]
                    grid.snapshot_offsetYPixel = exp["grid"]["snapshot_offsetYPixel"]

                if hasattr(grid, "pixelsPerMicronX"):
                    grid.pixelsPerMicronX = exp["grid"]["pixelsPerMicronX"]
                    grid.pixelsPerMicronY = exp["grid"]["pixelsPerMicronY"]

                if hasattr(grid, "dataCollectionId"):
                    grid.dataCollectionId = dc.dataCollectionId
                # Deprecated but needed for pydb
                else:
                    grid.dataCollectionGroupId = dcg.dataCollectionGroupId

                ses.add(grid)
                ses.commit()

            logger.info(f"Created datacollection: `{dc.dataCollectionId}`")
            logger.info(
                f"{self.config['ispyb_url']}/visit/{blses}/id/{dc.dataCollectionId}"
            )

            logger.info("Triggering before start plugins")
            self.before_start(dc.dataCollectionId)

            # Create the dataset dir
            data_dir = os.path.join(
                self.config["data_dir"].format(beamline=beamline),
                prop,
                exp["sample"],
                f"{exp['sample']}_{dc.dataCollectionId}",
            )

            dc.imageDirectory = data_dir
            ses.commit()

            if os.path.exists(data_dir):
                logger.warning(f"Data directory already exists: {data_dir}")

            os.makedirs(data_dir)
            if not os.path.exists(data_dir):
                raise AttributeError(
                    f"Could not create output data directory: {data_dir}"
                )

            # Link data files / snapshots
            link = self.config.get("copy_method", "copy") == "link"
            if link:
                logger.debug("Linking data")
                os.link(data, os.path.join(data_dir, os.path.basename(data)))
            else:
                logger.debug("Copying data")
                shutil.copy(data, os.path.join(data_dir, os.path.basename(data)))

            snapshot_path = os.path.join(
                self.config["raw_data"], exp.get("xtalSnapshotFullPath1")
            )
            if snapshot_path:
                if os.path.exists(snapshot_path):
                    snapshot = os.path.join(data_dir, os.path.basename(snapshot_path))
                    if link:
                        logger.debug("Linking snapshot")
                        os.link(snapshot_path, snapshot)
                    else:
                        logger.debug("Copying snapshot")
                        shutil.copy(snapshot_path, snapshot)

                    snap, snap_extension = os.path.splitext(snapshot_path)
                    thumb = f"{snap}t{snap_extension}"
                    if os.path.exists(thumb):
                        if link:
                            logger.debug("Linking thumbnail")
                            os.link(
                                thumb,
                                os.path.join(
                                    data_dir,
                                    f"{os.path.basename(snap)}t{snap_extension}",
                                ),
                            )
                        else:
                            logger.debug("Copying thumbnail")
                            shutil.copy(
                                thumb,
                                os.path.join(
                                    data_dir,
                                    f"{os.path.basename(snap)}t{snap_extension}",
                                ),
                            )
                    else:
                        logger.warning(f"Snapshot thumbnail does not exist {thumb}")

                    dc.xtalSnapshotFullPath1 = snapshot
                else:
                    logger.warning(f"Snapshot file does not exist {snapshot_path}")

            logger.info(f"Finshed copying data to: {data_dir}")

            if delay:
                time.sleep(delay)

            logger.info("Triggering after end plugins")
            self.after_end(dc.dataCollectionId)
