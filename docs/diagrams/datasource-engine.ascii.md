# DataSource Engine

## Aktualna architektura

```text
.json
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

.csv
+-------------------+
| CSV File          |
+-------------------+
          |
          v
+-------------------+
|     CSVSource     |
+-------------------+
          |
          v
+-------------------+
|      Dataset      |
+-------------------+

.xlsx
+-------------------+
| Excel File        |
+-------------------+
          |
          v
+-------------------+
|     ExcelSource   |
+-------------------+
          |
          v
+-------------------+
|      Dataset      |
+-------------------+
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
