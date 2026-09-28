# ETAP_01D

## Nazwa

Frontend Bootstrap

## Branch

feature/etap-01d-frontend-bootstrap

## Status

W realizacji

## Cel

Przygotowanie fundamentów frontendu aplikacji.

## Zakres

- index.html
- style.css
- app.js
- komunikacja z FastAPI

## Kryteria ukończenia

- frontend uruchamia się poprawnie
- pobiera dane z backendu
- wyświetla odpowiedź API

### Wykonano

- utworzono index.html
- utworzono style.css
- utworzono app.js
- zweryfikowano ładowanie JavaScript
- dodano obsługę DOMContentLoaded
- utworzono funkcję loadApplicationInfo()
- zweryfikowano uruchamianie JavaScript

- utworzono szkielet frontendu, - wykonano pierwszy fetch(), - zdiagnozowano problem CORS, - podjęto decyzję o serwowaniu frontendu przez FastAPI, - przeniesiono frontend do katalogów templates i static, - usunięto katalog frontend.

### Wykonano

- pobrano dane z endpointu info
- zaktualizowano DOM
- wyświetlono dane backendu na stronie
- dodano obsługę błędów try/catch

### Wykonano

- serwowanie frontendu przez FastAPI
- konfiguracja Jinja2Templates
- konfiguracja StaticFiles
- integracja frontend-backend
- aktualizacja widoku na podstawie danych API
- aktualizacja testów po zmianie root endpoint

### Dodano

- pierwszy komponent UI:
  SystemStatusPanel

### Dodano

- ToolboxPanel
- pierwsze elementy toolboxa:
  - Text
  - Field
  - Image
  - Chart

  ### Dodano

- CanvasPanel
- makietę obszaru roboczego raportu

### Dodano

- PropertyPanel
- makietę panelu właściwości

### Dodano

- Layout v1
- display:flex
- rozmieszczenie paneli:
  - ToolboxPanel
  - CanvasPanel
  - PropertyPanel

  ### Dodano

- responsywność layoutu
- media queries
- obsługę węższych ekranów

### Dodano

- SystemStatusPanel
- ToolboxPanel
- CanvasPanel
- PropertyPanel

### Layout

- display:flex
- flex:1
- flex-shrink
- gap

### Responsywność

- media queries
- układ pionowy dla małych ekranów

### Dokumentacja

- FRONTEND_OVERVIEW.md
- CSS_CHEATSHEET.md

### Dodano

- pierwszą interakcję użytkownika,
- obsługę kliknięcia ToolboxPanel,
- aktualizację PropertyPanel,
- wykorzystanie data-* attributes.

### Dodano

- komunikację ToolboxPanel → CanvasPanel
- synchronizację CanvasPanel i PropertyPanel

### Dodano

- pierwszy model danych Canvas
- canvasObjects
- renderCanvas()
- dodawanie obiektów do CanvasPanel

### Dodano

- identyfikatory obiektów Canvas
- selectedObject
- zaznaczanie obiektów
- aktualizację PropertyPanel na podstawie obiektu

### Dodano

- wizualne zaznaczanie obiektów
- klasę canvas-object-selected
- synchronizację selectedObject z CanvasPanel