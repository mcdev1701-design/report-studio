# Architektura systemu

## Aktualne komponenty

```text
+-------------------------+
| Frontend                |
| HTML, CSS, Vanilla JS   |
+------------+------------+
             |
             v
+-------------------------+
| FastAPI                 |
| REST API i aplikacja    |
+------------+------------+
             |
             v
+-------------------------+
| Warstwa źródeł danych   |
| File / SQL / Stream     |
+------------+------------+
             |
             +-------------------------+----------------------+
             |                         |                      |
             v                         v                      v
  JSON / CSV / Excel                MSSQL              STDIN / Pipe
             |                         |                      |
             +-------------------------+----------------------+
                                       v
                                    Dataset
```

## Kierunek rozwoju

```text
Frontend:
  +-- Konva.js
  +-- GSAP
```

Źródła strumieniowe są zaimplementowane. Technologie frontendu w powyższym
diagramie są planowane. Bieżący status projektu znajduje się w
[PROJECT_STATE.md](../../PROJECT_STATE.md).