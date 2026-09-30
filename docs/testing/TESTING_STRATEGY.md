# Strategia testów

Testy weryfikują zachowanie aplikacji na poziomie modułów i integracji.

## Rodzaje testów

- Jednostkowe: `tests/unit/`.
- Integracyjne: `tests/integration/`.
- UI: `tests/ui/` (obecnie bez zaimplementowanych testów).
- Wydajnościowe: `tests/performance/` (obecnie bez zaimplementowanych testów).

## Uruchomienie

Wszystkie testy:

```bash
python -m pytest
```

Testy jednostkowe:

```bash
python -m pytest tests/unit
```

Nowe testy dodawaj do katalogu odpowiadającego ich zakresowi. Testy powinny
sprawdzać zachowanie, a nie szczegóły implementacyjne.