from backend.app.services.datasources.file_source import (
    FileSource
)


def test_file_source_is_abstract():
    """
    Test sprawdzający, czy klasa FileSource jest klasą abstrakcyjną
    i nie można jej zainicjalizować.
    """
    assert (
        FileSource.__abstractmethods__
    )