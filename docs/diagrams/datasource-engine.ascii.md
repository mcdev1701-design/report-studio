# DataSource Engine

## Aktualna architektura

```text
+---------------------+
|   JSON File         |
+---------------------+
          |
          v
+---------------------+
|    JsonSource       |
+---------------------+
          |
          v
+---------------------+
|      Dataset        |
+---------------------+
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
