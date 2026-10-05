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