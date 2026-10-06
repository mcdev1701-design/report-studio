from pprint import pprint

from backend.app.services.datasources.unix_pipe_source import (
    UnixPipeSource
)

PIPE_PATH = "/tmp/reportstudio.pipe"

source = UnixPipeSource(
    PIPE_PATH
)

source.connect()

dataset = source.get_data()

source.disconnect()

print()
print("=== DATASET ===")
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