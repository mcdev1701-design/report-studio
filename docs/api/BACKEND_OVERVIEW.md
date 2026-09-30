# Backend Overview

Backend oparty jest na FastAPI. Punkt wejścia to `backend/app/main.py`, który
tworzy aplikację, rejestruje router API oraz serwuje szablon i zasoby statyczne.

## Główne moduły

- `backend/app/api/v1/endpoints/` zawiera endpointy API.
- `backend/app/core/` zawiera ustawienia, logger i cykl życia aplikacji.
- `backend/app/models/` zawiera modele domenowe, w tym `Dataset`.
- `backend/app/services/datasources/` zawiera kontrakt `DataSource` i jego
	implementacje.
- `backend/app/templates/` zawiera szablony Jinja2.
- `backend/app/static/` zawiera CSS, JavaScript i pozostałe zasoby frontendu.

## Endpointy

- `GET /` renderuje stronę aplikacji.
- `GET /api/v1/health` zwraca stan backendu.
- `GET /api/v1/info` zwraca nazwę, wersję i status aplikacji.

Moduły korzystają ze wspólnego loggera z `backend/app/core/logger.py`.

## Uruchomienie

```bash
uvicorn backend.app.main:app --reload
```
