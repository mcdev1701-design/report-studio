"""
Endpointy diagnostyczne aplikacji.

Cel:
    Udostępnienie prostych operacji pozwalających
    sprawdzić czy backend działa poprawnie.

Najczęściej wykorzystywany endpoint:
    GET /api/v1/health

W przyszłości:
    Endpoint może zwracać dodatkowo:

    - status bazy danych,
    - status połączeń sieciowych,
    - czas działania aplikacji,
    - wersję systemu.
"""

from fastapi import APIRouter

# Router grupujący endpointy związane
# ze stanem aplikacji.
router = APIRouter()


@router.get("/health")
def health_check():
    """
    Health Check.

    Cel:
        Pozwala szybko sprawdzić czy
        aplikacja odpowiada na zapytania.

    Adres:
        GET /api/v1/health

    Zwraca:
        JSON ze statusem aplikacji.

    Przykład odpowiedzi:

        {
            "status": "OK"
        }
    """

    return {
        "status": "OK"
    }