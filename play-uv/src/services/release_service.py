"""Contains the release service."""

from data.interfaces.irelease_repo import IReleaseRepo
from schemas.release import GithubRelease
from services.interfaces.irelease_service import IReleaseService


class ReleaseService(IReleaseService):
    """Contains the release service functionality."""

    def __init__(self, repo: IReleaseRepo) -> None:
        """Create the release service."""
        self.repo = repo
        super().__init__()

    def get_all(self) -> list[GithubRelease]:
        """
        Get the latest releases for the requests package.

        Returns:
            releases (list[GithubRelease]): 30 latest releases for the package.
        """
        result = self.repo.get_all()
        releases = []

        for item in result:
            release = GithubRelease.model_validate(item, strict=True)
            releases.append(release)

        return releases
