"""
Unit tests for the JsonSource class.
"""

from datetime import datetime

from backend.app.models.dataset import Dataset

from backend.app.services.datasources.json_source import (
    JsonSource
)


def test_json_source_connection():

    source = JsonSource(
        "examples/sample_data.json"
    )

    assert source.test_connection() is True


def test_json_source_get_data():

    source = JsonSource(
        "examples/sample_data.json"
    )

    source.connect()

    dataset = source.get_data()

    source.disconnect()

    assert isinstance(
        dataset,
        Dataset
    )

    assert dataset.name == "JSON Dataset"

    assert dataset.source_type == "json"

    assert dataset.source_name == (
        "examples/sample_data.json"
    )

    assert isinstance(
        dataset.loaded_at,
        datetime
    )

    assert dataset.row_count == 2

    assert dataset.columns == [
        "id",
        "name",
        "price"
    ]