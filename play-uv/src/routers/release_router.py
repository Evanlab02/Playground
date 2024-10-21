"""Contains the release router for the application."""

from fastapi import APIRouter

from data.release_repo import ReleaseRepo
from schemas.release import GithubRelease
from services.release_service import ReleaseService

REPO = ReleaseRepo()
SERVICE = ReleaseService(repo=REPO)

router = APIRouter(prefix="/api/v1/releases", tags=["release"])


@router.get("")
def get_releases() -> list[GithubRelease]:
    """Get the latest releases for the python requests package."""
    result = SERVICE.get_all()
    return result
