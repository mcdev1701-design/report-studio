# ETAP_03A - Report Model

## Cel

Zdefiniować model domenowy obiektów umieszczanych w raporcie, zanim zostaną
powiązane z warstwą wizualną.

## Branch

`feature/etap-03a-report-model`

## Status

W realizacji

## Zakres

- Abstrakcja bazowa `ReportObject`.
- Typy obiektów: `TextObject`, `FieldObject`, `ImageObject` i `ChartObject`.
- Wspólne właściwości oraz właściwości specyficzne dla typów.
- Zasady rozszerzania modelu na potrzeby Visual Canvas.

## Kryteria ukończenia

- [ ] Zdefiniowana i zaimplementowana hierarchia obiektów.
- [ ] Udokumentowane wspólne właściwości `ReportObject`.
- [ ] Udokumentowane i zaimplementowane właściwości typów konkretnych.
- [ ] Model umożliwia rozszerzenie o interakcje Visual Canvas bez przenoszenia
  logiki prezentacji do warstwy domenowej.
- [ ] Testy weryfikują kontrakt modelu i typy konkretnych obiektów.

## Rezultat

Kontrakt modelu raportu gotowy do wykorzystania przez kolejne podetapy
projektanta. Serializacja, zapis i odczyt dokumentów należą do ETAP_04.