from abc import abstractmethod

from backend.app.services.datasources.datasource import (
    DataSource
)


class SQLSource(DataSource):
    """
    Bazowa klasa źródeł SQL.
    """

    def __init__(self):

        self.connection = None

        self.connected = False

    @abstractmethod
    def build_connection_string(self):
        """
        Zwraca connection string
        dla konkretnego silnika.
        """
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def test_connection(self):
        pass

    @abstractmethod
    def execute_query(
        self,
        query: str
    ):
        pass