# ETAP_02A

## Nazwa

Data Source Abstraction

## Branch

feature/etap-02a-data-source-abstraction

## Status

W realizacji

## Cel

Stworzenie wspólnego interfejsu
dla wszystkich źródeł danych.

## Zakres

- DataSource
- dokumentacja architektury
- kontrakt interfejsu
- pierwszy model domenowy

## Kryteria ukończenia

- zaprojektowany DataSource
- dokumentacja architektury
- pierwszy interfejs źródła danych

### Wykonano

- utworzono katalog datasources
- utworzono klasę bazową DataSource
- wykorzystano Abstract Base Class
- zdefiniowano kontrakt dla źródeł danych

### Wykonano

- utworzono JsonSource
- przygotowano przykładowe dane JSON
- zaimplementowano:
  - connect()
  - disconnect()
  - test_connection()
  - get_data()
- dodano testy jednostkowe

### Wykonano

- utworzono DataSource
- wykorzystano ABC
- utworzono JsonSource
- przygotowano sample_data.json
- dodano testy jednostkowe

### Wynik testów

✅ 6 passed

### Dodano

- model Dataset
- row_count
- columns
- standard wymiany danych pomiędzy
  DataSource a Report Engine

### Dodano

- integrację JsonSource z Dataset
- row_count
- columns
- wspólny model wymiany danych