"""
Abstrakcyjna klasa bazowa dla źródeł danych SQL.

Cel:

Wspólna logika dla:

- MSSQLSource
- PostgreSQLSource
- SQLiteSource

SQLSource nie zna konkretnego silnika bazy danych.

Implementacje pochodne odpowiadają za:

- budowę connection string,
- konfigurację połączenia.
"""

from abc import abstractmethod

from backend.app.models.dataset import Dataset

from backend.app.services.datasources.datasource import (
    DataSource
)


class SQLSource(DataSource):
    """
    Bazowa klasa wszystkich źródeł SQL.
    """

    def __init__(self):

        self.connection = None

        self.connected = False

    @abstractmethod
    def build_connection_string(self) -> str:
        """
        Zwraca connection string dla
        konkretnej implementacji SQL.

        Przykłady:

        - MSSQL
        - PostgreSQL
        - SQLite
        """
        pass

    @abstractmethod
    def connect(self):
        """
        Nawiązanie połączenia.
        """
        pass

    @abstractmethod
    def disconnect(self):
        """
        Zamknięcie połączenia.
        """
        pass

    @abstractmethod
    def test_connection(self):
        """
        Test połączenia.
        """
        pass

    @abstractmethod
    def execute_query(
        self,
        query: str
    ) -> Dataset:
        """
        Wykonanie zapytania SQL.

        Parametry:
            query - zapytanie SELECT

        Wynik:
            Dataset
        """
        pass