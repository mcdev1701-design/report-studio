# Git - ściąga

Dokument zawiera przykładowe polecenia. Zasady pracy, nazewnictwo branchy
i format commitów opisuje [workflow projektu](PROJECT_WORKFLOW.md).

## Podstawowe informacje

```bash
git status
git branch --show-current
git log --oneline
git diff
```

## Branche

Nowy etap rozpoczynaj od aktualnego `develop`:

```bash
git switch develop
git pull
git switch -c feature/etap-nazwa
```

Przełączanie na istniejący branch:

```bash
git switch develop
git switch main
```

## Przygotowanie i commit zmian

Dodawaj tylko pliki przeznaczone do commita:

```bash
git add -- README.md
git add -p
git diff --cached
git commit -m "ETAP_03A opis zmiany"
```

## Push i merge

Pierwszy push nowego brancha:

```bash
git push -u origin feature/etap-nazwa
```

Po zakończeniu etapu, zgodnie z workflow:

```bash
git switch develop
git pull
git merge feature/etap-nazwa
git push
```

## Tagi

Po przygotowaniu wydania na `main` zgodnie z workflow, utworzenie
i publikowanie taga:

```bash
git tag -a v0.2.0 -m "Opis wydania"
git push origin v0.2.0
```

Przegląd tagów i szczegółów:

```bash
git tag
git show v0.2.0
```

## Repozytorium zdalne

```bash
git remote -v
git remote add origin https://github.com/OWNER/REPOSITORY.git
git push -u origin main
```

## Cofanie zmian

Przed cofaniem sprawdź `git status` i `git diff`. Przywrócenie pliku usuwa
niezapisane zmiany w jego lokalnej kopii:

```bash
git restore -- README.md
```

Usunięcie pliku z indeksu staging bez zmiany jego zawartości:

```bash
git restore --staged -- README.md
```

Polecenia usuwające branche i przywracające pliki stosuj tylko po
potwierdzeniu, że nie zawierają potrzebnych zmian.
