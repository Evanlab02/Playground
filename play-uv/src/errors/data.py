"""Contains the custom repository exceptions for the application."""


class DataInvalidError(Exception):
    """Data invalid exception."""

    def __init__(self, *args: object) -> None:
        """Init the exception."""
        super().__init__(*args)


class DataDoesNotExistError(Exception):
    """Data does not exist exception."""

    def __init__(self, *args: object) -> None:
        """Init the exception."""
        super().__init__(*args)
