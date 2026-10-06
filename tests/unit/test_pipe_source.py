from backend.app.services.datasources.pipe_source import (
    PipeSource
)


def test_pipe_source_is_abstract():

    assert PipeSource.__abstractmethods__