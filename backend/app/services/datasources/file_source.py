from abc import abstractmethod

from backend.app.services.datasources.datasource import (
    DataSource
)


class FileSource(DataSource):
    """
    Bazowa klasa wszystkich źródeł plikowych.
    """
    @abstractmethod
    def get_data(self):
        pass