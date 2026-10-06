# ETAP_02C

## Nazwa

Stream Sources

## Branch

feature/etap-02c-stream-sources

## Status

W realizacji - implementacja zakończona; formalne zamknięcie oczekuje na
przegląd.

## Cel

Projekt i implementacja źródeł strumieniowych.

## Zakres

- `StreamSource`
- `STDINSource`
- `PipeSource` z implementacjami dla Windows Named Pipe i Unix FIFO

## Kryteria ukończenia

- [x] Zaprojektowany `StreamSource`.
- [x] Działający `STDINSource`.
- [x] Działające źródła Pipe dla Windows i Unix.
- [x] Źródła zwracają `Dataset`.
- [x] Testy przechodzą poprawnie.

## Status implementacji

Implementacje wymienione w zakresie etapu znajdują się w
`backend/app/services/datasources/`. Każde źródło zwraca dane jako `Dataset`.
Status projektu pozostaje „W realizacji” do formalnego przeglądu i zamknięcia
etapu.

## Wykonano

- StreamSource
- STDINSource
- PipeSource
- WindowsPipeSource
- UnixPipeSource

Narzędzie debugujące Windows Pipe obsługuje tryby `server` i `client`.

## Weryfikacja

- STDIN zwraca dane jako `Dataset`.
- Windows Named Pipe zwraca dane jako `Dataset`.
- Unix FIFO zwraca dane jako `Dataset`.
- Pełny zestaw testów: `24 passed` (ostatnie uruchomienie).

## Do zamknięcia etapu

- Przeprowadzić formalny przegląd kryteriów ukończenia.
- Po akceptacji zaktualizować `PROJECT_STATE.md`, `README.md`, roadmapę
  i dziennik prac zgodnie z [workflow projektu](../PROJECT_WORKFLOW.md).