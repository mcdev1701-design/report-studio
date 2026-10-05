from backend.app.services.datasources.stdin_source import (
    STDINSource
)

source = STDINSource()

source.connect()

dataset = source.get_data()

source.disconnect()

print()
print(dataset)