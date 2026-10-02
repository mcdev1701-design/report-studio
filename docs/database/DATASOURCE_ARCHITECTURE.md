# Data Source Architecture

## Cel dokumentu

Dokument opisuje architekturę warstwy Data Source projektu Report Studio.

Warstwa Data Source odpowiada za dostarczanie danych do silnika raportowego.

Nie odpowiada za:

- renderowanie raportów,
- eksport danych,
- interfejs użytkownika,
- projektowanie raportów.

Jedyną odpowiedzialnością Data Source jest pobranie oraz udostępnienie danych.

---

# Definicja Data Source

Data Source jest abstrakcją źródła danych.

Z punktu widzenia Report Studio nie ma znaczenia czy dane pochodzą z:

- MSSQL
- CSV
- Excel
- JSON
- STDIN
- Named Pipe

Każde źródło danych powinno być obsługiwane w taki sam sposób.

---

# Główne założenia

## Jednolity interfejs

Każde źródło danych powinno udostępniać ten sam zestaw operacji.

Dzięki temu silnik raportowy nie będzie musiał wiedzieć z jakiego źródła pochodzą dane.

Przykład:

```text
Report Engine

        │
        ▼

DataSource

        │
        ▼

MSSQL
CSV
Excel
JSON
STDIN
Pipe
```

---

## Rozszerzalność

Dodanie nowego źródła danych nie powinno wymagać zmian
w silniku raportowym.

Przykład:

Dzisiaj:

```text
MSSQL
CSV
Excel
```

Jutro:

```text
Oracle
PostgreSQL
REST API
```

Powinny być dodawane jako nowe implementacje Data Source.

---

## Separacja odpowiedzialności

Data Source:

✅ pobiera dane

Data Source:

❌ nie renderuje raportu

❌ nie eksportuje PDF

❌ nie obsługuje UI

---

# Obsługiwane źródła danych

## Zaimplementowane

- JSON przez `JsonSource`.

## Planowane w ramach ETAP_02

- MSSQL
- CSV
- Excel

---

## Planowane w kolejnych etapach

- STDIN
- Named Pipe
- PostgreSQL
- Oracle
- REST API

---

# Kontrakt Data Source

Każde źródło danych powinno wspierać następujące operacje.

---

## connect()

Cel:

Nawiązanie połączenia ze źródłem danych.

Przykłady:

MSSQL

```text
Połączenie z serwerem SQL.
```

CSV

```text
Otwarcie pliku.
```

Named Pipe

```text
Połączenie z kanałem komunikacyjnym.
```

---

## disconnect()

Cel:

Zamknięcie połączenia lub zwolnienie zasobów.

Przykłady:

- zamknięcie połączenia MSSQL,
- zamknięcie pliku,
- zamknięcie Pipe.

---

## test_connection()

Cel:

Weryfikacja dostępności źródła danych.

Przykłady:

```text
Czy serwer SQL odpowiada?
```

```text
Czy plik istnieje?
```

```text
Czy Pipe jest dostępny?
```

---

## get_data()

Cel:

Pobranie danych.

Rezultat:

Dane powinny zostać zwrócone w ujednoliconej formie.

---

# Model architektury

```text
+----------------+
|   DataSource   |
+----------------+
        ▲
        │
        │
+-------+--------+--------+--------+---------+---------+
|       |        |        |        |         |         |
▼       ▼        ▼        ▼        ▼         ▼

MSSQL   CSV     Excel    JSON    STDIN     Pipe
```

---

# Oczekiwana struktura projektu

```text
backend/app/

services/

datasources/

├── datasource.py
├── mssql_source.py
├── csv_source.py
├── excel_source.py
├── json_source.py
├── stdin_source.py
└── pipe_source.py
```

---

# Przepływ danych

```text
Data Source
        │
        ▼
Data Source Engine
        │
        ▼
Report Engine
        │
        ▼
Renderer
        │
        ▼
HTML / PDF / Excel
```

---

# Decyzje architektoniczne

## Data Source nie zna raportów

Warstwa Data Source nie posiada wiedzy o:

- układzie raportu,
- grupowaniu,
- eksportach,
- wizualizacji.

Jej zadaniem jest wyłącznie dostarczenie danych.

---

## Report Engine nie zna typu źródła

Report Engine korzysta wyłącznie z interfejsu Data Source.

Nie powinien wiedzieć czy dane pochodzą z:

- MSSQL,
- CSV,
- Excel,
- Pipe.

---

# Kryteria ukończenia ETAP_02A

- [x] Zaprojektowany i udokumentowany kontrakt `DataSource`.
- [x] Określone planowane źródła danych.
- [x] Przygotowany model rozwoju warstwy danych.
- [x] Zaimplementowana klasa bazowa `DataSource`.
- [x] Dodana implementacja `JsonSource`.
- [x] Zdefiniowany model `Dataset` używany przez źródło JSON.

## Zakres implementacji ETAP_02A

Etap obejmuje kontrakt `DataSource`, pierwszą implementację `JsonSource`
oraz wspólny model `Dataset`. Kolejne źródła danych mogą być dodawane
niezależnie, zgodnie z tym kontraktem.

# Pierwsza implementacja

## JsonSource

Cel:

Zweryfikowanie poprawności architektury DataSource.

Powód wyboru:

- brak zależności zewnętrznych,
- prosta implementacja,
- możliwość testowania bez bazy danych.

Odpowiedzialność:

- odczyt pliku JSON,
- zwrócenie danych do silnika raportowego.

## Format zwracanych danych

get_data() zwraca:

list[dict]

Przykład:

[
    {
        "id": 1,
        "name": "Produkt A"
    },
    {
        "id": 2,
        "name": "Produkt B"
    }
]

Powód:

Jest to uniwersalny format możliwy do obsługi przez wszystkie planowane źródła danych.

# Wewnętrzny model danych

Data Source odpowiada wyłącznie za pobranie danych.

Wszystkie dane powinny zostać przekształcone do wspólnego formatu.

Aktualny standard:

```python
list[dict]
```

Przykład:

```python
[
    {
        "id": 1,
        "name": "Produkt A"
    }
]
```

Dzięki temu Report Engine nie musi wiedzieć czy dane
pochodzą z:

- MSSQL
- CSV
- Excel
- JSON
- Pipe

## Konfiguracja Data Source

Każde źródło danych otrzymuje konfigurację
podczas tworzenia obiektu.

Przykład:

source = JsonSource(
    file_path="sample_data.json"
)

source.connect()

source.get_data()

## JsonSource

Pierwsza implementacja DataSource.

Cel:

Weryfikacja architektury Data Source Engine.

Format wejściowy:

JSON

Format wyjściowy:

list[dict]

# Dataset

Dataset jest uniwersalnym nośnikiem danych
w projekcie Report Studio.

DataSource zwraca Dataset.

Report Engine pracuje na Dataset.

Renderer pracuje na Dataset.

## Aktualny przepływ danych

JSON File, CSV File
        ↓
JsonSource, CSVSource
        ↓
     Dataset
        ↓
  Report Engine

## Diagramy

Szczegółowe diagramy znajdują się w:

docs/diagrams/datasource-engine.ascii.md

## Zweryfikowane implementacje

✅ JsonSource

✅ CSVSource

Obie implementacje:

- dziedziczą po DataSource
- zwracają Dataset
- przechodzą testy jednostkowe

Architektura została zweryfikowana dla więcej niż jednego źródła danych.

## ExcelSource

Cel:

Odczyt danych z plików Excel (.xlsx).

Zakres v1:

- pierwszy arkusz roboczy
- nagłówki w pierwszym wierszu

Format wyjściowy:

Dataset

## Zaimplementowane

- JsonSource
- CSVSource
- ExcelSource

## Zweryfikowane źródła danych

Aktualnie zaimplementowano:

- JSON
- CSV
- Excel

Wszystkie implementacje:

- dziedziczą po DataSource,
- zwracają Dataset,
- wykorzystują wspólny kontrakt źródła danych.

### Konfiguracja

MSSQLSource korzysta z konfiguracji dostarczanej przez:

.env
↓
Settings
↓
MSSQLSource

Dane dostępowe nie są przechowywane w kodzie źródłowym.

## SQLSource

Warstwa pośrednia pomiędzy DataSource a implementacjami SQL.

Architektura:

```text
DataSource
      |
      +----------------+
                       |
                       |
               +-------+-------+
               |               |
               v               v

          FileSource      SQLSource
               |               |
               |               |
        +------+------+        |
        |      |      |        |
        v      v      v        v

      JSON    CSV   Excel    MSSQL
```

Odpowiedzialność:

- zarządzanie połączeniem SQL,
- wykonywanie zapytań,
- tworzenie Dataset.

Implementacje pochodne odpowiadają wyłącznie za konfigurację połączenia.

## Refaktoryzacja kontraktu DataSource

Po implementacji pierwszych źródeł danych zauważono różnicę pomiędzy:

- źródłami plikowymi,
- źródłami SQL.

Wprowadzono warstwę pośrednią:

DataSource
↓
FileSource

oraz:

DataSource
↓
SQLSource

Dzięki temu:

- JsonSource
- CSVSource
- ExcelSource

korzystają z:

get_data()

natomiast:

- MSSQLSource
- PostgreSQLSource
- SQLiteSource

korzystają z:

execute_query()
