# ETAP_02B - Source Implementations

## Branch

`feature/etap-02b-source-implementations` (branch etapu)

## Status

Zakończony

## Cel

Rozszerzyć kontrakt źródeł danych o implementacje plikowe i SQL,
zwracające wspólny model `Dataset`.

## Zakres

- `CSVSource` i `ExcelSource`.
- Abstrakcje `FileSource` i `SQLSource`.
- Konfiguracja i implementacja `MSSQLSource`.

## Wykonano

- Zaimplementowano `CSVSource` i `ExcelSource`; istniejący `JsonSource`
  dostosowano do wspólnego modelu `Dataset`.
- Wprowadzono `FileSource` dla źródeł plikowych oraz `SQLSource` dla źródeł
  SQL. Źródła plikowe udostępniają `get_data()`, a źródła SQL
  `execute_query()`.
- Dodano konfigurację MSSQL opartą na `Settings` i zmiennych środowiskowych.
- Zaimplementowano `MSSQLSource` z użyciem SQLAlchemy i `sqlalchemy-pytds`.
- Zweryfikowano połączenie z SQL Server oraz konwersję wyników zapytania
  do `Dataset`.

## Kryteria ukończenia

- [x] JSON, CSV i Excel zwracają `Dataset`.
- [x] MSSQL zwraca `Dataset`.
- [x] Istnieją abstrakcje `FileSource` i `SQLSource`.
- [x] Testy etapu przechodzą poprawnie.

## Rezultat

Etap zakończono; źródła JSON, CSV, Excel i MSSQL są zaimplementowane.
Źródła strumieniowe należą do ETAP_02C.

Ostatni odnotowany wynik testów etapu: `20 passed`.
