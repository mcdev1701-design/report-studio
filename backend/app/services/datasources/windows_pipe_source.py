"""
Windows Named Pipe Source.
"""

import json

from backend.app.models.dataset import Dataset

from backend.app.services.datasources.pipe_source import (
    PipeSource
)


class WindowsPipeSource(PipeSource):

    def __init__(
        self,
        pipe_name: str
    ):
        self.pipe_name = pipe_name

        self.connected = False

    def connect(self):
        raise NotImplementedError()

    def disconnect(self):
        raise NotImplementedError()

    def test_connection(self):
        raise NotImplementedError()

    def get_data(self) -> Dataset:
        raise NotImplementedError()