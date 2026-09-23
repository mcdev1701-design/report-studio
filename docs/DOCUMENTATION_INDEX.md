# DOCUMENTATION_INDEX

## Cel dokumentu

Dokument opisuje strukturę dokumentacji projektu Report Studio.

Każdy nowy dokument powinien zostać przypisany do jednej z kategorii
opisanych poniżej.

---

# Dokumenty główne (katalog główny projektu)

## README.md

Opis projektu widoczny na GitHub.

Zawiera:

- cel projektu,
- opis technologii,
- instrukcję uruchomienia,
- informacje o licencji.

---

## LICENSE

Licencja projektu.

Aktualnie:

- MIT License

---

## CHANGELOG.md

Historia zmian projektu.

Aktualizowany przy każdym większym wydaniu
oraz przed utworzeniem nowego taga.

---

## PROJECT_STATE.md

Aktualny stan projektu.

Zawiera:

- aktualny etap,
- status projektu,
- wykonane zadania,
- zadania w realizacji,
- następne kroki.

Aktualizowany po zakończeniu każdego etapu.

---

# Dokumentacja ogólna (docs)

## DEVLOG.md

Dziennik prac programistycznych.

Opisuje:

- co wykonano,
- napotkane problemy,
- rozwiązania,
- wnioski.

Aktualizacja po każdym etapie.

---

## ARCHITECT_LOG.md

Dziennik decyzji architektonicznych.

Opisuje:

- ważne decyzje,
- argumenty za wyborem rozwiązania,
- odrzucone alternatywy.

Aktualizacja wyłącznie przy istotnych zmianach architektury.

---

## COMMIT_RULES.md

Standard tworzenia commitów.

Opisuje:

- sposób nazewnictwa commitów,
- konwencje stosowane w projekcie.

---

## GIT_WORKFLOW.md

Strategia pracy z Git.

Opisuje:

- gałąź main,
- gałąź develop,
- gałęzie feature,
- merge workflow.

---

## GIT_CHEATSHEET.md

Szybka ściąga z najczęściej używanych komend Git.

---

## DOCUMENTATION_INDEX.md

Spis dokumentacji projektu.

---

# Architektura (docs/architecture)

## VISION.md

Wizja projektu.

Odpowiada na pytanie:

Dlaczego projekt powstaje?

---

## ROADMAP.md

Plan rozwoju projektu.

Odpowiada na pytanie:

Dokąd zmierza projekt?

---

## ARCHITECTURE.md

Ogólny opis architektury systemu.

Odpowiada na pytanie:

Jak działa system?

---

## PROJECT_STRUCTURE.md

Opis struktury katalogów projektu.

Odpowiada na pytanie:

Gdzie znajduje się dany element systemu?

---

# Decyzje architektoniczne (docs/decisions)

## ADR-XXX-*.md

Architecture Decision Records.

Jedna decyzja = jeden plik.

Przykłady:

- ADR-001-project-philosophy.md
- ADR-002-git-workflow.md

Opisuje:

- problem,
- decyzję,
- uzasadnienie,
- konsekwencje.

---

# Dokumentacja API (docs/api)

Opis interfejsów backendu.

Docelowo:

- endpointy,
- requesty,
- response,
- przykłady użycia.

---

# Frontend (docs/frontend)

Dokumentacja części frontendowej.

Docelowo:

- Konva.js,
- GSAP,
- komponenty GUI,
- logika projektanta raportów.

---

# Baza danych (docs/database)

Dokumentacja warstwy danych.

Docelowo:

- MSSQL,
- modele danych,
- migracje,
- połączenia i konfiguracja.

---

# Testy (docs/testing)

Dokumentacja testów.

Docelowo:

- testy jednostkowe,
- testy integracyjne,
- testy UI,
- procedury testowe.

---

# Deployment (docs/deployment)

Dokumentacja wdrożeniowa.

Docelowo:

- konfiguracja środowiska,
- Docker,
- publikacja aplikacji,
- CI/CD.

---

# Diagramy (docs/diagrams)

Diagramy projektu.

Formaty:

- draw.io
- png
- svg

Przykłady:

- architektura systemu,
- przepływ danych,
- workflow projektanta raportów,
- model raportu.

---

# Archiwum (docs/archive)

Archiwalne lub wycofane dokumenty.

Nigdy nie usuwać dokumentacji bez potrzeby.

Przenosić tutaj:

- stare wersje,
- odrzucone koncepcje,
- nieaktualne diagramy.

---

# Zasady prowadzenia dokumentacji

1. Najpierw dokumentacja, potem implementacja.
2. Każdy nowy typ dokumentu musi zostać dopisany do DOCUMENTATION_INDEX.md.
3. Nie duplikować informacji pomiędzy dokumentami.
4. Jedna odpowiedzialność = jeden dokument.
5. Każdy etap projektu powinien posiadać wpis w DEVLOG.md.
6. Każda istotna decyzja architektoniczna powinna posiadać własny ADR.
7. Przed utworzeniem taga należy zaktualizować:
   - PROJECT_STATE.md
   - CHANGELOG.md
   - DEVLOG.md