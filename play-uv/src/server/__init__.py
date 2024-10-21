"""Creates and loads the uvicorn server."""

from uvicorn import Config as UConfig
from uvicorn import Server as UServer


async def serve() -> None:
    """
    Serve the API.

    Args:
        reload (bool): Reload the server on file changes, false by default.
    """
    config = UConfig(
        app="api:app",
        port=8000,
        log_level="info",
        workers=16,
    )
    server = UServer(config)
    await server.serve()
