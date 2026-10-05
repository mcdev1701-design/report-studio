from pprint import pprint

from backend.app.services.datasources.mssql_source import (
    MSSQLSource
)

from backend.app.core.settings import settings

source = MSSQLSource()

source.connect()

schema = settings.mssql_schema

dataset = source.execute_query(
    f"""
    SELECT *
    FROM {schema}.Products
    """
)

source.disconnect()

print()
print("=== DATASET ===")
print()

print(dataset)

print()
print("=== COLUMNS ===")
print(dataset.columns)

print()
print("=== ROW COUNT ===")
print(dataset.row_count)

print()
print("=== ROWS ===")

pprint(dataset.rows)