# Data Source Engine

## Aktualna hierarchia zaimplementowanych źródeł

```text
                         +------------------+
                         |   DataSource     |
                         +--------+---------+
                                  |
                   +--------------+--------------+
                   |                             |
                   v                             v
          +-----------------+           +-----------------+
          |   FileSource    |           |    SQLSource    |
          +--------+--------+           +--------+--------+
                   |                             |
          +--------+--------+                    v
          |        |        |             +--------------+
          v        v        v             | MSSQLSource  |
       JsonSource CSVSource ExcelSource   +------+-------+
          |        |        |                    |
          +--------+--------+--------------------+
                           v
                      +----------+
                      | Dataset  |
                      +----------+
```

Źródła plikowe udostępniają `get_data()`, a `MSSQLSource` udostępnia
`execute_query(query)`. Obie ścieżki zwracają `Dataset`.

---

## Rozszerzenie w zakresie ETAP_02C

Poniższy diagram przedstawia planowany zakres etapu, a nie aktualnie
zaimplementowane klasy:

```text
                         +------------------+
                         |   DataSource     |
                         +--------+---------+
                                  |
          +-----------------------+-----------------------+
          |                       |                       |
          v                       v                       v

     FileSource             SQLSource             StreamSource
          |                       |                       |
          |                       |                       |
          v                       v                       v

   JSON / CSV / Excel      MSSQLSource           PipeSource
                                                       |
                                    +------------------+------------------+
                                    |                                     |
                                    v                                     v

                              WindowsPipe                           UnixPipe
```

Status i kryteria ukończenia etapu znajdują się w
[ETAP_02C.md](../stages/ETAP_02C.md).

---

## Przepływ docelowy danych

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

Warstwa źródeł danych nie odpowiada za Report Engine ani Renderer. Integracja
tych elementów należy do architektury docelowej projektu.
