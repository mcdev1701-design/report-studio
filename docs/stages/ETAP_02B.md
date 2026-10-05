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

1. Decyzja SQLAlchemy

2. Aktualizacja DATASOURCE_ARCHITECTURE.md

3. SQLSource (abstrakcja)

4. MSSQLSource

5. Pierwsze połączenie z SQL Server

6. Dataset

### Decyzje architektoniczne

- MSSQLSource będzie korzystał z SQLSource.
- Konfiguracja połączenia będzie dostarczana przez:
  .env → Settings → MSSQLSource.

### Dodano

- SQLSource
- warstwę pośrednią dla źródeł SQL

### Cel

Przygotowanie architektury pod:

- MSSQLSource
- PostgreSQLSource
- SQLiteSource

### Wykonano

- SQLSource (warstwa pośrednia dla źródeł SQL)
- konfiguracja MSSQL oparta o:
  - .env
  - Settings
- debug_settings.py
- przygotowanie architektury MSSQLSource

### Refaktoryzacja architektury

Dodano:

- FileSource
- SQLSource

Zmodyfikowano:

- JsonSource
- CSVSource
- ExcelSource

Rezultat:

Architektura źródeł danych została podzielona
na źródła plikowe i źródła SQL.

### MSSQLSource v1

Zaimplementowano:

- build_connection_string()
- connect()
- disconnect()
- test_connection()

Wynik:

✅ poprawne połączenie z SQL Server

### MSSQLSource

Dodano:

- execute_query()
- konwersję wyników SQL do Dataset

Rezultat:

SQL Server zwraca dane w tym samym formacie Dataset co:

- JsonSource
- CSVSource
- ExcelSource

### Status

Zakończony

## Kryteria ukończenia

✅ JsonSource

✅ CSVSource

✅ ExcelSource

✅ MSSQLSource

✅ Dataset

✅ FileSource

✅ SQLSource

✅ Połączenie z SQL Server

✅ execute_query()

✅ 20 passed