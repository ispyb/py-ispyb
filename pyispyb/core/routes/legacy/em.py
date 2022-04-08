
__license__ = "LGPLv3+"

from fastapi import Depends, HTTPException
from fastapi.responses import FileResponse
from pyispyb.app.base import AuthenticatedAPIRouter
from pyispyb.core.modules.legacy.proposal import find_proposal_id

from pyispyb.core.modules.legacy import em
from pyispyb.core.routes.legacy.dependencies import proposal_authorisation, session_authorisation

from .base import router as legacy_router
router = AuthenticatedAPIRouter(prefix="/em", tags=["EM - legacy with header token"])


############################
#          MOVIES          #
############################


@legacy_router.get(
    "/{token}/proposal/{proposal_id}/em/datacollection/{datacollection_id}/movie/all",
)
@router.get("/proposal/{proposal_id}/datacollection/{datacollection_id}/movies")
def get_movies(datacollection_id: int, proposal_id: int = Depends(proposal_authorisation)):
    """Get movies date for datacollection.

    Args:
        proposal_id (str): proposal id or name
        datacollection_id (str): data collection id
    """
    proposal_id = find_proposal_id(proposal_id)
    return em.get_movies_data_by_datacollection_id(
        proposal_id, datacollection_id)


@legacy_router.get(
    "/{token}/proposal/{proposal_id}/em/datacollection/{datacollection_id}/movie/{movie_id}/thumbnail",
    response_class=FileResponse
)
@router.get("/proposal/{proposal_id}/movie/{movie_id}/thumbnail")
def get_movie_thumbnail(movie_id: int, proposal_id: int = Depends(proposal_authorisation)):
    """Get thumbnails for movie.

    Args:
        proposal_id (str): proposal id or name
        movie_id (str): movie id
    """
    proposal_id = find_proposal_id(proposal_id)
    path = em.get_movie_thumbnails(proposal_id, movie_id)
    if path:
        path = path["movie_thumbnail"]
    if path:
        return path
    else:
        raise HTTPException(status_code=404, detail="Sample not found")


@legacy_router.get(
    "/{token}/proposal/{proposal_id}/em/datacollection/{datacollection_id}/movie/{movie_id}/motioncorrection/thumbnail",
    response_class=FileResponse
)
@router.get("/proposal/{proposal_id}/movie/{movie_id}/thumbnail/motioncorrection")
def get_motion_thumbnail(movie_id: int, proposal_id: int = Depends(proposal_authorisation)):
    """Get motion correction thumbnail for movie.

    Args:
        proposal_id (str): proposal id or name
        movie_id (str): movie id
    """
    proposal_id = find_proposal_id(proposal_id)
    path = em.get_movie_thumbnails(proposal_id, movie_id)
    if path:
        path = path["motion_correction_thumbnail"]
    if path:
        return path
    else:
        raise HTTPException(status_code=404, detail="Sample not found")


@legacy_router.get(
    "/{token}/proposal/{proposal_id}/em/datacollection/{datacollection_id}/movie/{movie_id}/ctf/thumbnail",
)
@router.get("/proposal/{proposal_id}/movie/{movie_id}/thumbnail/ctf")
def get_ctf_thumbnail(movie_id: int, proposal_id: int = Depends(proposal_authorisation)):
    """Get CTF thumbnail for movie.

    Args:
        proposal_id (str): proposal id or name
        movie_id (str): movie id
    """
    proposal_id = find_proposal_id(proposal_id)
    path = em.get_movie_thumbnails(proposal_id, movie_id)
    if path:
        path = path["ctf_thumbnail"]
    if path:
        return path
    else:
        raise HTTPException(status_code=404, detail="Sample not found")


@legacy_router.get(
    "/{token}/proposal/{proposal_id}/em/datacollection/{datacollection_id}/movie/{movie_id}/motioncorrection/drift",
    response_class=FileResponse
)
@router.get("/proposal/{proposal_id}/movie/{movie_id}/plot/motioncorrectiondrift")
def get_motion_drift_thumbnail(movie_id: int, proposal_id: int = Depends(proposal_authorisation)):
    """Get motion correction drift thumbnail for movie.

    Args:
        proposal_id (str): proposal id or name
        movie_id (str): movie id
    """
    proposal_id = find_proposal_id(proposal_id)
    path = em.get_movie_thumbnails(proposal_id, movie_id)
    if path:
        path = path["motion_correction_drift"]
    if path:
        return path
    else:
        raise HTTPException(status_code=404, detail="Sample not found")

############################
#          STATS           #
############################


@legacy_router.get(
    "/{token}/proposal/{proposal}/em/session/{session_id}/stats",
)
@router.get("/session/{session_id}/stats")
def get_stats_session(session_id: int = Depends(session_authorisation)):
    """Get stats for session.

    Args:
        session_id (str): session id
    """
    return em.get_stats_by_session_id(session_id)


@legacy_router.get(
    "/proposal/{proposal_id}/data_collections/{data_collections_ids}/stats",
)
@router.get("/proposal/{proposal_id}/data_collections/{data_collections_ids}/stats")
def get_stats_dcids(data_collections_ids: str, proposal_id: int = Depends(proposal_authorisation)):
    """Get stats for data collection ids.

    Args:
        proposal_id (str): proposal id or name
        data_collections_ids (str): comma-separated datacollection ids
    """
    proposal_id = find_proposal_id(proposal_id)
    return em.get_stats_by_data_collections_ids(
        proposal_id, data_collections_ids)


@legacy_router.get(
    "/proposal/{proposal_id}/data_collections_group/{data_collections_group_id}/stats",
)
@router.get("/proposal/{proposal_id}/data_collections_group/{data_collections_group_id}/stats")
def get_stats_group(data_collections_group_id: int, proposal_id: int = Depends(proposal_authorisation)):
    """Get stats for datacollection group.

    Args:
        proposal_id (str): proposal id or name
        data_collections_group_id (str): data collection group id
    """
    proposal_id = find_proposal_id(proposal_id)
    return em.get_stats_by_data_collections_group_id(
        proposal_id, data_collections_group_id)

############################
#     DATA COLLECTION      #
############################


@legacy_router.get(
    "/{token}/proposal/{proposal_id}/em/datacollection/session/{session_id}/list",
)
@router.get("/proposal/{proposal_id}/session/{session_id}/data_collections/groups")
def get_groups_for_session(proposal_id: int = Depends(proposal_authorisation), session_id: int = Depends(session_authorisation)):
    """Get datacollection groups for session.

    Args:
        proposal_id (str): proposal id or name
        session_id (str): session id
    """
    proposal_id = find_proposal_id(proposal_id)
    return em.get_data_collections_groups(proposal_id, session_id)

############################
#     CLASSIFICATION       #
############################


@legacy_router.get("/{token}/proposal/{proposal_id}/em/session/{session_id}/classification")
@router.get("/session/{session_id}/classification")
def get_classification(self, session_id: int = Depends(session_authorisation), **kwargs):
    """Get classification for session.

    Args:
        session_id (str): session id
    """
    return em.get_classification_by_session_id(session_id)
