"""Helpers for creating the FastAPI instance."""

from fastapi import FastAPI

from routers.release_router import router as release_router

app = FastAPI(title="Python Requests Releases API")
app.include_router(release_router)
