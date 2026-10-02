"""
Implementacja DataSource dla plików CSV.

Cel:

Odczyt danych z plików CSV
oraz zwrócenie ich do Report Studio
w postaci Dataset.

Aktualny standard:

Dataset
"""

from csv import DictReader

from datetime import datetime

"""
Abstrakcyjna definicja źródła danych.
"""
from backend.app.services.datasources.file_source import (
    FileSource
)

from backend.app.models.dataset import Dataset

class CSVSource(FileSource):
    """
    DataSource dla plików CSV.
    """

    def __init__(self, file_path: str):
        """
        Inicjalizacja źródła danych.

        Args:
            file_path:
                Ścieżka do pliku CSV.
        """

        self.file_path = file_path

        self.connected = False

    def connect(self):
        """
        Walidacja dostępności pliku CSV.
        """

        if not self.test_connection():

            raise FileNotFoundError(
                self.file_path
            )

        self.connected = True

    def disconnect(self):
        """
        Zamyka źródło danych.

        Dla CSV nie ma aktywnego połączenia,
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
        Pobiera dane z pliku CSV.

        Returns:
            Dataset
        """

        if not self.connected:

            raise RuntimeError(
                "DataSource is not connected."
            )

        rows = []

        with open(
            self.file_path,
            "r",
            encoding="utf-8"
        ) as file:

            reader = DictReader(file)

            for row in reader:

                rows.append(row)

        return Dataset(
            name="CSV Dataset",
            source_type="csv",
            source_name=self.file_path,
            loaded_at=datetime.now(),
            rows=rows
        )