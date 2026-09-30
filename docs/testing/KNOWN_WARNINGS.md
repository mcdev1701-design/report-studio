# Znane ostrzeżenia

Poniższe ostrzeżenia pojawiają się w pełnym zestawie testów na aktualnym
środowisku projektu.

## StarletteDeprecationWarning

Związane z użyciem `TestClient`.

Starlette wskazuje użycie `httpx` jako przestarzałe i sugeruje `httpx2`.

## BlockingPortal alias is deprecated

Ostrzeżenie AnyIO wskazuje alias `anyio.abc.BlockingPortal` jako przestarzały.

## Status

Potwierdzone 2026-09-30: `python -m pytest` zakończył się wynikiem
`6 passed, 2 warnings`. Ostrzeżenia nie zostały usunięte w ramach tej
refaktoryzacji dokumentacji.
