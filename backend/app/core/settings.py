"""
Konfiguracja aplikacji Report Studio.

Cel:
    Centralne przechowywanie ustawień projektu.

Dlaczego to robimy?

    Dzięki temu wszystkie ustawienia
    znajdują się w jednym miejscu.

W przyszłości:

    - MSSQL
    - Logging
    - Security
    - Environment Variables
    - PDF Engine
"""

from dataclasses import dataclass


@dataclass
class Settings:
    """
    Główna konfiguracja aplikacji.

    Dataclass automatycznie generuje:

    - __init__()
    - __repr__()
    - porównania obiektów

    Dzięki temu kod jest prostszy
    i bardziej czytelny.
    """

    app_name: str = "Report Studio"

    app_version: str = "0.1.0"

    api_prefix: str = "/api/v1"


# Tworzymy pojedynczą instancję konfiguracji.
settings = Settings()