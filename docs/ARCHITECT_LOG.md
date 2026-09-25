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

## 2026-09-24

### Decyzja

Frontend będzie rozwijany etapowo bez użycia frameworków SPA.

### Powód

Celem projektu jest pełne zrozumienie:

- HTML
- CSS
- JavaScript
- komunikacji z API

przed wprowadzeniem dodatkowych warstw abstrakcji.

### Korzyści

- prostszy debugging,
- łatwiejsza nauka,
- większa kontrola nad kodem.

## 2026-09-24

### Decyzja

Frontend będzie serwowany przez FastAPI.

### Powód

Na obecnym etapie projektu najważniejsze jest
zrozumienie podstaw komunikacji pomiędzy
frontendem a backendem.

Wprowadzenie oddzielnego serwera frontendowego
spowodowałoby dodatkową złożoność:

- CORS,
- dodatkowa konfiguracja,
- większa liczba elementów do utrzymania.

### Korzyści

- prostsza architektura,
- jedna aplikacja,
- brak problemów z CORS,
- łatwiejsza nauka działania FastAPI.

Frontend będzie serwowany przez FastAPI.

## 2026-09-25

### Decyzja

Usunięto oddzielny katalog frontend.

### Powód

Podjęto decyzję o serwowaniu frontendu bezpośrednio przez FastAPI.

Utrzymywanie dwóch lokalizacji zawierających pliki HTML, CSS i JavaScript prowadziłoby do:

- duplikacji kodu,
- ryzyka niespójności,
- trudniejszego utrzymania projektu.

### Korzyści

- jedno źródło prawdy,
- prostsza struktura projektu,
- brak problemów z CORS,
- łatwiejsza integracja frontendu z backendem.

### Wynik

Frontend został przeniesiony do:

```text
backend/app/templates/

backend/app/static/
├── css/
├── js/
└── assets/
