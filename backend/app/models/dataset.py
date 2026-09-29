"""
Dataset projektu Report Studio.

Cel:

Przechowywanie danych pobranych
ze źródeł danych oraz metadanych.
"""

from dataclasses import dataclass
from dataclasses import field
from datetime import datetime


@dataclass
class Dataset:
    """
    Reprezentacja danych pobranych ze źródła danych.    
    """
    name: str

    source_type: str

    source_name: str

    loaded_at: datetime = field(
	        default_factory=datetime.now() # jeżeli użytkownik nie poda daty, to domyślnie będzie aktualna data i czas
        )

    rows: list[dict] = field(default_factory=list) # jeżeli użytkownik nie poda listy, to domyślnie będzie pusta lista

    @property
    def row_count(self) -> int:
        """
        Liczba rekordów.
        """

        return len(self.rows)

    @property
    def columns(self):
        """
        Lista kolumn w ujednoliconej postaci.
        """
        if not self.rows:
            return []

        return list(
            self.rows[0].keys()
        )