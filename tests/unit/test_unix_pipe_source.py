from backend.app.services.datasources.unix_pipe_source import (
    UnixPipeSource
)


def test_unix_pipe_source_creation():

    source = UnixPipeSource(
        "/tmp/reportstudio.pipe"
    )

    assert source is not None
