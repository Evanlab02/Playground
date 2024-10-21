"""Contains the the release repository."""

import json
from typing import Any

from data.interfaces.irelease_repo import IReleaseRepo
from errors.data import DataDoesNotExistError, DataInvalidError


class ReleaseRepo(IReleaseRepo):
    """Contains the logic for the release repository."""

    def __init__(self) -> None:
        """Init the class."""
        super().__init__()

    def get_all(self) -> list[dict[str, Any]]:
        """
        Get the latest releases for the requests package.

        Returns:
            releases (list[dict[str, Any]]): 30 latest releases for the package.
        """
        data: list[dict[str, Any]] = []

        try:
            with open("./src/data/data.json", "r", encoding="UTF-8") as file:
                data = json.load(file)
        except FileNotFoundError as e:
            raise DataDoesNotExistError(e)

        if not isinstance(data, list):
            raise DataInvalidError(TypeError())

        return data
