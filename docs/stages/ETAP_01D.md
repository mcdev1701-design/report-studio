# ETAP_01D
## Branch

`feature/etap-01d-frontend-bootstrap` (branch historyczny etapu)

## Status

Zakończony

## Cel

Uruchomić podstawowy frontend serwowany przez FastAPI i przygotować pierwszy
interaktywny układ projektanta raportów.

## Zakres

- Szablon HTML, CSS i JavaScript.
- Integracja strony z endpointem informacyjnym FastAPI.
- Panele statusu, narzędzi, canvasu i właściwości.
- Podstawowe interakcje i responsywny układ.

## Wykonano

- Przeniesiono frontend do `backend/app/templates/` i
  `backend/app/static/`, aby serwować go przez FastAPI.
- Skonfigurowano Jinja2, pliki statyczne i pobieranie informacji z API.
- Dodano `SystemStatusPanel`, `ToolboxPanel`, `CanvasPanel` i
  `PropertyPanel`.
- Dodano responsywny układ Flexbox.
- Dodano tworzenie, zaznaczanie i usuwanie obiektów canvas oraz synchronizację
  panelu właściwości.
- Przygotowano `FRONTEND_OVERVIEW.md` i `CSS_CHEATSHEET.md`.

## Rezultat

Powstał działający szkielet interfejsu projektanta raportów, zintegrowany
z backendem FastAPI.