
# Podstawowe polecenia w PowerShell

## Tworzenie wirtulanego środowiska python

(PS) python -m venv .venv

## Aktywacja wirtualnego środowiska w powerschell

(PS).\.venv\Scripts\Activate.ps1

## Zapis zależności

(.venv) pip freeze > requirements.txt

## Uruchamianie serwera uvisorn

(.venv) uvicorn backend.app.main:app --reload