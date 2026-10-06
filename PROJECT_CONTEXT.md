# Kontekst projektu

## Cel

Report Studio to edukacyjny projekt wizualnego projektanta raportów,
inspirowanego Crystal Reports. Projekt służy nauce budowy aplikacji oraz
świadomemu dokumentowaniu jej architektury i rozwoju.

## Założenia

- Preferować prostą architekturę i rozwiązania, które można łatwo zrozumieć.
- Oddzielać warstwy aplikacji i ich odpowiedzialności.
- Utrzymywać dokumentację zgodną z kodem.

## Technologie

- Backend: FastAPI.
- Frontend: HTML, CSS i Vanilla JavaScript.
- Źródła danych: JSON, CSV, Excel, Microsoft SQL Server, STDIN,
  Windows Named Pipe i Unix FIFO.
- Planowane technologie frontendu: Konva.js i GSAP.

## Workflow Git

Projekt wykorzystuje branche `main`, `develop` i `feature/*`. Szczegółowy
proces opisuje [workflow projektu](docs/PROJECT_WORKFLOW.md), a komendy
podręczne zawiera [ściąga Git](docs/GIT_CHEATSHEET.md).

## Źródła informacji

- [PROJECT_STATE.md](PROJECT_STATE.md) jest jedynym źródłem bieżącego etapu,
  brancha i najbliższych zadań.
- [README.md](README.md) przedstawia projekt i jego skrócony status.
- [DOCUMENTATION_INDEX.md](docs/DOCUMENTATION_INDEX.md) kataloguje dokumenty.
- [ARCHITECT_LOG.md](docs/ARCHITECT_LOG.md) rejestruje decyzje architektoniczne.