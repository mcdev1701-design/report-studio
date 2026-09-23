# GIT CHEATSHEET - REPORT STUDIO

## Sprawdzenie stanu repozytorium

```bash
git status
```

---

## Wyświetlenie aktualnej gałęzi

```bash
git branch
```

---

## Wyświetlenie historii commitów

```bash
git log --oneline
```

---

## Utworzenie nowej gałęzi

```bash
git switch -c feature/nazwa-galezi
```

Przykład:

```bash
git switch -c feature/etap-01c-fastapi
```

---

## Przełączenie na istniejącą gałąź

```bash
git switch develop
```

Przykład:

```bash
git switch main
```

---

## Dodanie wszystkich zmian

```bash
git add .
```

---

## Dodanie pojedynczego pliku

```bash
git add README.md
```

---

## Utworzenie commita

```bash
git commit -m "ETAP_01B architektura projektu"
```

---

## Sprawdzenie zdalnego repozytorium

```bash
git remote -v
```

---

## Dodanie zdalnego repozytorium GitHub

```bash
git remote add origin https://github.com/login/repo.git
```

---

## Pierwszy push

```bash
git push -u origin main
```

---

## Wysłanie zmian do GitHub

```bash
git push
```

---

## Pobranie zmian z GitHub

```bash
git pull
```

---

## Push nowej gałęzi

```bash
git push -u origin feature/etap-01c-fastapi
```

---

## Scalenie gałęzi z develop

Przełącz się na develop:

```bash
git switch develop
```

Scal gałąź:

```bash
git merge feature/etap-01c-fastapi
```

Wyślij zmiany:

```bash
git push
```

---

## Usunięcie lokalnej gałęzi

```bash
git branch -d feature/etap-01c-fastapi
```

---

## Usunięcie gałęzi z GitHub

```bash
git push origin --delete feature/etap-01c-fastapi
```

---

## Utworzenie taga

```bash
git tag v0.1.0
```

---

## Wysłanie taga

```bash
git push origin v0.1.0
```

---

# Tagi

## Wyświetlenie tagów

```bash
git tag
```

## Dodawanie tagów z opisami 

```bash
git tag -a v0.1.0 -m "Bootstrap projektu"
```

## Wyświetlanie szczegółow taga

```bash
git show v0.1.0
```

## Powrót do konkretnej wersji

```bash
git checkout v0.1.0
```

## Publikacja taga

```bash
git push origin v0.1.0
```

## Wycofanie zmian w pliku

```bash
git restore README.md
```

---

## Cofnięcie pliku z git add

```bash
git restore --staged README.md
```

---

## Podejrzenie różnic

```bash
git diff
```

---

## Sprawdzenie konfiguracji użytkownika

```bash
git config --global user.name
git config --global user.email
```

---

## Ustawienie użytkownika Git

```bash
git config --global user.name "Marcin Cygan"

git config --global user.email "twoj@email.pl"
```

---

# WORKFLOW PROJEKTU REPORT STUDIO

## Utworzenie nowej funkcjonalności

```bash
git switch develop

git switch -c feature/etap-01c-fastapi
```

---

## Praca nad funkcjonalnością

```bash
git add .

git commit -m "ETAP_01C konfiguracja FastAPI"

git push -u origin feature/etap-01c-fastapi
```

---

## Zakończenie funkcjonalności

```bash
git switch develop

git merge feature/etap-01c-fastapi

git push
```

---

## Utworzenie wersji projektu

```bash
git switch main

git merge develop

git push

git tag v0.1.0

git push origin v0.1.0
```

---

# STRATEGIA GAŁĘZI

main
- stabilne wersje projektu

develop
- główna gałąź rozwoju

feature/*
- pojedyncze funkcjonalności

---

# KONWENCJA KOMITÓW

```text
ETAP_01A bootstrap projektu
ETAP_01B architektura projektu
ETAP_01C konfiguracja FastAPI
ETAP_01D pierwszy frontend

ETAP_02A data source abstraction
ETAP_02B MSSQL connector

ETAP_03A visual designer
ETAP_03B Konva integration
ETAP_03C GSAP integration
```

---

# TYPOWY CYKL PRACY

1. Przełącz na develop

```bash
git switch develop
```

2. Utwórz nową gałąź

```bash
git switch -c feature/nazwa
```

3. Wprowadź zmiany

4. Commit

```bash
git add .
git commit -m "Opis zmian"
```

5. Push

```bash
git push -u origin feature/nazwa
```

6. Merge do develop

```bash
git switch develop
git merge feature/nazwa
git push
```

7. Usuń gałąź

```bash
git branch -d feature/nazwa
```