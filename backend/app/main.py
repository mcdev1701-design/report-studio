"""
Główny punkt wejścia aplikacji.
"""

from fastapi import FastAPI

from app.config import (
    APP_NAME,
    APP_VERSION
)

from app.api.v1.endpoints.health import router as health_router

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

app.include_router(
    health_router,
    prefix="/api/v1",
    tags=["Health"]
)


@app.get("/")
def root():
    """
    Główny endpoint aplikacji.
    """

    return {
        "application": APP_NAME,
        "version": APP_VERSION
    }