"""Contains tests for the services of the application."""

from typing import Any

from data.interfaces.irelease_repo import IReleaseRepo
from tests.mocks import MOCK_RELEASES


class MockReleaseRepo(IReleaseRepo):
    """A mock release repo."""

    def __init__(self) -> None:
        """Create the repo."""
        super().__init__()

    def get_all(self) -> list[dict[str, Any]]:
        """Mock 2 releases from GitHub."""
        return [mock.model_dump() for mock in MOCK_RELEASES]
