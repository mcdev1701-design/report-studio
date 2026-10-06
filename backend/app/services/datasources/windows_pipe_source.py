"""
Implementacja PipeSource dla Windows Named Pipe.
"""

from datetime import datetime
import json

import win32file

from backend.app.models.dataset import Dataset

from backend.app.services.datasources.pipe_source import (
    PipeSource
)


class WindowsPipeSource(PipeSource):
    """Odbiera rekordy JSON z Windows Named Pipe."""

    def __init__(
        self,
        pipe_name: str
    ):
        """Tworzy źródło wskazujące nazwę Windows Named Pipe."""
        self.pipe_name = pipe_name

        self.pipe_handle = None

        self.connected = False

    def connect(self):
        """Otwiera istniejący Named Pipe do odczytu."""

        self.pipe_handle = win32file.CreateFile(
            self.pipe_name,
            win32file.GENERIC_READ,
            0,
            None,
            win32file.OPEN_EXISTING,
            0,
            None
        )

        self.connected = True

    def disconnect(self):
        """Zamyka uchwyt Pipe, jeśli połączenie zostało otwarte."""

        if self.pipe_handle:

            win32file.CloseHandle(
                self.pipe_handle
            )

        self.connected = False

    def test_connection(self):
        """Próbuje otworzyć i zamknąć Pipe, zwracając wynik testu."""
        try:

            self.connect()

            self.disconnect()

            return True

        except Exception as e:
            print(
                f"Connection test failed: {e}"
            )
            return False

    def get_data(self) -> Dataset:
        """Odczytuje do 65 536 bajtów JSON i zwraca je jako Dataset."""

        if not self.connected:

            raise RuntimeError(
                "DataSource is not connected."
            )

        result = win32file.ReadFile(
            self.pipe_handle,
            65536
        )

        content = result[1].decode(
            "utf-8"
        )

        rows = json.loads(content)

        return Dataset(
            name="Windows Pipe Dataset",
            source_type="pipe",
            source_name=self.pipe_name,
            loaded_at=datetime.now(),
            rows=rows
        )