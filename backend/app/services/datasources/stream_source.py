"""
Bazowa klasa źródeł strumieniowych.

Przykłady:

- STDINSource
- NamedPipeSource
"""

from abc import abstractmethod

from backend.app.models.dataset import Dataset

from backend.app.services.datasources.datasource import (
    DataSource
)


class StreamSource(DataSource):

    @abstractmethod
    def get_data(self) -> Dataset:
        """
        Odczyt danych ze strumienia.
        """
        pass