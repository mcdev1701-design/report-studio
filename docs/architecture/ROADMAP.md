# Mapa drogowa

## ETAP_01 - FUNDAMENTY

Przygotowanie środowiska projektu, repozytorium, dokumentacji, backendu,
podstawowego frontendu i testów.

**Status:** zakończony.

---

## ETAP_02 - DATA SOURCE ENGINE

Uniwersalna warstwa dostępu do danych.

Zakres:

- MSSQL
- CSV
- Excel
- JSON
- STDIN
- Windows Named Pipe
- Unix FIFO

**Status:** zakończony. Szczegółowe karty podetapów znajdują się w
`docs/stages/`.

Rezultat: działający silnik źródeł danych zwracających wspólny model
`Dataset`.

---

## ETAP_03 - VISUAL DESIGNER

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

Podetapy:

- **ETAP_03A - Report Model:** model obiektów raportu i ich właściwości.
- **ETAP_03B - Visual Canvas:** obszar projektowania wizualnego.
- **ETAP_03C - Object Interaction:** interakcje z obiektami na canvasie.
- **ETAP_03D - Konva Integration:** integracja biblioteki Konva.js.
- **ETAP_03E - Property Binding:** powiązanie właściwości z panelem edycji.
- **ETAP_03F - Layout Tools:** narzędzia układu obiektów.

Szczegóły bieżącego etapu zawiera
[PROJECT_STATE.md](../../PROJECT_STATE.md).

---

## ETAP_04 - REPORT PERSISTENCE

Zapis i odczyt modelu raportu w formacie JSON.

Planowany zakres:

- serializacja i deserializacja,
- walidacja dokumentu,
- wersjonowanie formatu.

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
