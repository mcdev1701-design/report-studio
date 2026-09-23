# PROJECT WORKFLOW

## Cel dokumentu

Dokument definiuje obowiązkowe czynności wykonywane podczas realizacji
kolejnych etapów projektu Report Studio.

---

# Cykl życia etapu

Każdy etap oraz podetap przechodzi przez następujące fazy:

1. Planowanie
2. Dokumentacja
3. Implementacja
4. Testy
5. Aktualizacja dokumentacji
6. Commit
7. Push
8. Merge
9. Tag (dla kamieni milowych)

---

# Rozpoczęcie nowego podetapu

Przykłady:

- ETAP_01C
- ETAP_01D
- ETAP_02A
- ETAP_02B

## Krok 1

Przełącz na develop

```bash
git switch develop
```

---

## Krok 2

Utwórz gałąź feature

```bash
git switch -c feature/nazwa
```

Przykład:

```bash
git switch -c feature/etap-01c-fastapi-bootstrap
```

---

## Krok 3

Zaktualizuj PROJECT_STATE.md

Aktualizujemy:

- Aktualny etap
- Aktualną gałąź
- Status
- Następny krok

---

## Krok 4

Dodaj wpis do DEVLOG.md

Przykład:

Rozpoczęto ETAP_01C.

Utworzono branch:

feature/etap-01c-fastapi-bootstrap

---

## Krok 5

Utwórz dokument etapu

Lokalizacja:

```text
docs/stages/
```

Przykład:

```text
ETAP_01C.md
```

Uzupełnij:

- nazwę etapu
- cel
- zakres
- status
- kryteria ukończenia

---

## Krok 6

Jeśli wymagana jest nowa decyzja architektoniczna

Utwórz nowy ADR.

Lokalizacja:

```text
docs/decisions/
```

---

# W trakcie realizacji etapu

Aktualizujemy wyłącznie:

## ETAP_xx.md

opis wykonanych prac

---

## ARCHITECT_LOG.md

jeżeli podjęto nową decyzję architektoniczną

---

## DEVLOG.md

jeżeli napotkano istotne problemy lub rozwiązania

---

# Zakończenie podetapu

Przykład:

ETAP_01C

## Aktualizujemy:

### ETAP_01C.md

Status:

```text
Zakończony
```

Uzupełniamy:

- wykonane zadania
- sposób testowania
- rezultat

---

### DEVLOG.md

Dodajemy:

- podsumowanie etapu
- wnioski

---

### PROJECT_STATE.md

Aktualizujemy:

- Zakończone etapy
- Następny etap

---

## Commit

```bash
git add .

git commit -m "ETAP_01C konfiguracja backend FastAPI"
```

---

## Push

```bash
git push
```

---

## Merge do develop

```bash
git switch develop

git merge feature/etap-01c-fastapi-bootstrap

git push
```

---

## Usunięcie branch

```bash
git branch -d feature/etap-01c-fastapi-bootstrap
```

---

# Kamień milowy (Milestone)

Przykłady:

- ETAP_01 zakończony
- ETAP_02 zakończony
- ETAP_03 zakończony

---

# Przed utworzeniem taga

Obowiązkowo aktualizujemy:

## CHANGELOG.md

opis zmian

---

## PROJECT_STATE.md

status projektu

---

## DEVLOG.md

podsumowanie etapu

---

## ROADMAP.md

aktualizacja statusów

---

# Utworzenie taga

Wyłącznie na branchu main.

```bash
git switch main

git merge develop

git push
```

---

## Tworzenie taga

```bash
git tag -a v0.1.0 -m "Bootstrap projektu"
```

---

## Publikacja taga

```bash
git push origin v0.1.0
```

---

# Po utworzeniu taga

Aktualizujemy:

## CHANGELOG.md

Dodajemy sekcję:

```markdown
## v0.1.0

### Added

...
```

---

## PROJECT_STATE.md

Przechodzimy do następnego etapu.

Przykład:

Aktualny etap:

ETAP_02

---

# Dokumenty aktualizowane przy każdym podetapie

Obowiązkowo:

✅ PROJECT_STATE.md

✅ DEVLOG.md

✅ ETAP_xx.md

---

# Dokumenty aktualizowane okazjonalnie

✅ ARCHITECT_LOG.md

✅ ADR-XXX.md

✅ ROADMAP.md

✅ ARCHITECTURE.md

---

# Dokumenty aktualizowane wyłącznie przy milestone

✅ CHANGELOG.md

✅ Tag Git

✅ Release GitHub

---

# Złota zasada projektu

Najpierw:

Dokumentacja

Potem:

Implementacja

Nigdy odwrotnie.

# Standard komentowania kodu

Każdy nowy plik Python powinien zawierać:

1. Nagłówek modułu (docstring).
2. Opis celu pliku.
3. Opis przyszłego przeznaczenia.
4. Komentarze dla sekcji kodu.
5. Docstring dla każdej funkcji.
6. Komentarz wyjaśniający "dlaczego",
   a nie tylko "co robi kod".

Projekt ma charakter edukacyjny,
dlatego czytelność jest ważniejsza
niż minimalna liczba linii kodu.
