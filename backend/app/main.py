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
from backend.app.config import (
    APP_NAME,
    APP_VERSION,
    API_PREFIX
)

# Import routera endpointów zdrowia aplikacji.
from backend.app.api.v1.endpoints.health import (
    router as health_router
)

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
    title=APP_NAME,
    version=APP_VERSION
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
    prefix=API_PREFIX,
    tags=["Health"]
)


@app.get("/")
def root():
    """
    Główny endpoint aplikacji.

    Cel:
        Szybkie sprawdzenie czy aplikacja działa.

    Adres:
        GET /

    Przykładowa odpowiedź:

        {
            "application": "Report Studio",
            "version": "0.1.0"
        }
    """

    return {
        "application": APP_NAME,
        "version": APP_VERSION
    }
