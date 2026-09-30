# Frontend Overview

## Cel dokumentu

Dokument opisuje architekturę, strukturę oraz założenia części frontendowej projektu Report Studio.

Frontend odpowiada za interakcję użytkownika z systemem, projektowanie raportów oraz komunikację z backendem FastAPI.

---

## Aktualna implementacja

Frontend jest serwowany przez FastAPI. Szablon znajduje się w
`backend/app/templates/`, a zasoby statyczne w `backend/app/static/`.
Bieżący etap i branch są utrzymywane w `PROJECT_STATE.md`.

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
- obsługę paneli i interakcji dostępnych w bieżącej wersji.

Projektowanie raportów, konfiguracja źródeł, podgląd i eksport są zakresem
przyszłych etapów opisanych w roadmapie.

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

Aktualna struktura:

```text
backend/app/
|-- templates/index.html
`-- static/
        |-- css/style.css
        `-- js/app.js
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

Szczegółowy plan etapów znajduje się w `docs/architecture/ROADMAP.md`.
HTML

`app.js` wywołuje `loadApplicationInfo()` po `DOMContentLoaded`. Funkcja
pobiera JSON z `/api/v1/info` i aktualizuje element `backend-info`.

```text
HTML -> JavaScript -> FastAPI -> JSON -> DOM
```

# Komponenty UI

## SystemStatusPanel

Cel:

Prezentacja podstawowych informacji
o działającej aplikacji.

Źródło danych:

GET /api/v1/info

Wyświetlane informacje:

- Application
- Version
- Status

Odpowiedzialność:

- wyświetlanie danych,
- aktualizacja po otrzymaniu odpowiedzi API,
- prezentacja stanu aplikacji.

## ToolboxPanel

Cel:

Prezentacja elementów możliwych do dodania do raportu.

W przyszłości:

- Drag & Drop
- Integracja z Konva.js
- Tworzenie obiektów raportu

Pierwsze elementy:

- Text
- Field
- Image
- Chart

Odpowiedzialność:

- prezentacja dostępnych narzędzi,
- inicjowanie dodawania komponentów raportu.

## CanvasPanel

Cel:

Główny obszar roboczy projektanta raportów.

W przyszłości:

- Konva.js
- Drag & Drop
- Resize obiektów
- Grid
- Snap

Odpowiedzialność:

- wyświetlanie elementów raportu,
- projektowanie układu raportu,
- interakcja z ToolboxPanel.

Aktualny status:
Panel renderuje i zaznacza obiekty DOM; integracja z Konva.js jest planowana.

## PropertyPanel

Cel:

Prezentacja właściwości zaznaczonego elementu raportu.

W przyszłości:

- pozycja obiektu,
- rozmiar obiektu,
- czcionka,
- kolor,
- powiązane dane.

Odpowiedzialność:

- wyświetlanie właściwości,
- edycja właściwości,
- komunikacja z CanvasPanel.

Aktualny status:
Panel pokazuje wybrane narzędzie lub zaznaczony obiekt; pełna edycja
właściwości jest zakresem przyszłych prac.

## Layout v1

Projektant raportów składa się z trzech głównych paneli:

- ToolboxPanel
- CanvasPanel
- PropertyPanel

Panele rozmieszczone są poziomo przy użyciu:

display: flex

Cel:

Przygotowanie struktury przyszłego wizualnego projektanta raportów.

## Responsywność

Layout projektanta raportów powinien dostosowywać się do szerokości okna przeglądarki.

Desktop:

Toolbox | Canvas | Properties

Tablet / Małe ekrany:

Toolbox
Canvas
Properties

Technologia:

- CSS Flexbox
- Media Queries

## Implementacja UI

Punktem wejścia logiki interfejsu jest `backend/app/static/js/app.js`.
Szczegóły paneli, układu i interakcji opisują poprzednie sekcje.

## Pierwsza interakcja UI

Cel:

Obsługa wyboru narzędzia z ToolboxPanel.

Przepływ:

Użytkownik
↓
Kliknięcie przycisku
↓
JavaScript
↓
Aktualizacja PropertyPanel

Aktualny zakres:

- wybór narzędzia,
- wyświetlenie aktywnego narzędzia.

## Komunikacja komponentów

Aktualny przepływ:

ToolboxPanel
↓
JavaScript
↓
CanvasPanel

oraz

ToolboxPanel
↓
JavaScript
↓
PropertyPanel

## Pierwsze obiekty Canvas

Cel:

Dodawanie obiektów do CanvasPanel.

Aktualny zakres:

- Text Object

Przepływ:

Toolbox
↓
Click
↓
JavaScript
↓
Canvas Object
↓
CanvasPanel

## Zaznaczanie obiektów

Cel:

Umożliwienie zaznaczania obiektów znajdujących się na CanvasPanel.

Przepływ:

Canvas Object
↓
Click
↓
selectedObject
↓
PropertyPanel

Aktualny zakres:

- zaznaczanie obiektu,
- wyświetlenie informacji o obiekcie.

## Wizualne zaznaczanie obiektów

Cel:

Wyróżnienie aktualnie zaznaczonego obiektu Canvas.

Przepływ:

Canvas Object
↓
Click
↓
selectedObject
↓
Aktualizacja stylu CSS
↓
Wyróżnienie obiektu

## Usuwanie obiektów

Cel:

Usuwanie obiektów znajdujących się na CanvasPanel.

Przepływ:

Canvas Object
↓
Select
↓
Delete
↓
Usunięcie obiektu
↓
Render Canvas

Aktualny zakres:

- usuwanie pojedynczego obiektu
- wykorzystanie klawisza Delete