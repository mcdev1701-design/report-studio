"""
Testy CSVSource.

Cel:

Weryfikacja poprawności implementacji
DataSource dla plików CSV.
"""

from datetime import datetime

import pytest

from backend.app.models.dataset import Dataset

from backend.app.services.datasources.csv_source import (
    CSVSource
)


def test_csv_source_connection():
    """
    Sprawdzenie dostępności pliku CSV.
    """

    source = CSVSource(
        "examples/sample_data.csv"
    )

    assert source.test_connection() is True

def test_csv_source_get_data():
    """
    Pobranie danych z pliku CSV.
    """

    source = CSVSource(
        "examples/sample_data.csv"
    )

    source.connect()

    dataset = source.get_data()

    source.disconnect()

    assert isinstance(
        dataset,
        Dataset
    )

    assert dataset.name == "CSV Dataset"

    assert dataset.source_type == "csv"

    assert dataset.source_name == (
        "examples/sample_data.csv"
    )

    assert isinstance(
        dataset.loaded_at,
        datetime
    )

    assert dataset.row_count == 3

    assert dataset.columns == [
        "id",
        "name",
        "price"
    ]

def test_csv_source_requires_connection():
    """ 
    Próba pobrania danych bez uprzedniego połączenia.   
    """
    
    source = CSVSource(
    "examples/sample_data.csv"
    )

    with pytest.raises(RuntimeError):

        source.get_data()