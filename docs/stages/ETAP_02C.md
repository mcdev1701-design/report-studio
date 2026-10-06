# ETAP_02C

## Nazwa

Stream Sources

## Branch

feature/etap-02c-stream-sources

## Status

Zakończony

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
- Pełny zestaw testów przy zamknięciu etapu: `23 passed`.