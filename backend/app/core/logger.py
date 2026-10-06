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

    logger = logging.getLogger("report_studio")
    logger.setLevel(logging.INFO)

    # Uvicorn reload może ponownie importować moduł; nie duplikuj wtedy handlera.
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )

        console_handler.setFormatter(formatter)

        logger.addHandler(console_handler)

    return logger


logger = setup_logger()