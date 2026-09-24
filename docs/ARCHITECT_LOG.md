# Architecture Log

Dokument zawiera historię najważniejszych decyzji architektonicznych projektu Report Studio.

---

## 2026-09

### Decyzja

Brak frameworka frontendowego.

### Powód

Celem projektu jest dokładne zrozumienie działania aplikacji.

### Korzyści

- pełna kontrola nad kodem,
- lepsze zrozumienie JavaScript,
- mniejsza złożoność na początku projektu.

---

### Decyzja

FastAPI jako backend.

### Powód

Nowoczesny framework Python o wysokiej wydajności i dobrej dokumentacji.

### Korzyści

- szybkie tworzenie API,
- automatyczna dokumentacja Swagger,
- nowoczesne podejście do budowy aplikacji.

---

### Decyzja

GSAP + Konva.js jako podstawa wizualnego projektanta raportów.

### Powód

Budowa nowoczesnego wizualnego projektanta raportów działającego w przeglądarce.

### Korzyści

- zaawansowany canvas,
- płynne animacje,
- doświadczenie zbliżone do aplikacji desktopowych.

---

## 2026-09-23

### Decyzja

Backend zostanie zbudowany w oparciu o FastAPI z podziałem na moduły:

- api
- services
- schemas
- models
- core

### Powód

Ograniczenie przyszłej refaktoryzacji oraz zachowanie modularnej architektury.

### Korzyści

- łatwiejsza rozbudowa projektu,
- czytelny podział odpowiedzialności,
- możliwość niezależnego rozwijania modułów.

---

### Decyzja

Wprowadzono centralny obiekt Settings.

### Powód

Wszystkie ustawienia aplikacji będą zarządzane z jednego miejsca.

### Korzyści

- prostsza konfiguracja,
- łatwiejsze testowanie,
- łatwiejsza rozbudowa projektu.

---

### Decyzja

Usunięto config.py.

### Powód

Wprowadzono centralną konfigurację opartą o obiekt Settings.

### Wynik

Wszystkie ustawienia aplikacji znajdują się w:

```text
backend/app/core/settings.py

## Zasady prowadzenia dokumentu 
1. Wpisujemy wyłącznie decyzje architektoniczne. 
2. Nie wpisujemy zwykłych zmian implementacyjnych. 
3. Jeden wpis = jedna decyzja. 
4. Każda decyzja powinna zawierać: 
- Decyzję 
- Powód 
- Korzyści lub Wynik 
5. Wpisy grupujemy chronologicznie według dat.