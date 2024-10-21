"""Contains tests for the release repository."""

import pytest
from pytest_mock import MockerFixture

from data.release_repo import ReleaseRepo
from errors.data import DataDoesNotExistError, DataInvalidError
from schemas.release import GithubRelease


def test_get_all(mocker: MockerFixture) -> None:
    """Test the get all function."""
    mock_value: list[GithubRelease] = [
        GithubRelease(
            created_at="Yesterday",
            name="Release 1",
            prerelease=False,
            published_at="Today",
            tag_name="v1.0.0",
            url="https://github.com/v1",
        ),
        GithubRelease(
            created_at="Today",
            name="Release 2",
            prerelease=True,
            published_at="Today",
            tag_name="v2.0.0",
            url="https://github.com/v2",
        ),
    ]

    func = mocker.patch("json.load")
    func.return_value = [mock.model_dump() for mock in mock_value]

    repo = ReleaseRepo()
    data = repo.get_all()
    assert len(data) == 2
    assert data == [mock.model_dump() for mock in mock_value]


def test_get_all_when_file_does_not_exist(mocker: MockerFixture) -> None:
    """Test the get all function when the file does not exist."""
    func = mocker.patch("builtins.open")
    func.side_effect = FileNotFoundError("File does not exist.")

    with pytest.raises(DataDoesNotExistError):
        repo = ReleaseRepo()
        repo.get_all()


def test_get_all_with_invalid_data(mocker: MockerFixture) -> None:
    """Test the get all function when the file does not exist."""
    mock_value: dict[str, str] = {}

    func = mocker.patch("json.load")
    func.return_value = mock_value

    with pytest.raises(DataInvalidError):
        repo = ReleaseRepo()
        repo.get_all()
