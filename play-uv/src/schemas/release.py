"""Contains the release schemas."""

from pydantic import BaseModel


class GithubRelease(BaseModel):
    """A single release."""

    url: str
    tag_name: str
    name: str
    prerelease: bool
    created_at: str
    published_at: str
