"""
Bazowa klasa źródeł Pipe.

Źródła Pipe umożliwiają komunikację
pomiędzy procesami.

Implementacje:

- WindowsPipeSource
- UnixPipeSource
"""

from abc import abstractmethod

from backend.app.models.dataset import Dataset

from backend.app.services.datasources.stream_source import (
    StreamSource
)


class PipeSource(StreamSource):

    @abstractmethod
    def connect(self):
        """
        Nawiązanie połączenia z Pipe.
        """
        pass

    @abstractmethod
    def disconnect(self):
        """
        Zamknięcie Pipe.
        """
        pass

    @abstractmethod
    def test_connection(self):
        """
        Weryfikacja dostępności Pipe.
        """
        pass

    @abstractmethod
    def get_data(self) -> Dataset:
        """
        Odczyt danych z Pipe.

        Returns:
            Dataset
        """
        pass