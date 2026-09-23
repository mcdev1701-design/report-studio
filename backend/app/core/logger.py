"""
Centralny system logowania aplikacji.

Cel:
    Ujednolicenie sposobu logowania zdarzeń
    we wszystkich modułach projektu.

Przykładowe zastosowania:

    - start aplikacji,
    - błędy MSSQL,
    - eksport PDF,
    - import danych,
    - komunikacja Pipe.

W przyszłości:

    - zapis do pliku,
    - log rotation,
    - różne poziomy logowania,
    - logowanie do bazy danych.
"""

import logging


def setup_logger() -> logging.Logger:
    """
    Tworzy i konfiguruje główny logger aplikacji.

    Returns:
        logging.Logger
    """

    # Tworzymy logger aplikacji.
    logger = logging.getLogger("report_studio")

    # Ustawiamy minimalny poziom logowania.
    logger.setLevel(logging.INFO)

    # Zapobiega wielokrotnemu dodawaniu handlerów
    # podczas działania funkcji reload w Uvicorn.
    if not logger.handlers:

        # Obsługa wyświetlania logów w konsoli.
        console_handler = logging.StreamHandler()

        # Format komunikatów logów.
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger


# Globalna instancja loggera.
logger = setup_logger()