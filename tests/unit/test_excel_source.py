"""
Unit tests for ExcelSource.
"""

from datetime import datetime

import pytest

from backend.app.models.dataset import Dataset

from backend.app.services.datasources.excel_source import (
    ExcelSource
)


def test_excel_source_connection():
    """
    Test połączenia z plikiem Excel.
    """
    source = ExcelSource(
        "examples/sample_data.xlsx"
    )

    assert source.test_connection() is True


def test_excel_source_requires_connection():
    """
    Test sprawdzający, czy metoda get_data() wymaga połączenia.
    """
    source = ExcelSource(
        "examples/sample_data.xlsx"
    )

    with pytest.raises(RuntimeError):

        source.get_data()


def test_excel_source_get_data():
    """
    Test pobierania danych z pliku Excel.
    """
    source = ExcelSource(
        "examples/sample_data.xlsx"
    )

    source.connect()

    dataset = source.get_data()

    source.disconnect()

    assert isinstance(
        dataset,
        Dataset
    )

    assert dataset.name == "Excel Dataset"

    assert dataset.source_type == "excel"

    assert dataset.source_name == (
        "examples/sample_data.xlsx"
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