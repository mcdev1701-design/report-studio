"""
Bazowa klasa źródeł Pipe.

Źródła Pipe umożliwiają komunikację
proces ↔ proces.

Przykłady:

- Windows Pipe
- Unix FIFO
"""

from abc import abstractmethod

from backend.app.models.dataset import Dataset

from backend.app.services.datasources.stream_source import (
    StreamSource
)


class PipeSource(StreamSource):
    """
    Bazowa klasa źródeł Pipe.
    """
    @abstractmethod
    def get_data(self) -> Dataset:
        """
        Odczyt danych z Pipe.
        """
        pass