"""
Bazowa klasa źródeł SQL.
"""

from abc import abstractmethod

from backend.app.services.datasources.datasource import (
    DataSource
)

from backend.app.models.dataset import Dataset


class SQLSource(DataSource):

    @abstractmethod
    def build_connection_string(self) -> str:
        pass

    @abstractmethod
    def execute_query(
        self,
        query: str
    ) -> Dataset:
        pass