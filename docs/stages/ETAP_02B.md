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

### Dodano

- CSVSource
- ExcelSource
- sample_data.csv
- sample_data.xlsx
- test_csv_source.py
- test_excel_source.py

### Refaktoryzacja

- ujednolicono implementacje JsonSource, CSVSource i ExcelSource
- connect() wykorzystuje test_connection()
- get_data() wymaga aktywnego połączenia
- source_type zapisany małymi literami

### Rezultat

JSON, CSV oraz Excel zwracają wspólny model Dataset.

### Wynik testów

✅ 13 passed

### Przygotowanie MSSQLSource

- dodano obsługę zmiennych środowiskowych
- dodano konfigurację MSSQL do Settings
- utworzono lokalny plik .env
- zweryfikowano poprawny odczyt konfiguracji

Status:

✅ Konfiguracja środowiska gotowa