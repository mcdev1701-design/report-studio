# Data Source Engine

## Aktualna hierarchia zaimplementowanych źródeł

```text
DataSource
├── FileSource
│   ├── JsonSource
│   ├── CSVSource
│   └── ExcelSource
├── SQLSource
│   └── MSSQLSource
└── StreamSource
    ├── STDINSource
    └── PipeSource
        ├── WindowsPipeSource
        └── UnixPipeSource

Wszystkie implementacje
└── Dataset
```

Źródła plikowe udostępniają `get_data()`, a `MSSQLSource` udostępnia
`execute_query(query)`. Źródła strumieniowe udostępniają `get_data()`.
Wszystkie ścieżki zwracają `Dataset`.

---

## Docelowy przepływ raportowania

```text
Źródło danych
      |
      v
   Dataset
      |
      v
 Report Engine
      |
      v
  Renderer
      |
      +---- HTML
      +---- PDF
      +---- Excel
      +---- CSV
```

Report Engine i Renderer należą do docelowej architektury; warstwa źródeł
danych nie odpowiada za ich implementację. Status i kryteria ETAP_02C
znajdują się w [karcie etapu](../stages/ETAP_02C.md).
