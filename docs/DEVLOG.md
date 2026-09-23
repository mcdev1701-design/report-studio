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