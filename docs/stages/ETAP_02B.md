# ETAP_02B

## Nazwa

Source Implementations

## Branch

feature/etap-02b-source-implementations

## Status

W realizacji

## Cel

Implementacja kolejnych źródeł danych opartych o kontrakt DataSource.

## Zakres

- CSVSource
- ExcelSource
- przygotowanie pod MSSQLSource

## Kryteria ukończenia

- CSVSource zwraca Dataset
- ExcelSource zwraca Dataset
- testy przechodzą poprawnie
- architektura pozostaje spójna

### Dodano

- CSVSource
- sample_data.csv
- test_csv_source.py

### Refaktoryzacja

- ujednolicono JsonSource
- connect() wykorzystuje test_connection()
- source_type zapisany małymi literami

### Wynik testów

✅ 10 passed