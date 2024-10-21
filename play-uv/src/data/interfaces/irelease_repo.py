"""Contains the interface for the release repository."""

from abc import ABC, abstractmethod
from typing import Any


class IReleaseRepo(ABC):
    """Interface for the release repository."""

    def __init__(self) -> None:
        """Init the class."""
        super().__init__()

    @abstractmethod
    def get_all(self) -> list[dict[str, Any]]:
        """
        Get the latest releases for the requests package.

        Returns:
            releases (list[dict[str, Any]]): 30 latest releases for the package.
        """
