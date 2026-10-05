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
| FileSource / SQLSource  |
+------------+------------+
             |
             +-------------------------+
             |                         |
             v                         v
  JSON / CSV / Excel                MSSQL
             |                         |
             +------------+------------+
                          v
                       Dataset
```

## Kierunek rozwoju

```text
StreamSource
  +-- STDINSource
  +-- NamedPipeSource

Frontend:
  +-- Konva.js
  +-- GSAP
```

Źródła strumieniowe oraz wskazane technologie frontendu są planowane lub
rozwijane w swoich etapach. Bieżący status projektu znajduje się w
[PROJECT_STATE.md](../../PROJECT_STATE.md).