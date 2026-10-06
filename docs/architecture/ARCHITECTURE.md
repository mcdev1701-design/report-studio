# Architektura systemu

## Aktualna architektura

```text
+-------------------------+
| Przeglądarka            |
| HTML, CSS, Vanilla JS   |
+------------+------------+
             |
             v
+-------------------------+
| FastAPI                 |
| Strona i REST API       |
+------------+------------+
             |
             v
+-------------------------+
| Warstwa źródeł danych   |
| File / SQL / Stream     |
+------------+------------+
             |
             +---------------------+--------------------------+
             |                     |                          |
             v                     v                          v
  JSON / CSV / Excel             MSSQL              STDIN / Named Pipe
             |                     |                          |
             +---------------------+--------------------------+
                                   v
                                Dataset
```

## Kierunek rozwoju

```text
ETAP_03A: Report Model
    |
    v
Visual Designer
    |
    +-- Konva.js
    +-- GSAP
```

Silnik raportowy, zapis projektów i eksport należą do kolejnych etapów.
Bieżący zakres i status prac wskazuje
[PROJECT_STATE.md](../../PROJECT_STATE.md).