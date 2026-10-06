"""Wspólny model danych zwracany przez źródła Report Studio."""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Dataset:
    """Rekordy pobrane ze źródła wraz z opisującymi je metadanymi."""

    name: str

    source_type: str

    source_name: str

    loaded_at: datetime = field(default_factory=datetime.now)

    rows: list[dict] = field(default_factory=list)

    @property
    def row_count(self) -> int:
        """Zwraca liczbę rekordów w zestawie danych."""
        return len(self.rows)

    @property
    def columns(self):
        """Zwraca nazwy kolumn na podstawie pierwszego rekordu."""
        if not self.rows:
            return []

        return list(
            self.rows[0].keys()
        )