"""
Implementacja SQLSource dla Microsoft SQL Server.

Cel:

Połączenie z bazą SQL Server
oraz wykonywanie zapytań SQL.

Konfiguracja:

.env
↓
Settings
↓
MSSQLSource
"""

from backend.app.core.settings import settings

from backend.app.services.datasources.sql_source import (
    SQLSource
)

from backend.app.models.dataset import Dataset


class MSSQLSource(SQLSource):
    """
    Implementacja SQLSource dla MSSQL.
    """

    def __init__(self):

        super().__init__()

    def build_connection_string(self) -> str:
        """
        Buduje connection string.

        Aktualnie zwraca jego wersję testową.
        """

        return (
            f"mssql://"
            f"{settings.mssql_username}:"
            f"{settings.mssql_password}@"
            f"{settings.mssql_server}/"
            f"{settings.mssql_database}"
        )

    def connect(self):
        """
        Nawiązanie połączenia.

        Implementacja zostanie dodana
        po integracji z SQLAlchemy.
        """

        raise NotImplementedError(
            "connect() not implemented yet."
        )

    def disconnect(self):
        """
        Zamknięcie połączenia.

        Implementacja zostanie dodana
        po integracji z SQLAlchemy.
        """

        raise NotImplementedError(
            "disconnect() not implemented yet."
        )

    def test_connection(self):
        """
        Test połączenia.

        Implementacja zostanie dodana
        po integracji z SQLAlchemy.
        """

        raise NotImplementedError(
            "test_connection() not implemented yet."
        )

    def execute_query(
        self,
        query: str
    ) -> Dataset:
        """
        Wykonanie zapytania SQL.

        Implementacja zostanie dodana
        po integracji z SQLAlchemy.
        """

        raise NotImplementedError(
            "execute_query() not implemented yet."
        )