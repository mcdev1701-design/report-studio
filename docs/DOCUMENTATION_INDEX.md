# DOCUMENTATION_INDEX

## Cel dokumentu

Dokument opisuje strukturę dokumentacji projektu Report Studio.

Każdy nowy dokument powinien zostać przypisany do jednej z kategorii opisanych poniżej.

---

# Dokumenty główne (katalog główny projektu)

## README.md

Opis projektu widoczny na GitHub.

Zawiera:

- cel projektu,
- opis technologii,
- instrukcję uruchomienia,
- informacje o licencji,
- aktualny status projektu,
- aktualny etap,
- aktualny branch.

Aktualizowany:

- przy rozpoczęciu etapu,
- przy zakończeniu etapu,
- przy kamieniach milowych.

---

## LICENSE

Licencja projektu.

Aktualnie:

- MIT License

---

## CHANGELOG.md

Historia zmian projektu.

Zawiera:

- nowe funkcjonalności,
- poprawki,
- wydania,
- kamienie milowe.

Aktualizowany:

- przed utworzeniem nowego taga,
- przed wydaniem nowej wersji.

---

## PROJECT_STATE.md

Aktualny stan projektu.

Zawiera:

- aktualny etap,
- aktualny branch,
- status projektu,
- wykonane zadania,
- zadania w realizacji,
- kolejne kroki.

Aktualizowany po zakończeniu każdego podetapu i etapu.

---

# Dokumentacja ogólna (docs)

## DEVLOG.md

Dziennik prac programistycznych.

Opisuje:

- co wykonano,
- napotkane problemy,
- zastosowane rozwiązania,
- wnioski.

Aktualizacja:

- na początku etapu,
- w trakcie realizacji,
- przy zakończeniu etapu.

---

## ARCHITECT_LOG.md

Dziennik decyzji architektonicznych.

Opisuje:

- najważniejsze decyzje projektowe,
- uzasadnienia,
- korzyści,
- konsekwencje.

Aktualizacja:

- wyłącznie przy decyzjach architektonicznych.

Nie służy do opisywania codziennych zmian w kodzie.

---

## PROJECT_WORKFLOW.md

Procedura prowadzenia projektu.

Opisuje:

- workflow etapów,
- workflow dokumentacji,
- workflow Git,
- workflow tagowania,
- działania wykonywane przy rozpoczęciu i zakończeniu etapów.

Jest nadrzędnym dokumentem operacyjnym projektu.

---

## COMMIT_RULES.md

Standard tworzenia commitów.

Opisuje:

- format commitów,
- przykłady commitów,
- dobre praktyki.

---

## GIT_WORKFLOW.md

Strategia pracy z Git.

Opisuje:

- branch main,
- branch develop,
- branch feature,
- merge workflow.

---

## GIT_CHEATSHEET.md

Szybka ściąga z najczęściej używanych komend Git.

---

## DOCUMENTATION_INDEX.md

Spis całej dokumentacji projektu.

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

Jedna decyzja = jeden dokument.

Przykłady:

- ADR-001-project-philosophy.md
- ADR-002-git-workflow.md

Każdy ADR powinien zawierać:

- problem,
- decyzję,
- uzasadnienie,
- konsekwencje,
- status.

---

# Dokumentacja API (docs/api)

Dokumentacja backendu i endpointów.

Przykład:

### BACKEND_OVERVIEW.md

Zawiera:

- opis backendu,
- strukturę katalogów,
- główne komponenty,
- sposób uruchamiania.

Docelowo:

- endpointy,
- requesty,
- response,
- przykłady użycia.

---

# Frontend (docs/frontend)

Dokumentacja części frontendowej.

## FRONTEND_OVERVIEW.md

Główny dokument opisujący frontend aplikacji.

Zawiera:

- cele i założenia frontendu,
- wykorzystywane technologie,
- planowane technologie,
- strukturę katalogów,
- komunikację z backendem,
- architekturę frontendu,
- roadmapę rozwoju frontendu.

Docelowo:

- Konva.js,
- GSAP,
- komponenty GUI,
- logika projektanta raportów,
- komunikacja z API.

---

# Baza danych (docs/database)

Dokumentacja warstwy danych.

Docelowo:

- MSSQL,
- modele danych,
- migracje,
- konfiguracja połączeń,
- diagramy bazy danych.

---

# Testy (docs/testing)

Dokumentacja testów.

Docelowo:

- testy jednostkowe,
- testy integracyjne,
- testy UI,
- testy wydajnościowe,
- procedury testowe.

---

# Deployment (docs/deployment)

Dokumentacja wdrożeniowa.

Docelowo:

- konfiguracja środowiska,
- Docker,
- publikacja aplikacji,
- CI/CD,
- instrukcje wdrożeniowe.

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
- workflow raportów,
- struktura projektu,
- model raportu.

---

# Dokumentacja etapów (docs/stages)

Dokumentacja poszczególnych etapów rozwoju projektu.

Przykłady:

- ETAP_01A.md
- ETAP_01B.md
- ETAP_01C.md
- ETAP_01D.md

Każdy dokument etapu powinien zawierać:

- nazwę etapu,
- branch,
- status,
- cel,
- zakres,
- kryteria ukończenia,
- wykonane zadania,
- rezultaty,
- sposób testowania.

Aktualizowany:

- przy rozpoczęciu etapu,
- w trakcie realizacji,
- po zakończeniu etapu.

---

# PROJECT_CONTEXT.md

Kontekst dla AI

# Archiwum (docs/archive)

Archiwalne lub wycofane dokumenty.

Przechowuje:

- stare wersje dokumentów,
- porzucone koncepcje,
- nieaktualne diagramy,
- materiały historyczne.

Dokumentów nie usuwamy bez potrzeby.

Przenosimy je do archiwum.

---

# Zasady prowadzenia dokumentacji

1. Najpierw dokumentacja, potem implementacja.
2. Każdy nowy dokument musi zostać wpisany do DOCUMENTATION_INDEX.md.
3. Nie duplikujemy informacji pomiędzy dokumentami.
4. Jeden dokument powinien mieć jedną odpowiedzialność.
5. README.md musi zawsze odzwierciedlać aktualny stan projektu.
6. Każdy etap musi posiadać własny dokument w katalogu docs/stages.
7. Każda istotna decyzja architektoniczna powinna posiadać wpis w ARCHITECT_LOG.md lub oddzielny ADR.
8. Przed utworzeniem taga należy zaktualizować:
   - README.md
   - PROJECT_STATE.md
   - DEVLOG.md
   - CHANGELOG.md
   - ROADMAP.md
9. Rozpoczęcie etapu wymaga aktualizacji:
   - README.md
   - PROJECT_STATE.md
   - DEVLOG.md
   - ETAP_xx.md
10. Zakończenie etapu wymaga aktualizacji:
   - README.md
   - PROJECT_STATE.md
   - DEVLOG.md
   - ETAP_xx.md
11. Każdy kamień milowy (Milestone) powinien zakończyć się:
   - aktualizacją CHANGELOG.md,
   - utworzeniem taga Git,
   - publikacją Release na GitHub.