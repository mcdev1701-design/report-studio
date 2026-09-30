# Report Engine

## Architektura docelowa

```text
Data Source
      |
      v
+---------------------+
|      Dataset        |
+---------------------+
      |
      v
+---------------------+
|   Report Engine     |
+---------------------+
      |
      v
+---------------------+
|     Renderer        |
+---------------------+
```

---

## Przepływ danych

```text
JSON
CSV
Excel
MSSQL
Pipe

      |
      v

+---------------------+
|      Dataset        |
+---------------------+

      |
      v

+---------------------+
|   Report Engine     |
+---------------------+

- filtrowanie
- grupowanie
- agregacje
- obliczenia

      |
      v

+---------------------+
|     Renderer        |
+---------------------+

      |
      +---- HTML

      |
      +---- PDF

      |
      +---- Excel

      |
      +---- CSV
```

---

## Separacja odpowiedzialności

```text
DataSource
    |
    +-- skąd pochodzą dane

Dataset
    |
    +-- jakie dane zostały pobrane

Report Engine
    |
    +-- jak dane przetworzyć

Renderer
    |
    +-- jak dane wyświetlić
```

---

## Długoterminowa wizja

```text
Dataset
     |
     v
Report Engine
     |
     +---- Parameters
     |
     +---- Grouping
     |
     +---- Calculations
     |
     +---- Subreports
     |
     +---- Charts
```
