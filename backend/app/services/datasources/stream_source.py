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
    """Wspólny kontrakt dla źródeł odczytujących dane ze strumienia."""

    @abstractmethod
    def get_data(self) -> Dataset:
        """Odczytuje rekordy ze strumienia i zwraca je jako Dataset."""
        pass