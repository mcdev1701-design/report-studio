"""
Implementacja StreamSource
dla standardowego wejścia (STDIN).
"""
from datetime import datetime
import json
import sys

from backend.app.models.dataset import Dataset

from backend.app.services.datasources.stream_source import (
    StreamSource
)


class STDINSource(StreamSource):

    def __init__(self):

        self.connected = False

    def connect(self):

        self.connected = True

    def disconnect(self):

        self.connected = False

    def test_connection(self):

        return True

    def get_data(self) -> Dataset:

        if not self.connected:

            raise RuntimeError(
                "DataSource is not connected."
            )

        content = sys.stdin.read()

        rows = json.loads(content)

        return Dataset(
            name="STDIN Dataset",
            source_type="stdin",
            source_name="stdin",
            loaded_at=datetime.now(),
            rows=rows
        )