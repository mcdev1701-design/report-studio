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
