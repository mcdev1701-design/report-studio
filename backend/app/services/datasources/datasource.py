"""
Abstrakcyjna definicja źródła danych.

Każde źródło danych w Report Studio
musi implementować ten kontrakt.

Przykłady:

- MSSQLSource
- CSVSource
- ExcelSource
- JsonSource
- PipeSource
"""

from abc import ABC
from abc import abstractmethod


class DataSource(ABC):
    """
    Bazowa klasa wszystkich źródeł danych.
    """

    @abstractmethod
    def connect(self):
        """
        Nawiązanie połączenia ze źródłem danych.
        """
        pass

    @abstractmethod
    def disconnect(self):
        """
        Zamknięcie połączenia ze źródłem danych.
        """
        pass

    @abstractmethod
    def test_connection(self):
        """
        Test dostępności źródła danych.
        """
        pass

    @abstractmethod
    def get_data(self):
        """
        Pobranie danych.

        Zwraca:

        Dane w ujednoliconej postaci.
        """
        pass