# ROADMAP

## ETAP_01 - FUNDAMENTY

Cel:

Przygotowanie środowiska projektowego.

Zakres:

- Git
- GitHub
- Dokumentacja
- FastAPI
- Frontend
- Testy

Status:

Zakończony

---

## ETAP_02 - DATA SOURCE ENGINE

Cel:

Uniwersalna warstwa dostępu do danych.

Planowane źródła dla ukończenia ETAP_02:

- MSSQL
- CSV
- Excel
- JSON
- STDIN
- Named Pipes

Zaimplementowane są źródła JSON, CSV, Excel, MSSQL, STDIN oraz pipe:
Windows Named Pipe i Unix FIFO.

Rezultat:

Pierwszy działający silnik źródeł danych.

Status: W realizacji. Zakończono ETAP_02A i ETAP_02B; implementacja ETAP_02C
i testy są zakończone, a formalne zamknięcie oczekuje na przegląd. Bieżący
status wskazuje [PROJECT_STATE.md](../../PROJECT_STATE.md), a zakres i
kryteria etapu opisuje [ETAP_02C.md](../stages/ETAP_02C.md).

---

## ETAP_03 - VISUAL DESIGNER

Cel:

Przeglądarkowy projektant raportów.

Funkcje:

- Canvas
- Toolbox
- Properties Panel
- Drag & Drop
- Resize
- Grid
- Snap

Technologie:

- Konva.js
- GSAP

---

## ETAP_04 - REPORT MODEL

Cel:

Model raportu zapisany w JSON.

Funkcje:

- Save
- Load
- Validation
- Versioning

---

## ETAP_05 - HTML RENDERER

Cel:

Generowanie raportu HTML.

---

## ETAP_06 - EXPORT ENGINE

Cel:

Eksport raportów.

Formaty:

- PDF
- Excel
- CSV
- XML

---

## ETAP_07 - PARAMETERS

Cel:

Dynamiczne parametry raportów.

---

## ETAP_08 - GROUPING

Cel:

Grupowanie oraz agregacje.

---

## ETAP_09 - CHART ENGINE

Cel:

Obsługa wykresów.

---

## ETAP_10 - SUBREPORTS

Cel:

Raporty zagnieżdżone.

---

## ETAP_11 - REPOSITORY

Cel:

Centralne repozytorium raportów.

---

## ETAP_12 - RELEASE 1.0

Cel:

Pierwsza stabilna wersja systemu.
