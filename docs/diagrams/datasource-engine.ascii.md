# DataSource Engine

## Aktualna architektura

```text
                     +---------------+
                     |  DataSource   |
                     +---------------+
                              |
              +---------------+---------------+
              |                               |
              v                               v

        +-------------+                 +-------------+
        | FileSource  |                 |  SQLSource  |
        +-------------+                 +-------------+
              |                               |
      +-------+-------+                       |
      |       |       |                       |
      v       v       v                       v

 +--------+ +------+ +-------+        +-------------+
 | JSON   | | CSV  | | Excel |        | MSSQLSource |
 +--------+ +------+ +-------+        +-------------+
                                 |
                                 v

                          +---------------+
                          |    Dataset    |
                          +---------------+
```

---

## Architektura docelowa

```text
+-------------+
| JsonSource  |
+-------------+
        |
+-------------+
| CSVSource   |
+-------------+
        |
+-------------+
| ExcelSource |
+-------------+
        |
+-------------+
| SQLSource   |
+-------------+
        |
+-------------+
| MSSQLSource |
+-------------+
        |
+-------------+
| PipeSource  |
+-------------+
        |
        v

+---------------------+
|      Dataset        |
+---------------------+
```

---

## Odpowiedzialności

```text
DataSource
    |
    +-- pobiera dane
    |
    +-- nie renderuje raportów
    |
    +-- nie obsługuje UI

Dataset
    |
    +-- przechowuje dane
    |
    +-- przechowuje metadane
```
