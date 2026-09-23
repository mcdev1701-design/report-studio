"""
Obsługa cyklu życia aplikacji.

Cel:
    Reakcja na uruchomienie oraz zamknięcie aplikacji.

W przyszłości:

    - inicjalizacja bazy danych,
    - połączenie MSSQL,
    - cache,
    - weryfikacja katalogów eksportu.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from backend.app.core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Obsługa startu i zamknięcia aplikacji.

    FastAPI wywoła kod przed 'yield'
    podczas startu aplikacji.

    Kod po 'yield' zostanie wykonany
    podczas zamykania aplikacji.
    """

    logger.info("=== START REPORT STUDIO ===")

    yield

    logger.info("=== STOP REPORT STUDIO ===")