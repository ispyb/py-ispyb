from collections import Counter
from dataclasses import dataclass
from difflib import SequenceMatcher
import os
from typing import Any, Optional

from ispyb import models
import sqlalchemy
from sqlalchemy import func, and_, text, extract, distinct, Date, cast


from ...config import settings
from ...core.modules.utils import get_last_line, to_energy
from ...app.extensions.database.utils import Paged, page
from ...app.extensions.database.definitions import (
    with_authorization,
)
from ...app.extensions.database.middleware import db
from ...core.schemas import stats as schema


def filter_query(
    query: "sqlalchemy.orm.Query[Any]",
    runId: str = None,
    beamLineName: str = None,
    session: str = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> "sqlalchemy.orm.Query[Any]":
    if runId:
        query = query.join(
            models.VRun,
            models.BLSession.startDate.between(
                models.VRun.startDate, models.VRun.endDate
            ),
        )
        query = query.filter(models.VRun.runId == runId)

    if beamLineName:
        query = query.filter(models.BLSession.beamLineName == beamLineName)

    if session:
        query = query.filter(models.BLSession.session == session)

    if beamLineGroups:
        query = with_authorization(query, beamLineGroups, joinBLSession=False)

    return query


def get_breakdown(
    session: Optional[str] = None,
    beamLineName: Optional[str] = None,
    runId: Optional[str] = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> schema.Breakdown:

    if session:
        info = (
            db.session.query(
                models.BLSession.startDate,
                models.BLSession.endDate,
                models.BLSession.beamLineName,
                models.BLSession.session,
                (
                    func.timestampdiff(
                        text("SECOND"),
                        models.BLSession.startDate,
                        models.BLSession.endDate,
                    )
                    / 3600
                ).label("duration"),
            )
            .join(models.Proposal)
            .filter(models.BLSession.session == session)
            .first()
        )
    else:
        info = (
            db.session.query(
                models.VRun.startDate,
                models.VRun.endDate,
                models.VRun.run,
                (
                    func.timestampdiff(
                        text("SECOND"),
                        models.VRun.startDate,
                        models.VRun.endDate,
                    )
                    / 3600
                ).label("duration"),
            )
            .filter(models.VRun.runId == runId)
            .first()
        )

    queries = {}
    queries["dc"] = (
        db.session.query(
            models.DataCollection.dataCollectionId,
            models.DataCollection.startTime,
            models.DataCollection.endTime,
            models.DataCollection.runStatus.label("status"),
            models.DataCollectionGroup.experimentType.label("subType"),
            models.DataCollection.wavelength,
            models.DataCollection.beamSizeAtSampleX,
            models.DataCollection.beamSizeAtSampleY,
            models.DataCollection.chiStart,
            models.DataCollection.kappaStart,
            models.DataCollection.phiStart,
        )
        .select_from(models.DataCollection)
        .join(models.DataCollectionGroup)
        .outerjoin(
            models.BLSample,
            models.DataCollectionGroup.blSampleId == models.BLSample.blSampleId,
        )
        .filter(
            and_(
                models.DataCollection.startTime != None,  # noqa
                models.DataCollection.endTime != None,  # noqa
            )
        )
        .group_by(models.DataCollection.dataCollectionId)
        .order_by(models.DataCollection.startTime)
    )

    queries["robot"] = (
        db.session.query(
            models.RobotAction.robotActionId,
            models.RobotAction.startTimestamp.label("startTime"),
            models.RobotAction.endTimestamp.label("endTime"),
            models.RobotAction.actionType.label("subType"),
            models.RobotAction.status,
        )
        .outerjoin(models.BLSample)
        .group_by(models.RobotAction.robotActionId)
        .order_by(models.RobotAction.endTimestamp)
    )

    queries["edge"] = (
        db.session.query(
            models.EnergyScan.energyScanId,
            models.EnergyScan.startTime,
            models.EnergyScan.endTime,
        )
        .outerjoin(models.BLSample)
        .order_by(models.EnergyScan.endTime)
        .group_by(models.EnergyScan.energyScanId)
    )

    queries["xrf"] = (
        db.session.query(
            models.XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId,
            models.XFEFluorescenceSpectrum.startTime,
            models.XFEFluorescenceSpectrum.endTime,
        )
        .outerjoin(models.BLSample)
        .order_by(models.XFEFluorescenceSpectrum.endTime)
        .group_by(models.XFEFluorescenceSpectrum.xfeFluorescenceSpectrumId)
    )

    queries["fault"] = (
        db.session.query(
            models.BFFault.faultId,
            models.BFFault.title,
            models.BFFault.beamtimelost_starttime.label("startTime"),
            models.BFFault.beamtimelost_endtime.label("endTime"),
        )
        .filter(models.BFFault.beamtimelost == 1)
        .order_by(models.BFFault.beamtimelost_endtime)
        .group_by(models.BFFault.faultId)
    )

    if session:
        queries["strategy"] = (
            db.session.query(
                models.DataCollection.endTime.label("startTime"),
                func.max(models.Screening.bltimeStamp).label("endTime"),
            )
            .join(models.Screening)
            .join(models.DataCollectionGroup)
            .order_by(models.DataCollection.endTime)
            .group_by(
                models.DataCollection.dataCollectionId, models.DataCollection.endTime
            )
        )

        queries["centring"] = (
            db.session.query(
                models.RobotAction.endTimestamp.label("startTime"),
                func.min(models.DataCollection.startTime).label("endTime"),
                func.timestampdiff(
                    text("SECOND"),
                    cast(models.RobotAction.endTimestamp, Date),
                    func.min(models.DataCollection.startTime),
                ).label("duration"),
            )
            .select_from(models.RobotAction)
            .join(
                models.DataCollectionGroup,
                models.DataCollectionGroup.blSampleId == models.RobotAction.blsampleId,
            )
            .join(
                models.DataCollection,
                and_(
                    models.DataCollection.dataCollectionGroupId
                    == models.DataCollectionGroup.dataCollectionGroupId,
                    models.RobotAction.endTimestamp < models.DataCollection.startTime,
                ),
            )
            .join(
                models.BLSession,
                models.BLSession.sessionId == models.DataCollectionGroup.sessionId,
            )
            .order_by(models.RobotAction.endTimestamp)
            .group_by(models.RobotAction.endTimestamp)
        )

    else:
        queries["sessions"] = (
            db.session.query(
                models.BLSession.session,
                models.BLSession.startDate.label("startTime"),
                models.BLSession.endDate.label("endTime"),
                models.BLSession.scheduled,
                models.Proposal.title,
            )
            .order_by(models.BLSession.startDate)
            .group_by(models.BLSession.session)
        )

    results = {}
    for key in queries.keys():
        if key not in ["fault", "strategy", "centring", "sessions"]:
            queries[key] = (
                queries[key]
                .add_columns(
                    models.BLSample.name.label("sample"),
                    models.Protein.name.label("protein"),
                )
                .outerjoin(models.Crystal)
                .outerjoin(models.Protein)
            )

        if key not in ["sessions", "centring"]:
            queries[key] = queries[key].join(models.BLSession)

        queries[key] = queries[key].join(models.Proposal)

        queries[key] = filter_query(
            queries[key], runId, beamLineName, session, beamLineGroups
        )

        if key == "centring":
            subquery = queries[key].subquery()
            queries[key] = db.session.query(
                subquery.c.startTime.label("startTime"),
                subquery.c.endTime.label("endTime"),
            ).filter(subquery.c.duration < 1000)
            print(queries[key])

        results[key] = [r._asdict() for r in queries[key].all()]

    history = []
    for key in ["dc", "robot", "edge", "xrf", "centring", "strategy"]:
        if key in results:
            for row in results[key]:
                history.append(schema.BreakdownPoint(eventType=key, **row))

    if "sessions" in results:
        for row in results["sessions"]:
            if row["scheduled"]:
                history.append(schema.BreakdownPoint(eventType="session", **row))

    series = []
    for plottable in [
        "wavelength",
        "beamSizeAtSampleX",
        "beamSizeAtSampleY",
        "chiStart",
        "phiStart",
        "kappaStart",
    ]:
        series.append(
            schema.BreakdownPlottable(
                title="energy" if plottable == "wavelength" else plottable,
                data=[
                    to_energy(row[plottable])
                    if plottable == "wavelength"
                    else row[plottable]
                    for row in results["dc"]
                ],
            )
        )

    overview = (
        schema.BreakdownOverviewSession if session else schema.BreakdownOverviewRun
    )
    return {
        "overview": overview(
            counts=schema.BreakdownOverviewCounts(
                datacollections=len(results["dc"]),
                failed=0,
                datacollectionTypes=Counter([row["subType"] for row in results["dc"]]),
                robot=len(results["robot"]),
                edge=len(results["edge"]),
                xrf=len(results["xrf"]),
            ),
            **info,
        ),
        "history": history,
        "plottables": schema.BreakdownPlottables(
            time=[row["startTime"] for row in results["dc"]], series=series
        ),
    }


def get_times(
    session: Optional[str] = None,
    proposal: Optional[str] = None,
    beamLineName: Optional[str] = None,
    runId: Optional[str] = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> schema.Times:
    """Get proportions of time used in a session"""
    queries = {}
    queries["dc"] = (
        db.session.query(
            func.min(models.BLSession.startDate).label("start"),
            func.max(models.BLSession.endDate).label("end"),
            models.BLSession.session,
            (
                func.timestampdiff(
                    text("SECOND"),
                    func.min(models.BLSession.startDate),
                    func.max(models.BLSession.endDate),
                )
                / 3600
            ).label("duration"),
            (
                func.sum(
                    func.timestampdiff(
                        text("SECOND"),
                        models.DataCollection.startTime,
                        models.DataCollection.endTime,
                    )
                )
                / (
                    3600
                    * (
                        func.count(models.DataCollection.dataCollectionId)
                        / func.count(distinct(models.DataCollection.dataCollectionId))
                    )
                )
            ).label("datacollection"),
            func.max(models.DataCollection.endTime).label("last"),
            func.greatest(
                func.timestampdiff(
                    text("SECOND"),
                    func.min(models.BLSession.startDate),
                    func.min(models.DataCollection.startTime),
                )
                / 3600,
                0,
            ).label("startup"),
            func.greatest(
                func.timestampdiff(
                    text("SECOND"),
                    func.max(models.DataCollection.endTime),
                    func.max(models.BLSession.endDate),
                )
                / 3600,
                0,
            ).label("remaining"),
        )
        .select_from(models.DataCollection)
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
        .group_by(models.BLSession.session)
        .order_by(models.BLSession.startDate.desc())
    )

    queries["robot"] = (
        db.session.query(
            (
                func.timestampdiff(
                    text("SECOND"),
                    models.RobotAction.startTimestamp,
                    models.RobotAction.endTimestamp,
                )
                / 3600
            ).label("robot"),
            models.BLSession.session,
        )
        .select_from(models.RobotAction)
        .join(models.BLSession)
        .join(models.Proposal)
        .group_by(models.BLSession.session)
    )

    queries["edge"] = (
        db.session.query(
            (
                func.timestampdiff(
                    text("SECOND"),
                    models.EnergyScan.startTime,
                    models.EnergyScan.endTime,
                )
                / 3600
            ).label("edge"),
            models.BLSession.session,
        )
        .select_from(models.EnergyScan)
        .join(models.BLSession)
        .join(models.Proposal)
        .group_by(models.BLSession.session)
    )

    queries["xrf"] = (
        db.session.query(
            (
                func.timestampdiff(
                    text("SECOND"),
                    models.XFEFluorescenceSpectrum.startTime,
                    models.XFEFluorescenceSpectrum.endTime,
                )
                / 3600
            ).label("xrf"),
            models.BLSession.session,
        )
        .select_from(models.XFEFluorescenceSpectrum)
        .join(models.BLSession)
        .join(models.Proposal)
        .group_by(models.BLSession.session)
    )

    queries["strategy"] = (
        db.session.query(
            (
                func.timestampdiff(
                    text("SECOND"),
                    models.DataCollection.endTime,
                    func.max(models.Screening.bltimeStamp),
                )
                / 3600
            ).label("strategy"),
            models.BLSession.session,
        )
        .select_from(models.DataCollection)
        .join(models.Screening)
        .join(
            models.DataCollectionGroup,
            models.DataCollectionGroup.dataCollectionGroupId
            == models.DataCollection.dataCollectionGroupId,
        )
        .join(models.BLSession)
        .join(models.Proposal)
        .group_by(
            models.DataCollection.dataCollectionId,
            models.BLSession.session,
            models.DataCollection.endTime,
        )
    )

    queries["centring"] = (
        db.session.query(
            (
                func.timestampdiff(
                    text("SECOND"),
                    cast(models.RobotAction.endTimestamp, Date),
                    func.min(models.DataCollection.startTime),
                )
                / 3600
            ).label("centring"),
            models.BLSession.session,
        )
        .select_from(models.RobotAction)
        .join(
            models.DataCollection,
            models.RobotAction.endTimestamp < models.DataCollection.startTime,
        )
        .join(
            models.DataCollectionGroup,
            and_(
                models.DataCollectionGroup.dataCollectionGroupId
                == models.DataCollection.dataCollectionGroupId,
                models.RobotAction.blsampleId == models.DataCollectionGroup.blSampleId,
            ),
        )
        .join(
            models.BLSession,
            models.BLSession.sessionId == models.DataCollectionGroup.sessionId,
        )
        .join(
            models.Proposal, models.Proposal.proposalId == models.BLSession.proposalId
        )
        .group_by(
            models.DataCollection.dataCollectionId,
            models.BLSession.session,
            models.DataCollection.endTime,
        )
    )

    queries["fault"] = (
        db.session.query(
            (
                func.timestampdiff(
                    text("SECOND"),
                    models.BFFault.beamtimelost_starttime,
                    models.BFFault.beamtimelost_endtime,
                )
                / 3600
            ).label("fault"),
            models.BLSession.session,
        )
        .select_from(models.BFFault)
        .join(models.BLSession)
        .join(models.Proposal)
        .group_by(models.BLSession.session)
    )

    for key in queries.keys():
        queries[key] = filter_query(
            queries[key], runId, beamLineName, session, beamLineGroups
        )
        if proposal:
            queries[key] = queries[key].filter(models.Proposal.proposal == proposal)

    strategy = queries["strategy"].subquery()
    queries["strategy"] = db.session.query(
        func.sum(strategy.c.strategy).label("strategy"),
        strategy.c.session.label("session"),
    ).group_by(strategy.c.session)

    centring = queries["centring"].subquery()
    queries["centring"] = (
        db.session.query(
            func.sum(centring.c.centring).label("centring"),
            centring.c.session.label("session"),
        )
        .filter(centring.c.centring < 0.25)
        .group_by(centring.c.session)
    )

    results = {}
    for key in queries.keys():
        results[key] = [r._asdict() for r in queries[key].all()]

    session_lookup = {}
    for key in ["robot", "strategy", "edge", "xrf", "centring", "fault"]:
        if key not in session_lookup:
            session_lookup[key] = {}

        for row in results[key]:
            session_lookup[key][row["session"]] = row[key]

    sessions = []
    for row in results["dc"]:
        session_time = schema.SessionTimeEntry(
            **row,
            robot=session_lookup["robot"].get(row["session"], 0),
            strategy=session_lookup["strategy"].get(row["session"], 0),
            edge=session_lookup["edge"].get(row["session"], 0),
            xrf=session_lookup["xrf"].get(row["session"], 0),
            centring=session_lookup["centring"].get(row["session"], 0),
            fault=session_lookup["fault"].get(row["session"], 0),
        )
        session_time.thinking = session_time.calc_thinking()
        sessions.append(session_time)

    average = schema.AverageTimeEntry()
    average.average(*sessions)
    return {"sessions": sessions, "average": average}


def get_errors(
    session: Optional[str] = None,
    beamLineName: Optional[str] = None,
    runId: Optional[str] = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> schema.Errors:
    """Get proportion of success and errors for data collection types
    along with their error message frequency"""
    queries = {}
    queries["total"] = (
        db.session.query(
            func.count(distinct(models.DataCollection.dataCollectionId)).label("count"),
            models.DataCollectionGroup.experimentType,
        )
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
        .group_by(models.DataCollectionGroup.experimentType)
    )

    queries["dc"] = (
        db.session.query(
            models.DataCollection.dataCollectionId,
            models.DataCollection.runStatus,
            models.DataCollectionGroup.experimentType,
            models.DataCollectionFileAttachment.fileFullPath.label("logFile"),
        )
        .join(
            models.DataCollectionFileAttachment,
            and_(
                models.DataCollectionFileAttachment.dataCollectionId
                == models.DataCollection.dataCollectionId,
                models.DataCollectionFileAttachment.fileType == "log",
                models.DataCollectionFileAttachment.fileFullPath.like("%err%"),
            ),
        )
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
        .group_by(models.DataCollection.dataCollectionId)
        .filter(models.DataCollection.runStatus.notlike("%success%"))
    )

    for key in queries.keys():
        queries[key] = filter_query(
            queries[key], runId, beamLineName, session, beamLineGroups
        )

    totals_rows = [r._asdict() for r in queries["total"].all()]
    totals: dict[str, schema.ExperimentTypeGroup] = {}
    for row in totals_rows:
        totals[row["experimentType"]] = schema.ExperimentTypeGroupPrepare(
            experimentType=row["experimentType"],
            total=row["count"],
            failed=0,
            aborted=0,
            messages={},
        )

    datacollections = [r._asdict() for r in queries["dc"].all()]
    for row in datacollections:
        if "aborted" in row["runStatus"].lower():
            totals[row["experimentType"]].aborted += 1
        else:
            totals[row["experimentType"]].failed += 1

            if row["logFile"]:
                log_path = row["logFile"]
                if settings.path_map:
                    log_path = settings.path_map + log_path
                    if os.path.exists(log_path):
                        last_line = get_last_line(log_path)
                        if last_line:
                            if last_line not in totals[row["experimentType"]].messages:

                                replaced = False
                                for message in totals[
                                    row["experimentType"]
                                ].messages.keys():
                                    s = SequenceMatcher(None, last_line, message)
                                    if s.ratio() > 0.8:
                                        last_line = message
                                        replaced = True

                                if not replaced:
                                    totals[row["experimentType"]].messages[
                                        last_line
                                    ] = schema.ExperimentTypeMessages(
                                        message=last_line,
                                        count=0,
                                    )

                            totals[row["experimentType"]].messages[last_line].count += 1

    for row in totals.values():
        row.failedPercent = round(row.failed / row.total * 100, 1)
        row.abortedPercent = round(row.aborted / row.total * 100, 1)
        row.messages = list(row.messages.values())
        row.messages = sorted(row.messages, key=lambda d: d.count)

    return {"totals": list(totals.values())}


def get_hourlies(
    session: Optional[str] = None,
    proposal: Optional[str] = None,
    beamLineName: Optional[str] = None,
    runId: Optional[str] = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
) -> schema.Hourlies:
    """Get hourly statistics"""
    queries = {}

    queries["datacollections"] = (
        db.session.query(
            func.count(distinct(models.DataCollection.dataCollectionId)).label("count"),
            extract("HOUR", models.DataCollection.startTime).label("hour"),
        )
        .join(models.DataCollectionGroup)
        .group_by(
            func.concat(
                extract("DAY", models.DataCollection.startTime),
                extract("HOUR", models.DataCollection.startTime),
            )
        )
    )

    queries["loaded"] = (
        db.session.query(
            func.count(distinct(models.RobotAction.robotActionId)).label("count"),
            extract("HOUR", models.RobotAction.startTimestamp).label("hour"),
        )
        .filter(models.RobotAction.actionType.like("load"))
        .group_by(
            func.concat(
                extract("DAY", models.RobotAction.startTimestamp),
                extract("HOUR", models.RobotAction.startTimestamp),
            )
        )
    )

    hourlies = {}
    for key in queries.keys():
        queries[key] = queries[key].join(models.BLSession).join(models.Proposal)

        queries[key] = filter_query(
            queries[key], runId, beamLineName, session, beamLineGroups
        )

        if proposal:
            queries[key] = queries[key].filter(models.Proposal.proposal == proposal)

        subquery = queries[key].subquery()
        queries[key] = db.session.query(
            func.avg(subquery.c.count).label("average"), subquery.c.hour
        ).group_by(subquery.c.hour)

        results = [r._asdict() for r in queries[key].all()]
        hour_map = {}
        for row in results:
            hour_map[row["hour"]] = row["average"]

        hourlies[key] = schema.Hourly(
            hour=[hour for hour in range(24)],
            average=[hour_map.get(hour, 0) for hour in range(24)],
        )

    return hourlies


@dataclass
class HistogramParameter:
    unit: str
    start: float
    end: float
    bin_size: int
    column: "sqlalchemy.Column[Any]"
    count_column: "sqlalchemy.Column[Any]"


def get_parameter_histogram(
    session: Optional[str] = None,
    beamLineName: Optional[str] = None,
    runId: Optional[str] = None,
    beamLineGroup: Optional[str] = None,
    beamLineGroups: Optional[dict[str, Any]] = None,
    parameter: str = "energy",
) -> schema.ParameterHistograms:
    """Get a parameter histogram"""
    parameters: dict[str, HistogramParameter] = {
        "energy": HistogramParameter(
            unit="eV",
            start=1000,
            end=25000,
            bin_size=200,
            column=(1.98644568e-25 / (models.DataCollection.wavelength * 1e-10))
            / 1.60217646e-19,
            count_column=models.DataCollection.wavelength,
        ),
        "beamsizex": HistogramParameter(
            unit="um",
            start=0,
            end=150,
            bin_size=5,
            column=models.DataCollection.beamSizeAtSampleX * 1000,
            count_column=models.DataCollection.beamSizeAtSampleX,
        ),
        "beamsizey": HistogramParameter(
            unit="um",
            start=0,
            end=150,
            bin_size=5,
            column=models.DataCollection.beamSizeAtSampleY * 1000,
            count_column=models.DataCollection.beamSizeAtSampleY,
        ),
        "exposuretime": HistogramParameter(
            unit="ms",
            start=0,
            end=5000,
            bin_size=50,
            column=models.DataCollection.exposureTime * 1000,
            count_column=models.DataCollection.exposureTime,
        ),
    }

    if parameter not in parameters:
        raise IndexError(f"Unknown parameter `{parameter}`")

    param = parameters[parameter]
    query = (
        db.session.query(
            ((param.column / param.bin_size) * param.bin_size).label("x"),
            func.count(param.count_column).label("y"),
            models.BLSession.beamLineName,
        )
        .select_from(models.DataCollection)
        .join(models.DataCollectionGroup)
        .join(models.BLSession)
        .join(models.Proposal)
        .group_by(models.BLSession.beamLineName, text("x"))
        .order_by(models.BLSession.beamLineName, text("x"))
    )

    query = filter_query(query, runId, beamLineName, session, beamLineGroups)

    if beamLineGroups:
        if beamLineGroup:
            for group in beamLineGroups:
                if group == beamLineGroup:
                    query = query.filter(
                        models.BLSession.beamLineName.in_(
                            [bl["beamLineName"] for bl in group.beamlines]
                        )
                    )

    results = [r._asdict() for r in query.all()]
    histogram_lookup = {}
    for row in results:
        if row["beamLineName"] not in histogram_lookup:
            histogram_lookup[row["beamLineName"]] = {}
        histogram_lookup[row["beamLineName"]][round(row["x"])] = row["y"]

    histograms = {}
    for beamline in histogram_lookup.keys():
        histograms[beamline] = {}
        for histogram_bin in range(param.start, param.end, param.bin_size):
            if histogram_bin not in histogram_lookup[beamline]:
                histograms[beamline][histogram_bin] = 0
            else:
                histograms[beamline][histogram_bin] = histogram_lookup[beamline][
                    histogram_bin
                ]

    return schema.ParameterHistograms(
        parameter=parameter,
        unit=param.unit,
        beamLines=[
            schema.ParameterHistogram(
                beamLineName=beamline,
                bin=list(histogram.keys()),
                frequency=list(histogram.values()),
            )
            for beamline, histogram in histograms.items()
        ],
    )


def get_runs(skip: int, limit: int) -> Paged[models.VRun]:
    query = db.session.query(models.VRun).order_by(models.VRun.startDate.desc())
    total = query.count()
    query = page(query, skip=skip, limit=limit)
    return Paged(total=total, results=query.all(), skip=skip, limit=limit)
