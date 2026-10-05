# Znane ostrzeżenia

Poniższe ostrzeżenia pojawiają się w pełnym zestawie testów na aktualnym
środowisku projektu.

## StarletteDeprecationWarning

Związane z użyciem `TestClient`.

Starlette wskazuje użycie `httpx` jako przestarzałe i sugeruje `httpx2`.

## BlockingPortal alias is deprecated

Ostrzeżenie AnyIO wskazuje alias `anyio.abc.BlockingPortal` jako przestarzały.

### Status

Ostrzeżenia zostały potwierdzone podczas wcześniejszych uruchomień testów.

Aktualny wynik testów należy sprawdzać
na podstawie bieżącego uruchomienia pytest.

