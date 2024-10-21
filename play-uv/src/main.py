"""Entry point for the application."""

import asyncio
import sys

from server import serve


async def main(args: list[str]) -> None:
    """Entry point for the application."""
    await serve()


if __name__ == "__main__":
    args = sys.argv
    args.pop(0)
    asyncio.run(main(args))
