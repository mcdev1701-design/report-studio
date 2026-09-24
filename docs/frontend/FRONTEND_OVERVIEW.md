# Frontend Overview

## Cel dokumentu

Dokument opisuje architekturę, strukturę oraz założenia części frontendowej projektu Report Studio.

Frontend odpowiada za interakcję użytkownika z systemem, projektowanie raportów oraz komunikację z backendem FastAPI.

---

# Status

Aktualny etap:

ETAP_01D

Status:

W realizacji

Branch:

feature/etap-01d-frontend-bootstrap

---

# Główne założenia

Frontend budowany jest zgodnie z filozofią projektu:

- pełne zrozumienie każdej linii kodu,
- minimalizacja złożoności na początku projektu,
- stopniowe wprowadzanie nowych technologii,
- rozbudowa oparta o rzeczywiste potrzeby.

Na początkowym etapie nie wykorzystujemy frameworków frontendowych.

Nie używamy:

- React
- Vue
- Angular

Frontend budowany jest w oparciu o:

- HTML
- CSS
- Vanilla JavaScript

---

# Rola frontendu

Frontend odpowiada za:

- prezentację danych użytkownikowi,
- komunikację z backendem FastAPI,
- obsługę interfejsu użytkownika,
- projektowanie raportów,
- konfigurację źródeł danych,
- podgląd raportów,
- eksport raportów.

---

# Technologie

## Aktualnie używane

### HTML

Odpowiada za strukturę dokumentu.

### CSS

Odpowiada za wygląd interfejsu.

### JavaScript

Odpowiada za:

- komunikację z API,
- obsługę zdarzeń,
- aktualizację interfejsu.

---

## Planowane technologie

### Konva.js

Odpowiada za warstwę graficzną projektanta raportów.

Przykłady:

- Canvas
- Drag & Drop
- Resize
- Grid
- Snap

### GSAP

Odpowiada za:

- animacje interfejsu,
- płynne przejścia,
- animacje komponentów,
- poprawę UX.

---

# Struktura katalogów

Docelowa struktura:

```text
frontend/

├── index.html
│
├── css/
│   └── style.css
│
├── js/
│   └── app.js
│
└── assets/
```

---

# Opis katalogów

## index.html

Główny dokument aplikacji.

Zawiera:

- strukturę widoku,
- podłączenie CSS,
- podłączenie JavaScript.

---

## css/

Arkusze stylów aplikacji.

Na obecnym etapie:

```text
style.css
```

W kolejnych etapach:

```text
layout.css
designer.css
components.css
theme.css
```

---

## js/

Kod JavaScript aplikacji.

Na obecnym etapie:

```text
app.js
```

W kolejnych etapach:

```text
api.js
designer.js
toolbar.js
property-panel.js
routing.js
```

---

## assets/

Zasoby statyczne.

Przykłady:

- obrazy,
- ikony,
- logo,
- czcionki.

---

# Komunikacja z backendem

Frontend komunikuje się z backendem za pomocą REST API.

Przykład przepływu:

```text
Przeglądarka
        │
        ▼
JavaScript
        │
        ▼
FastAPI
        │
        ▼
JSON
        │
        ▼
JavaScript
        │
        ▼
HTML
```

---

# Pierwszy cel ETAP_01D

Uzyskanie komunikacji:

```text
Frontend
        ↔
Backend
```

Scenariusz:

1. Użytkownik otwiera stronę.
2. JavaScript wysyła zapytanie do API.
3. FastAPI zwraca dane.
4. Dane wyświetlane są w przeglądarce.

---

# Docelowa architektura frontendu

```text
Browser

↓

index.html

↓

app.js

↓

FastAPI

↓

JSON

↓

app.js

↓

DOM Update
```

---

# Plan rozwoju

## ETAP_01D

Frontend Bootstrap

Zakres:

- index.html
- style.css
- app.js
- pierwsza komunikacja z API

---

## ETAP_03

Visual Designer

Zakres:

- Canvas
- Toolbox
- Properties Panel

---

## ETAP_03B

Konva.js

Zakres:

- obiekty raportu,
- zaznaczanie,
- przesuwanie,
- zmiana rozmiaru.

---

## ETAP_03C

GSAP

Zakres:

- animacje,
- efekty wizualne,
- poprawa UX.

---

# Zasady

1. Najpierw dokumentacja, potem implementacja.
2. Nie wprowadzamy frameworków frontendowych bez uzasadnionej potrzeby.
3. Kod powinien być maksymalnie czytelny i edukacyjny.
4. Każda większa decyzja frontendowa powinna zostać opisana w ADR.
5. Frontend ma pozostać modularny i łatwy do rozbudowy.

## Status

Aktualny etap:

ETAP_01D

Status:

W realizacji

Branch:

feature/etap-01d-frontend-bootstrap

## Pierwszy przepływ danych

HTML

↓

DOMContentLoaded

↓

JavaScript

↓

REST API

↓

JSON

↓

DOM Update

loadApplicationInfo()

Odpowiedzialność:

1. Wysłanie zapytania HTTP.
2. Odebranie odpowiedzi JSON.
3. Aktualizacja elementu backend-info.
4. Obsługa błędów.

## Funkcja loadApplicationInfo()

Odpowiedzialność:

1. Wysłanie zapytania HTTP do backendu.
2. Odebranie odpowiedzi JSON.
3. Aktualizacja widoku.
4. Obsługa błędów połączenia.

Wejście:

Brak.

Wyjście:

Aktualizacja elementu:

backend-info
