"""
Implementacja DataSource dla plików JSON.

Cel:

Odczyt danych z plików JSON
oraz zwrócenie ich do Report Studio
w ujednoliconej postaci.

Aktualny standard:

Dataset
"""

import json

from datetime import datetime

"""
Abstrakcyjna definicja źródła danych.
"""
from backend.app.services.datasources.file_source import (
    FileSource
)

from backend.app.models.dataset import Dataset

class JsonSource(FileSource):
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
        Walidacja dostępności pliku JSON.
        """

        if not self.test_connection():

            raise FileNotFoundError(
                self.file_path
            )

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

    def get_data(self) -> Dataset:
        """
        Pobranie danych z pliku JSON.   
        """
        if not self.connected:

            raise RuntimeError(
                "DataSource is not connected."
            )

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return Dataset(
            name="JSON Dataset",
            source_type="json",
            source_name=self.file_path,
            loaded_at=datetime.now(),
            rows=data
        )