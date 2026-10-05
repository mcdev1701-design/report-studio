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

Wprowadzono pierwszy model zaznaczania obiektów.

Pojęcia:

- selectedTool
- selectedObject

Rezultat:

PropertyPanel prezentuje dane wybranego obiektu Canvas.

Wprowadzono wizualne zaznaczanie obiektów Canvas.

Mechanizm:

selectedObject
↓
renderCanvas()
↓
aktualizacja klas CSS
↓
wyróżnienie zaznaczonego obiektu

## Podsumowanie ETAP_01D

Zrealizowano:

- Frontend Bootstrap
- Integrację z FastAPI
- Jinja2 Templates
- Static Files
- SystemStatusPanel
- ToolboxPanel
- CanvasPanel
- PropertyPanel
- Layout Flexbox
- Responsywność
- Dynamiczne skróty kontekstowe
- Tworzenie obiektów Canvas
- Zaznaczanie obiektów
- Usuwanie obiektów
- Aktualizację PropertyPanel
- Aktualizację CanvasPanel

Rezultat:

Powstał pierwszy działający szkielet wizualnego projektanta raportów.

## ETAP_02A

Rozpoczęto prace nad warstwą źródeł danych, aby oddzielić pobieranie danych
od silnika raportowego.

### DataSource i JsonSource

- Dodano abstrakcyjny kontrakt `DataSource`.
- Zaimplementowano `JsonSource` z metodami `connect()`, `disconnect()`,
	`test_connection()` i `get_data()`.
- Dodano `examples/sample_data.json` do weryfikacji pierwszej implementacji.

### Dataset

- Dodano model `Dataset` jako wspólny format danych i metadanych.
- `JsonSource.get_data()` zwraca `Dataset` z `row_count` i `columns` zamiast
	surowej listy rekordów.

### Weryfikacja historyczna

W trakcie prac zapisano wynik `6 passed`. Aktualny wynik pełnego zestawu
testów znajduje się w `docs/testing/KNOWN_WARNINGS.md` oraz w logu uruchomienia.

### Rozpoczęto

## ETAP_02B

Rozpoczęto implementację kolejnych źródeł danych.

Branch:

feature/etap-02b-source-implementations

Zakres:

- CSVSource
- ExcelSource
- przygotowanie pod MSSQLSource

Cel:

Zweryfikowanie, że różne źródła danych zwracają ten sam model Dataset.

### CSVSource

Dodano drugą implementację DataSource.

Komponent:

CSVSource

Weryfikacja architektury:

JSON
↓
Dataset

CSV
↓
Dataset

Rezultat:

Różne źródła danych zwracają ten sam model Dataset.

Testy:

✅ 10 passed

### ExcelSource

Dodano trzecią implementację DataSource.

Komponent:

ExcelSource

Obsługiwany format:

- XLSX

Przepływ:

Excel
↓
ExcelSource
↓
Dataset

Rezultat:

Trzy różne źródła danych zwracają wspólny model Dataset.

Zweryfikowane źródła:

- JSON
- CSV
- Excel

Testy:

✅ 13 passed

### Przygotowanie SQLSource

Podjęto decyzję o dodaniu warstwy SQLSource
przed implementacją MSSQLSource.

Powód:

- wieloplatformowość,
- łatwiejsza obsługa PostgreSQL,
- łatwiejsza obsługa SQLite,
- mniejsze uzależnienie od SQL Server.

### Przygotowanie MSSQLSource

Wprowadzono konfigurację MSSQL opartą o:

.env
↓
Settings
↓
DataSource

Korzyści:

- brak danych dostępowych w repozytorium
- spójna konfiguracja aplikacji
- przygotowanie pod MSSQLSource

### SQLSource

Wprowadzono warstwę pośrednią pomiędzy:

DataSource
↓
MSSQLSource

Cel:

Uniknięcie uzależnienia architektury od jednego silnika bazodanowego.

Przyszłe źródła:

- MSSQL
- PostgreSQL
- SQLite

### SQLSource

Dodano warstwę pośrednią SQLSource.

Architektura:

DataSource
↓
SQLSource
↓
MSSQLSource

Cel:

Przygotowanie pod:
- MSSQL
- PostgreSQL
- SQLite

oraz ograniczenie zależności od jednego silnika bazodanowego.

### Refaktoryzacja DataSource

Podczas projektowania MSSQLSource odkryto,
że źródła plikowe oraz źródła SQL posiadają
odmienne modele pracy.

Wprowadzono:

DataSource
↓
FileSource

oraz

DataSource
↓
SQLSource

Rezultat:

Bardziej czytelna oraz łatwiejsza do rozbudowy architektura.

### MSSQLSource

Po raz pierwszy zweryfikowano komunikację
Report Studio z rzeczywistym SQL Server.

Architektura:

.env
↓
Settings
↓
MSSQLSource
↓
SQLAlchemy
↓
sqlalchemy-pytds
↓
SQL Server

Rezultat:

test_connection() zwraca True.

Po raz pierwszy pobrano dane z SQL Server.

Przepływ:

SQL Server
↓
MSSQLSource
↓
Dataset

Architektura została zweryfikowana
dla źródeł:

- JSON
- CSV
- Excel
- MSSQL

Data Source Engine został zweryfikowany
dla czterech różnych źródeł danych.