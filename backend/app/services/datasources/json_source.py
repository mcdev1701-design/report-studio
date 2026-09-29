"""
Implementacja DataSource dla plików JSON.

Cel:

Odczyt danych z plików JSON
oraz zwrócenie ich do Report Studio
w ujednoliconej postaci.

Aktualny standard:

list[dict]
"""

import json

from backend.app.services.datasources.datasource import (
    DataSource
)


class JsonSource(DataSource):
    """
    DataSource dla plików JSON.
    """

    def __init__(self, file_path: str):
        """
        Inicjalizacja źródła danych.

        Args:
            file_path:
                Ścieżka do pliku JSON.
        """

        self.file_path = file_path

        self.connected = False

    def connect(self):
        """
        Nawiązanie połączenia.

        Dla pliku JSON oznacza jedynie
        sprawdzenie czy plik istnieje.
        """

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ):
            pass

        self.connected = True

    def disconnect(self):
        """
        Zamknięcie połączenia.

        Dla JSON nie ma aktywnego połączenia,
        ale zachowujemy wspólny kontrakt.
        """

        self.connected = False

    def test_connection(self):
        """
        Test dostępności pliku.

        Returns:
            bool
        """

        try:

            with open(
                self.file_path,
                "r",
                encoding="utf-8"
            ):
                pass

            return True

        except FileNotFoundError:

            return False

    def get_data(self):
        """
        Pobranie danych.

        Returns:
            list[dict]
        """

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return data