"""
Ręczne testowanie ExcelSource.

Uruchomienie:

python tools/debug_excel_source.py
"""

from pprint import pprint

from backend.app.services.datasources.excel_source import (
    ExcelSource
)

source = ExcelSource(
    "examples/sample_data.xlsx"
)

source.connect()

dataset = source.get_data()

source.disconnect()

print("\n=== DATASET ===\n")

print(dataset)

print("\n=== COLUMNS ===\n")

print(dataset.columns)

print("\n=== ROWS ===\n")

pprint(dataset.rows)