# Architecture Log

## 2026-09

### Decyzja

Brak frameworka frontendowego.

### Powód

Celem projektu jest dokładne
zrozumienie działania aplikacji.

---

### Decyzja

FastAPI jako backend.

### Powód

Nowoczesny framework Python
o wysokiej wydajności i dobrej dokumentacji.

---

### Decyzja

GSAP + Konva.js.

### Powód

Budowa nowoczesnego wizualnego projektanta raportów.

## 2026-09-23

### Decyzja

Backend zostanie zbudowany w oparciu o FastAPI
z podziałem na:

- api
- services
- schemas
- models
- core

### Powód

Ograniczenie przyszłej refaktoryzacji
oraz zachowanie modularnej architektury.

## ETAP_01C

### Decyzja

Wprowadzono centralny obiekt Settings.

### Powód

Wszystkie ustawienia aplikacji będą
zarządzane z jednego miejsca.

### Korzyści

- prostsza konfiguracja,
- łatwiejsze testowanie,
- łatwiejsza rozbudowa projektu.

### Decyzja

Wprowadzono centralny system logowania.

### Powód

Wszystkie moduły aplikacji będą korzystać
z jednego mechanizmu logowania.

### Korzyści

- łatwiejsze debugowanie
- monitorowanie błędów
- spójność logów

### Decyzja

Usunięto config.py.

### Powód

Wprowadzono centralną konfigurację
opartą o obiekt Settings.

### Wynik

Wszystkie ustawienia aplikacji
znajdują się w core/settings.py.

### Decyzja

Wprowadzono centralną obsługę cyklu życia aplikacji.

### Powód

Przygotowanie projektu pod przyszłą
inicjalizację bazy danych i usług.
