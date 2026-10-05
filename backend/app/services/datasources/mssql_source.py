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

from sqlalchemy import create_engine
from sqlalchemy import text

from datetime import datetime

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

        self.engine = None

    def build_connection_string(self) -> str:
        """
        Buduje connection string.

        Aktualnie zwraca jego wersję testową.
        """

        return (
            f"mssql+pytds://"
            f"{settings.mssql_username}:"
            f"{settings.mssql_password}@"
            f"{settings.mssql_server}/"
            f"{settings.mssql_database}"
        )

    def connect(self):
        """
        Nawiązanie połączenia z bazą danych.
        """

        connection_string = self.build_connection_string()

        self.engine = create_engine(connection_string)

        self.connection = self.engine.connect()

        self.connected = True

    def disconnect(self):
        """
        Zamknięcie połączenia.
        """

        if self.connection:
            self.connection.close()

        self.connected = False

    def test_connection(self):

        try:

            self.connect()

            result = self.connection.execute(
                text("SELECT 1")
            )

            result.scalar()

            self.disconnect()

            return True

        except Exception as exc:
            print(
                f"Test połączenia nie powiódł się: {exc}"
            )
            return False

    def execute_query(
        self,
        query: str
    ) -> Dataset:
        """
        Wykonanie zapytania SQL.

        Args:
            query:
                Zapytanie SQL.

        Returns:
            Dataset
        """

        if not self.connected:

            raise RuntimeError(
                "DataSource is not connected."
            )

        result = self.connection.execute(
            text(query)
        )

        rows = []

        column_names = result.keys()

        for row in result:

            rows.append(
                dict(
                    zip(
                        column_names,
                        row
                    )
                )
            )

        return Dataset(
            name="MSSQL Dataset",
            source_type="mssql",
            source_name=settings.mssql_database,
            loaded_at=datetime.now(),
            rows=rows
        )