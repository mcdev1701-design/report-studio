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

    def __init__(
        self,
        pipe_path: str
    ):
        self.pipe_path = pipe_path

        self.connected = False

    def connect(self):
        """
        Weryfikacja istnienia FIFO.
        """

        if not self.test_connection():

            raise FileNotFoundError(
                self.pipe_path
            )

        self.connected = True

    def disconnect(self):

        self.connected = False

    def test_connection(self):

        return os.path.exists(
            self.pipe_path
        )

    def get_data(self) -> Dataset:

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