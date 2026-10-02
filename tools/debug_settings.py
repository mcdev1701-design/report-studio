from backend.app.core.settings import (
    settings
)

print()

print("SERVER:")
print(settings.mssql_server)

print()

print("DATABASE:")
print(settings.mssql_database)

print()

print("USERNAME:")
print(settings.mssql_username)

print()

print("PASSWORD:")
print(
    "*" * len(settings.mssql_password)
    if settings.mssql_password
    else None
)