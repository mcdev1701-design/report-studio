from unittest.mock import patch

from backend.app.models.dataset import Dataset

from backend.app.services.datasources.stdin_source import (
    STDINSource
)


def test_stdin_source_get_data():

    source = STDINSource()

    source.connect()

    fake_input = """
    [
        {
            "id": 1,
            "name": "Produkt A"
        }
    ]
    """

    with patch(
        "sys.stdin.read",
        return_value=fake_input
    ):

        dataset = source.get_data()

    source.disconnect()

    assert isinstance(
        dataset,
        Dataset
    )

    assert dataset.source_type == "stdin"

    assert dataset.row_count == 1