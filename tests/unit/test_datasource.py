from backend.app.services.datasources.datasource import (
    DataSource
)


def test_datasource_is_abstract():

    assert DataSource.__abstractmethods__