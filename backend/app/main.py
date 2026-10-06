"""
Główny punkt wejścia aplikacji Report Studio.

Plik uruchamiany jest przez serwer Uvicorn.

Przykład uruchomienia:

    uvicorn backend.app.main:app --reload

Odpowiedzialności:

    - utworzenie obiektu FastAPI,
    - rejestracja endpointów,
    - konfiguracja Swagger UI,
    - konfiguracja routingu.
"""

from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.app.api.v1.endpoints.health import (
    router as health_router
)
from backend.app.core.settings import settings
from backend.app.core.logger import logger
from backend.app.core.lifecycle import lifespan

logger.info("Uruchamianie aplikacji Report Studio")

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan
)

app.mount(
    "/static",
    StaticFiles(directory="backend/app/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="backend/app/templates"
)

app.include_router(
    health_router,
    prefix=settings.api_prefix,
    tags=["Health"]
)


@app.get("/", response_class=HTMLResponse)
def root(request: Request):
    """
    Strona główna aplikacji.
    """

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
