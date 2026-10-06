# Report Studio

Report Studio to edukacyjny projekt wizualnego projektanta raportów,
inspirowanego narzędziami takimi jak Crystal Reports.

## Cele

- Budowa projektanta raportów w przeglądarce.
- Nauka FastAPI, JavaScriptu i architektury aplikacji.
- Dokumentowanie decyzji i procesu rozwoju.

## Technologie

- Backend: FastAPI
- Frontend: HTML, CSS i Vanilla JavaScript
- Źródła danych: JSON, CSV, Excel, Microsoft SQL Server, STDIN,
  Windows Named Pipe i Unix FIFO
- Planowane technologie frontendu: Konva.js i GSAP

## Status projektu

Aktualny etap, branch i następny krok są prowadzone w
[PROJECT_STATE.md](PROJECT_STATE.md). Aplikacja zawiera podstawowy interfejs
projektanta oraz warstwę źródeł danych; model raportu jest obecnie rozwijany.

## Dokumentacja

- [Indeks dokumentacji](docs/DOCUMENTATION_INDEX.md)
- [Zasady i katalog dokumentacji (Word)](docs/DOCUMENTATION_GUIDE.odt)
- [Kontekst projektu](PROJECT_CONTEXT.md)
- [Struktura projektu](PROJECT_STRUCTURE.md)
- [Mapa drogowa](docs/architecture/ROADMAP.md)
- [Workflow projektu](docs/PROJECT_WORKFLOW.md)
- [Historia zmian](CHANGELOG.md)

## Uruchomienie testów

```bash
python -m pytest -v
```

## AI-Assisted Development

Projekt jest rozwijany przy wsparciu Microsoft 365 Copilot w ramach podejścia
AI-Assisted Development.

Copilot wspomaga proces analizy, projektowania, implementacji i
dokumentowania rozwiązania. Decyzje architektoniczne, weryfikacja kodu
oraz integracja zmian pozostają po stronie autora projektu.

## Licencja

Projekt udostępniony na licencji MIT. Szczegóły znajdują się w pliku
[LICENSE](LICENSE).
