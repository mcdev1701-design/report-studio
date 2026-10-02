# Stan projektu

## Aktualny etap

ETAP_02B - Source Implementations

## Aktualny branch

feature/etap-02b-source-implementations

## Status

W realizacji

## Zakończone etapy

- ETAP_01A - Bootstrap projektu
- ETAP_01B - Dokumentacja architektury
- ETAP_01C - Backend Foundation
- ETAP_01D - Frontend Bootstrap
- ETAP_02A - Data Source Foundation

## Wykonano w ETAP_02B

✅ JsonSource

✅ CSVSource

✅ ExcelSource

✅ Dataset

✅ Diagramy Data Source Engine

✅ Konfiguracja MSSQL przez Settings i .env

✅ Refaktoryzacja JsonSource

✅ Ujednolicenie kontraktu DataSource

✅ Testy JsonSource

✅ Testy CSVSource

✅ Testy ExcelSource

✅ Odczyt konfiguracji przez debug_settings.py

## Aktualny wynik testów

✅ 13 passed

## Aktualna decyzja architektoniczna

MSSQLSource będzie korzystał z:

.env
↓
Settings
↓
MSSQLSource

Dane dostępowe nie są przechowywane w kodzie źródłowym ani repozytorium Git.

## Następny krok

Implementacja MSSQLSource oparta o:

- SQLAlchemy
- Settings
- Dataset

## Dalsze kroki ETAP_02B

- MSSQLSource
- test_mssql_source.py
- weryfikacja kontraktu Dataset dla źródeł SQL
- przegląd i zamknięcie ETAP_02B

### Aktualny etap

ETAP_02B - Source Implementations

### Aktualny branch

feature/etap-02b-source-implementations

### Wykonano

✅ JsonSource

✅ CSVSource

✅ ExcelSource

✅ Dataset

✅ Diagramy Data Source Engine

✅ Konfiguracja MSSQL przez .env i Settings

### Następny krok:

Implementacja MSSQLSource oparta o SQLSource.
