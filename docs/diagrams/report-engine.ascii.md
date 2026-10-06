# Docelowy silnik raportowy

Silnik raportowy i renderer są planowanymi elementami architektury. Model
obiektów raportu jest rozwijany w ETAP_03A; diagram nie oznacza, że cały
przepływ jest już zaimplementowany.

## Docelowa architektura

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

## Docelowy przepływ danych

```text
Pliki
SQL
Strumienie

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

## Możliwe rozszerzenia silnika

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
