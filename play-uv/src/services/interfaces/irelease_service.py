"""Contains the interface for the release service."""

from abc import ABC, abstractmethod

from schemas.release import GithubRelease


class IReleaseService(ABC):
    """Interface for the release service."""

    def __init__(self) -> None:
        """Init the class."""
        super().__init__()

    @abstractmethod
    def get_all(self) -> list[GithubRelease]:
        """
        Get the 30 latest releases for the requests package.

        Returns:
            releases (list[GithubRelease]): 30 latest releases for the package.
        """
