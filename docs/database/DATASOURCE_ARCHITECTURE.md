# Architektura źródeł danych

## Cel i zakres

Warstwa źródeł danych pobiera rekordy ze źródeł takich jak pliki lub baza
danych i normalizuje wynik do modelu `Dataset`. Nie odpowiada za interfejs
użytkownika, projektowanie ani renderowanie raportu.

Dokument opisuje istniejące implementacje oraz planowane rozszerzenia.
Szczegółowy diagram znajduje się w
[datasource-engine.ascii.md](../diagrams/datasource-engine.ascii.md).

## Aktualny stan implementacji

### Zaimplementowane

- `JsonSource` - odczyt plików JSON.
- `CSVSource` - odczyt plików CSV.
- `ExcelSource` - odczyt plików `.xlsx`.
- `MSSQLSource` - wykonywanie zapytań do Microsoft SQL Server.
- `FileSource` i `SQLSource` - klasy bazowe dla odpowiednich typów źródeł.

Implementacje znajdują się w `backend/app/services/datasources/`.

### Źródła strumieniowe

Zakres ETAP_02C obejmuje:

- `StreamSource`.
- `STDINSource`.
- `NamedPipeSource`.

Te źródła nie są jeszcze częścią aktualnej implementacji backendu.

### Możliwe przyszłe rozszerzenia

PostgreSQL, SQLite, Oracle i REST API są kierunkami rozwoju; nie należą do
zakresu ukończonych implementacji wymienionych powyżej.

## Kontrakt i hierarchia

`DataSource` definiuje cykl życia źródła:

- `connect()` - przygotowanie źródła do odczytu.
- `disconnect()` - zamknięcie połączenia lub zwolnienie zasobów.
- `test_connection()` - sprawdzenie dostępności źródła.

Klasy pochodne grupują źródła według sposobu pobierania danych:

```text
DataSource
├── FileSource
│   ├── JsonSource
│   ├── CSVSource
│   └── ExcelSource
└── SQLSource
    └── MSSQLSource
```

Źródła plikowe implementują `get_data()`. Źródła SQL udostępniają
`execute_query(query)`. W obu przypadkach wynikiem jest `Dataset`; metody
pobierania różnią się, ponieważ źródła plikowe i SQL mają odmienny sposób
interakcji.

Źródła strumieniowe, gdy zostaną zaimplementowane, będą rozwijane w ramach
ETAP_02C. Ich dokładne miejsce w hierarchii powinno wynikać z projektu
`StreamSource`, a nie z założenia, że wszystkie źródła muszą mieć identyczną
metodę pobierania.

## Model `Dataset`

`Dataset` jest wspólną postacią danych przekazywaną przez implementacje.
Zawiera:

- `name` - nazwę zestawu danych,
- `source_type` - typ źródła,
- `source_name` - identyfikator lub nazwę źródła,
- `loaded_at` - czas pobrania,
- `rows` - rekordy jako listę słowników.

Model udostępnia też `row_count` i `columns`. Jego definicja znajduje się
w `backend/app/models/dataset.py`.

## Przepływy

### Źródło plikowe

```text
Plik JSON / CSV / XLSX
          |
          v
       FileSource
          |
          | get_data()
          v
        Dataset
```

### Źródło SQL

```text
.env -> Settings -> MSSQLSource -> SQLAlchemy -> SQL Server
                                      |
                                      | execute_query(query)
                                      v
                                    Dataset
```

Konfiguracja połączenia MSSQL jest pobierana z `Settings`; dane dostępowe
nie powinny być umieszczane w kodzie źródłowym.

## Zasady architektoniczne

- Konkretny typ źródła nie powinien być wymagany do interpretacji zawartości
  `Dataset`.
- Źródła danych odpowiadają za pobranie i opisanie danych, nie za ich
  raportowanie ani prezentację.
- Dodanie nowego źródła powinno rozszerzać warstwę źródeł bez przenoszenia
  logiki odczytu do interfejsu użytkownika.

## Historia kontraktu

ETAP_02A rozpoczął się od kontraktu `DataSource` i `JsonSource`. W toku
ETAP_02B wspólny model wynikowy został ujednolicony jako `Dataset`, a
rozróżnienie `FileSource`/`SQLSource` odzwierciedliło różne sposoby
pobierania danych. Wcześniejsze opisy `list[dict]` jako samodzielnego wyniku
źródła przedstawiają etap pośredni; aktualnym formatem wyniku jest `Dataset`.

## STDINSource

Pierwsza implementacja StreamSource.

Przepływ:

STDIN
↓
STDINSource
↓
Dataset

## WindowsPipeSource

Implementacja PipeSource dla Windows.

Architektura:

PipeSource
↓
WindowsPipeSource
↓
pywin32
↓
Windows Named Pipe
↓
Dataset
