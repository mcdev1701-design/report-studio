"""
Centralna konfiguracja aplikacji Report Studio.

W tym miejscu przechowywane są podstawowe
ustawienia backendu.

Cel edukacyjny:
    Pokazanie jak oddzielić konfigurację
    od logiki biznesowej.

W kolejnych etapach plik zostanie rozbudowany o:

    - ustawienia bazy danych MSSQL,
    - poziomy logowania,
    - zmienne środowiskowe,
    - konfigurację eksportu PDF,
    - konfigurację bezpieczeństwa.
"""

# Nazwa aplikacji widoczna m.in. w Swagger UI.
APP_NAME = "Report Studio"

# Aktualna wersja aplikacji.
APP_VERSION = "0.1.0"

# Wspólny prefiks dla wszystkich endpointów REST API.
#
# Dzięki temu późniejsza zmiana:
#
# /api/v1
#
# na:
#
# /api/v2
#
# będzie wymagała modyfikacji tylko w jednym miejscu.
API_PREFIX = "/api/v1"