"""
Testy endpointów diagnostycznych.

Cel:
    Weryfikacja poprawnego działania
    podstawowych endpointów aplikacji.
"""

from fastapi.testclient import TestClient

from backend.app.main import app


# Tworzymy klienta testowego FastAPI.
client = TestClient(app)


def test_root_endpoint():
    """
    Test endpointu GET /
    """

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "application": "Report Studio",
        "version": "0.1.0"
    }


def test_health_endpoint():
    """
    Test endpointu GET /api/v1/health
    """

    response = client.get("/api/v1/health")

    assert response.status_code == 200

    assert response.json() == {
        "status": "OK"
    }