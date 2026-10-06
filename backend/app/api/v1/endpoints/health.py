"""Endpointy diagnostyczne i informacyjne aplikacji."""

from fastapi import APIRouter

from backend.app.core.logger import logger

router = APIRouter()


@router.get("/health")
def health_check():
    """Zwraca stan dostępności backendu."""
    logger.info("Wywołano endpoint health")

    return {
        "status": "OK"
    }

@router.get("/info")
def info_check():
    """
    Endpoint informacyjny.

    Cel:
        Udostępnia podstawowe informacje
        o aplikacji.

    Adres:
        GET /api/v1/info

    Zwraca:
        JSON z informacjami o aplikacji.

    Przykład odpowiedzi:

        {
            "application": "Report Studio",
            "version": "0.1.0",
            "status": "Development"
        }
    """

    logger.info("Wywołano endpoint info")

    return {
        "application": "Report Studio",
        "version": "0.1.0",
        "status": "Development"
    }