# ETAP_02A - Data Source Engine

## Branch

feature/etap-02a-data-source-engine

## Status

W realizacji

## Cel

Zdefiniować wspólny kontrakt źródeł danych i sprawdzić go na pierwszej
implementacji.

## Zakres

- Abstrakcyjna klasa `DataSource`.
- Implementacja źródła JSON.
- Model `Dataset` jako ujednolicona postać zwracanych danych.
- Testy jednostkowe.

## Kryteria ukończenia

✅ Zaprojektowany kontrakt DataSource

✅ Udokumentowana architektura

✅ Określone wspierane źródła danych

✅ Przygotowany model rozwoju warstwy danych

✅ Utworzona abstrakcyjna klasa DataSource

✅ Utworzony model Dataset

✅ Utworzona pierwsza implementacja JsonSource

✅ Testy przechodzą poprawnie


## Wykonano

- Utworzono klasę bazową `DataSource` opartą na `ABC`.
- Zaimplementowano `connect()`, `disconnect()`, `test_connection()` i
  `get_data()` w `JsonSource`.
- Dodano przykładowe dane JSON w `examples/sample_data.json`.
- Dodano model `Dataset` z właściwościami `row_count` i `columns`.
- Zintegrowano `JsonSource` z `Dataset`.
- Dodano testy jednostkowe dla kontraktu i źródła JSON.

## Weryfikacja

Ostatni lokalny wynik: `6 passed` dla `tests/unit`.

Status:

ETAP_02A zakończony.
