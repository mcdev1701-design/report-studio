# Architecture Log

Dokument zawiera historię najważniejszych decyzji architektonicznych projektu Report Studio.

Log zachowuje chronologię decyzji. Uzasadnienia i konsekwencje formalnie
zatwierdzonych decyzji znajdują się w dokumentach ADR.

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
```

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
```

### Decyzja

Projektant raportów będzie rozwijany w oparciu o trzy główne komponenty UI:

- ToolboxPanel
- CanvasPanel
- PropertyPanel

### Powód

Rozdzielenie odpowiedzialności interfejsu użytkownika.

### Korzyści

- prostsza rozbudowa,
- czytelniejszy kod,
- łatwiejsza integracja z Konva.js.

### Decyzja

Pierwsza wersja interfejsu wykorzystuje Flexbox.

### Powód

Prosta implementacja układu:

- ToolboxPanel
- CanvasPanel
- PropertyPanel

### Korzyści

- responsywność
- czytelny kod CSS
- łatwa przyszła integracja z Konva.js

### Decyzja

Wszystkie źródła danych zwracają Dataset.

### Powód

Silnik raportowy nie powinien znać typu źródła danych.

### Korzyści

- JSON i CSV są nierozróżnialne dla Report Engine
- łatwiejsza implementacja MSSQL
- łatwiejsze rozszerzanie systemu

### Decyzja

ExcelSource wykorzystuje openpyxl.

### Powód

Obsługa nowoczesnego formatu XLSX bez zależności od Microsoft Excel.

### Korzyści

- obsługa plików XLSX,
- integracja z istniejącym kontraktem DataSource,
- możliwość wykorzystania danych biznesowych dostarczanych przez użytkowników.

### Decyzja

Warstwa źródeł SQL będzie projektowana z myślą o wieloplatformowości.

### Powód

Report Studio jest projektem Open Source.

Implementacja nie powinna być uzależniona od jednego systemu operacyjnego.

### Kierunek

Preferowane jest wykorzystanie SQLAlchemy jako warstwy abstrakcji dla źródeł SQL.

### Decyzja

Źródła danych SQL będą implementowane
przez warstwę pośrednią SQLSource.

### Powód

Ograniczenie zależności od jednego silnika bazodanowego.

### Korzyści

- łatwiejsza obsługa MSSQL,
- możliwość dodania PostgreSQL,
- możliwość dodania SQLite,
- zgodność z założeniami Open Source.

### Decyzja

Rozdzielono DataSource na FileSource oraz SQLSource.

### Powód

Źródła plikowe wykorzystują model:

connect()
↓
get_data()

Źródła SQL wykorzystują model:

connect()
↓
execute_query()

Wspólny kontrakt DataSource okazał się zbyt ogólny.

### Korzyści

- bardziej naturalny model źródeł danych,
- łatwiejsza implementacja MSSQL,
- łatwiejsza implementacja PostgreSQL,
- łatwiejsza implementacja SQLite,
- mniejsza liczba sztucznych metod.