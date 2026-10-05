from backend.app.models.dataset import Dataset

from backend.app.services.datasources.json_source import (
    JsonSource
)

from backend.app.services.datasources.csv_source import (
    CSVSource
)

from backend.app.services.datasources.excel_source import (
    ExcelSource
)


def test_all_file_sources_return_dataset():

    json_source = JsonSource(
        "examples/sample_data.json"
    )

    csv_source = CSVSource(
        "examples/sample_data.csv"
    )

    excel_source = ExcelSource(
        "examples/sample_data.xlsx"
    )

    json_source.connect()
    csv_source.connect()
    excel_source.connect()

    json_dataset = json_source.get_data()
    csv_dataset = csv_source.get_data()
    excel_dataset = excel_source.get_data()

    assert isinstance(
        json_dataset,
        Dataset
    )

    assert isinstance(
        csv_dataset,
        Dataset
    )

    assert isinstance(
        excel_dataset,
        Dataset
    )