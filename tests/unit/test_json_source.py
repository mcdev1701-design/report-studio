"""
Unit tests for the JsonSource class.
"""
from backend.app.services.datasources.json_source import (
    JsonSource
)


def test_json_source_connection():
    """
    Test połączenia z plikiem JSON.
    """
    source = JsonSource(
        "examples/sample_data.json"
    )

    assert source.test_connection() is True

def test_json_source_get_data():
    """
    Test pobrania danych z pliku JSON.
    """
    source = JsonSource(
        "examples/sample_data.json"
    )

    source.connect()

    data = source.get_data()

    source.disconnect()

    assert isinstance(data, list)

    assert len(data) == 2