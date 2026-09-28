## ETAP_01C

### Commit 1

ETAP_01C bootstrap backend FastAPI

Wykonano:

- przygotowano strukturę backend/app
- dodano pakiety Python (__init__.py)
- dodano config.py
- dodano main.py
- dodano endpoint health
- uruchomiono Swagger UI
- zweryfikowano działanie aplikacji

Wynik testów:

✅ GET /

✅ GET /api/v1/health

✅ GET /docs

### Testy automatyczne

Wprowadzono pytest.

Dodano pierwsze testy:

- root endpoint
- health endpoint

Rezultat:

2 testy przechodzą poprawnie.

### Uwagi

Podczas uruchamiania testów pojawiają się ostrzeżenia
Dotyczące:

- FastAPI
- Starlette
- httpx

Nie wpływają na działanie aplikacji.

Do ponownej weryfikacji podczas aktualizacji zależności.

## ETAP_01D

Data: 2026-09-24

Rozpoczęto ETAP_01D.

Utworzono branch:

feature/etap-01d-frontend-bootstrap

Cel etapu:

- przygotowanie struktury frontendu
- komunikacja z FastAPI
- pierwszy ekran aplikacji

Utworzono pierwszy szkielet frontendu.

Zweryfikowano:

- HTML
- CSS
- JavaScript

Frontend działa lokalnie.

Dodano pierwszy cykl życia frontendu.

Przepływ:

HTML
↓
DOMContentLoaded
↓
loadApplicationInfo()

Zweryfikowano poprawną kolejność wykonywania kodu.


utworzono frontend
wykonano pierwszy fetch
zidentyfikowano problem CORS
podjęto decyzję o serwowaniu frontendu przez FastAPI


Przeniesiono frontend do struktury FastAPI. Usunięto katalog:
frontend/

### Integracja FastAPI i Frontendu

- frontend został przeniesiony do templates i static
- skonfigurowano Jinja2Templates
- skonfigurowano StaticFiles
- frontend pobiera dane z API
- dane wyświetlane są w przeglądarce

Wynik:

Pełna komunikacja:

FastAPI
↓
JSON
↓
JavaScript
↓
DOM
↓
Przeglądarka

Wprowadzono pierwszy komponent UI.

Komponent:

SystemStatusPanel

Cel:

Prezentacja informacji o stanie aplikacji.

Dodano pierwszy komponent projektanta raportów.

Komponent:

ToolboxPanel

Cel:

Prezentacja narzędzi dostępnych dla użytkownika.

Wprowadzono pierwszy układ projektanta raportów.

Technologia:

display:flex

Rezultat:

Panele rozmieszzczone poziomo,
w sposób przypominający narzędzia
typu Crystal Reports.

Wprowadzono pierwszą responsywność UI.

Technologie:

- Flexbox
- Media Queries

Rezultat:

Layout dostosowuje się do szerokości ekranu.

### Layout v1

Utworzono pierwszą wersję układu projektanta raportów.

Wykorzystane technologie:

- Flexbox
- Media Queries

Dodano komponenty:

- ToolboxPanel
- CanvasPanel
- PropertyPanel

Rezultat:

Interfejs zaczyna przypominać aplikację typu:

- Crystal Reports
- JasperSoft Studio
- Visual Studio Designer

### Dokumentacja

Dodano:

CSS_CHEATSHEET.md

Cel:

Budowa własnej bazy wiedzy CSS wykorzystywanej w projekcie.

Wprowadzono pierwszą interakcję UI.

Mechanizm:

Toolbox
↓
Click Event
↓
JavaScript
↓
PropertyPanel

Rezultat:

Użytkownik może wybierać narzędzia
i obserwować reakcję interfejsu.

Wprowadzono pierwszą komunikację pomiędzy komponentami UI.

Przepływ:

Toolbox
↓
JavaScript
↓
Canvas
↓
Properties

Rezultat:

Zmiana wybranego narzędzia aktualizuje dwa komponenty interfejsu jednocześnie.

Wprowadzono pierwszy stan aplikacji.

Obiekt:

canvasObjects

Przepływ:

Toolbox
↓
Click
↓
State Update
↓
Render
↓
Canvas

Rezultat:

Użytkownik może dodawać obiekty na canvas.
