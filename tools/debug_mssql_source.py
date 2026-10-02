"""
Debug MSSQLSource.
"""

from backend.app.services.datasources.mssql_source import (
    MSSQLSource
)

from backend.app.core.settings import settings

source = MSSQLSource()

print()
print("=== CONNECTION STRING ===")
print()

# print(
#     source.build_connection_string()
# )

print(
    source.build_connection_string().replace(
        settings.mssql_password,
        "********"
    )
)