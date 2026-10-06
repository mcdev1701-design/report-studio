"""
Implementacja PipeSource dla Unix FIFO.

Obsługiwane środowiska:

- Linux
- WSL
- macOS
"""

from datetime import datetime
import json
import os

from backend.app.models.dataset import Dataset

from backend.app.services.datasources.pipe_source import (
    PipeSource
)


class UnixPipeSource(PipeSource):
    """Odczytuje rekordy JSON z Unix FIFO."""

    def __init__(
        self,
        pipe_path: str
    ):
        """Tworzy źródło dla FIFO wskazanego ścieżką."""
        self.pipe_path = pipe_path

        self.connected = False

    def connect(self):
        """Sprawdza istnienie ścieżki i oznacza źródło jako połączone."""

        if not self.test_connection():

            raise FileNotFoundError(
                self.pipe_path
            )

        self.connected = True

    def disconnect(self):
        """Oznacza źródło jako odłączone."""
        self.connected = False

    def test_connection(self):
        """Sprawdza, czy ścieżka FIFO istnieje."""
        return os.path.exists(
            self.pipe_path
        )

    def get_data(self) -> Dataset:
        """Blokująco odczytuje JSON z FIFO do końca strumienia."""

        if not self.connected:

            raise RuntimeError(
                "DataSource is not connected."
            )

        with open(
            self.pipe_path,
            "r",
            encoding="utf-8"
        ) as fifo:

            content = fifo.read()

        rows = json.loads(content)

        return Dataset(
            name="Unix Pipe Dataset",
            source_type="pipe",
            source_name=self.pipe_path,
            loaded_at=datetime.now(),
            rows=rows
        )