from backend.app.services.datasources.datasource import (
    DataSource
)


def test_datasource_is_abstract():
    """
    Sprawdzenie, czy klasa DataSource jest abstrakcyjna.
    """
    assert DataSource.__abstractmethods__