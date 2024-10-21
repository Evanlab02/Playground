"""Contains tests for the release service."""

from services.release_service import ReleaseService
from tests.mocks import MOCK_RELEASES
from tests.services import MockReleaseRepo

service = ReleaseService(repo=MockReleaseRepo())


def test_get_all() -> None:
    """Test the get all function."""
    result = service.get_all()
    assert len(result) == 2
    assert [item.model_dump() for item in result] == [
        item.model_dump() for item in MOCK_RELEASES
    ]
