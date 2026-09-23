"""
Endpointy monitorujące stan aplikacji.
"""
from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health_check():
    """
    Sprawdzenie stanu aplikacji.
    """

    return {
        "status": "OK"
    }