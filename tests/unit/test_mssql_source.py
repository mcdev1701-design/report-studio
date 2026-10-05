from backend.app.core.settings import settings
from backend.app.services.datasources.mssql_source import (
    MSSQLSource
)


def test_mssql_source_creation():
    """
    Testuje utworzenie instancji MSSQLSource.
    """
    source = MSSQLSource()

    assert source is not None


def test_mssql_connection_string():
    """
    Testuje budowanie ciągu połączenia dla MSSQLSource.
    """
    source = MSSQLSource()

    connection_string = (
        source.build_connection_string()
    )

    assert isinstance(
        connection_string,
        str
    )

    assert "mssql+pytds://" in connection_string

def test_mssql_source_connection_string():
    """
    Testuje, czy connection string zawiera poprawne informacje.
    """
    source = MSSQLSource()

    connection_string = (
        source.build_connection_string()
    )

    assert isinstance(
        connection_string,
        str
    )

    assert (
        settings.mssql_server
        in connection_string
    )

def test_mssql_execute_query():

    source = MSSQLSource()

    source.connect()

    dataset = source.execute_query(
        f"""
        SELECT TOP 1 *
        FROM {settings.mssql_schema}.Products
        """
    )

    source.disconnect()

    assert dataset.source_type == "mssql"

    assert dataset.row_count >= 1