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

# Import konfiguracji aplikacji.
from backend.app.core.settings import settings

# Import routera endpointów zdrowia aplikacji.
from backend.app.api.v1.endpoints.health import (
    router as health_router
)

# Import loggera aplikacji.
from backend.app.core.logger import logger

# Import obsługi cyklu życia aplikacji.
from backend.app.core.lifecycle import lifespan

# Import obsługi szablonów HTML.
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

logger.info("Uruchamianie aplikacji Report Studio")

# ==================================================
# FASTAPI APPLICATION
# ==================================================
#
# Tworzymy główny obiekt aplikacji.
#
# FastAPI wykorzysta te informacje między innymi
# do wygenerowania dokumentacji Swagger.
#
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    lifespan=lifespan
)

#==================================================
# STATIC FILES CONFIGURATION
#=================================================
app.mount(
    "/static",
    StaticFiles(directory="backend/app/static"),
    name="static"
)

#=================================================
# TEMPLATES CONFIGURATION
#=================================================
templates = Jinja2Templates(
    directory="backend/app/templates"
)

# ==================================================
# ROUTER REGISTRATION
# ==================================================
#
# Rejestrujemy endpointy znajdujące się
# w pliku health.py
#
# Efekt końcowy:
#
# GET /api/v1/health
#
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
