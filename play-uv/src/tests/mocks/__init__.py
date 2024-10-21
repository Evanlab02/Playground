"""Contains mocks for the tests."""

from schemas.release import GithubRelease

MOCK_RELEASES: list[GithubRelease] = [
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
