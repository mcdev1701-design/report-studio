# ETAP_02C

## Nazwa

Stream Sources

## Branch

feature/etap-02c-stream-sources

## Status

W realizacji

## Cel

Projekt i implementacja źródeł strumieniowych.

## Zakres

- StreamSource
- STDINSource
- NamedPipeSource

## Kryteria ukończenia

- zaprojektowany StreamSource
- działający STDINSource
- działający NamedPipeSource
- zwracanie Dataset
- testy przechodzą poprawnie

## Status implementacji

ETAP_02C jest w realizacji. Źródła strumieniowe z zakresu tego etapu nie są
jeszcze ujęte w aktualnej implementacji backendu. Ich projekt i postęp
realizacji dokumentuj w tym pliku.

### Wykonano

- zaprojektowano StreamSource
- określono kontrakt dla źródeł strumieniowych
- StreamSource
- STDINSource

### Cel

Przygotowanie architektury pod:

- STDINSource
- NamedPipeSource

### Zweryfikowano

- STDIN → Dataset

### Decyzja architektoniczna

Źródła Pipe będą rozwijane jako:

StreamSource
↓
PipeSource
↓
WindowsPipe / UnixPipe

Zamiast implementacji zależnej wyłącznie od Windows.

### Wykonano

- StreamSource
- STDINSource
- PipeSource

### Cel

Przygotowanie architektury pod:

- WindowsPipe
- UnixPipe

### Dodano

- WindowsPipeSource
- pierwszą implementację PipeSource

### Zakres

- połączenie z istniejącym Named Pipe
- odbiór danych JSON
- konwersja do Dataset

### Refaktoryzacja narzędzi

Połączono:

- debug_pipe_server.py
- debug_windows_pipe_source.py

w jeden plik:

- debug_windows_pipe_source.py

Obsługiwane tryby:

- server
- client

### Wykonano

- StreamSource
- STDINSource
- PipeSource
- WindowsPipeSource

### Decyzje architektoniczne

PipeSource rozwijany jest jako warstwa wieloplatformowa.

Implementacje:

- WindowsPipeSource
- UnixPipeSource

### Dodano

- UnixPipeSource

### Zweryfikowano

PipeSource
↓
UnixPipeSource
↓
Dataset

### Wykonano

- StreamSource
- STDINSource
- PipeSource
- WindowsPipeSource
- UnixPipeSource

### Zweryfikowano

STDIN
↓
Dataset

Windows Pipe
↓
Dataset

Unix FIFO
↓
Dataset

### Wynik

✅ 23 passed