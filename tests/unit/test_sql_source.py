from backend.app.services.datasources.sql_source import (
    SQLSource
)


def test_sql_source_is_abstract():
    """
    Testuje, czy klasa SQLSource jest klasą abstrakcyjną.
    """
    assert (
        SQLSource.__abstractmethods__
    )