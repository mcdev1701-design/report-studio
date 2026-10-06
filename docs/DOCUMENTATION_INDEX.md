# Indeks dokumentacji

## Cel dokumentu

Dokument opisuje strukturę dokumentacji projektu Report Studio.

Każdy dokument ma jedno główne miejsce i odpowiedzialność. Bieżący etap,
branch i następny krok są utrzymywane wyłącznie w `PROJECT_STATE.md`.

---

# Dokumenty główne (katalog główny projektu)

## README.md

Publiczny opis projektu.

Zawiera:

- cel projektu,
- opis technologii,
- informacje o licencji,
- krótki status projektu.

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

Jedno źródło prawdy dla aktualnego etapu, brancha, wykonanych prac i
najbliższego kroku. Aktualizowany przy zmianie tych informacji.

---

## PROJECT_CONTEXT.md

Stały kontekst projektu, jego cel, założenia i technologie. Nie przechowuje
bieżącego statusu prac.

---

## PROJECT_STRUCTURE.md

Skrócony opis katalogów projektu i ich odpowiedzialności.

---

## CONTRIBUTING.md

Podstawowe zasady przygotowywania zmian i wskazówki do workflow.

---

## DOCUMENTATION_GUIDE.odt

[Przewodnik Word](DOCUMENTATION_GUIDE.odt) zawiera zasady prowadzenia
dokumentacji i opis każdego pliku Markdown. `docs/trash/info.md` jest
prywatnym zbiorem luźnych notatek, a nie źródłem normatywnym.

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

Log jest chronologicznym podsumowaniem. Szczegółowy zapis formalnej decyzji
znajduje się w odpowiadającym jej ADR.

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

## GIT_CHEATSHEET.md

Szybka ściąga komend Git. Strategię i konwencję commitów opisuje
`PROJECT_WORKFLOW.md`.

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

# Decyzje architektoniczne (docs/decisions)

## ADR-XXX-*.md

Architecture Decision Records.

Jedna decyzja = jeden dokument.

Przykłady:

- ADR-001-project-philosophy.md
- ADR-002-git-workflow.md
- ADR-003-frontend.md

Każdy ADR powinien zawierać:

- problem,
- decyzję,
- uzasadnienie,
- konsekwencje,
- status.

---

# Dokumentacja API (docs/api)

Dokumentacja backendu i endpointów.

Dokument:

### BACKEND_OVERVIEW.md

Zawiera:

- opis backendu,
- strukturę katalogów,
- główne komponenty,
- sposób uruchamiania.

Opisuje również dostępne endpointy i przykładowy sposób uruchomienia.

---

# Frontend (docs/frontend)

Dokumentacja części frontendowej.

## FRONTEND_OVERVIEW.md

Główny dokument opisujący frontend aplikacji.

Zawiera:

- aktualną strukturę plików frontendu,
- panele i dostępne interakcje,
- rozróżnienie używanych i planowanych technologii.

## CSS_CHEATSHEET.md

Przykłady selektorów i właściwości CSS przydatnych przy rozwoju interfejsu.

---

# Baza danych (docs/database)

## DATASOURCE_ARCHITECTURE.md

Opis aktualnej architektury źródeł danych, kontraktu `DataSource` oraz modelu
`Dataset`. Obejmuje zaimplementowane źródła plikowe, SQL i strumieniowe oraz
kierunki przyszłych rozszerzeń.

---

# Testy (docs/testing)

## TESTING_STRATEGY.md

Strategia i zakres testowania projektu.

## KNOWN_WARNINGS.md

Znane ostrzeżenia i ograniczenia testów.

Zawiera ostrzeżenia deprecacyjne potwierdzone w aktualnym zestawie testów.

---

# Deployment (docs/deployment)

Katalog jest przygotowany; dokumentacja wdrożeniowa nie została jeszcze
utworzona.

Docelowo:

- konfiguracja środowiska,
- Docker,
- publikacja aplikacji,
- CI/CD,
- instrukcje wdrożeniowe.

---

# Diagramy (docs/diagrams)

Diagramy tekstowe architektury zapisane w Markdown. Każdy diagram powinien
odróżniać stan aktualny od planowanego.

## datasource-engine.ascii.md

Architektura Data Source Engine.

## frontend-architecture.ascii.md

Architektura części frontendowej.

## report-engine.ascii.md

Architektura silnika raportowego.

---

# Dokumentacja etapów (docs/stages)

Dokumentacja poszczególnych etapów rozwoju projektu.

Przykłady:

- ETAP_01B.md
- ETAP_01C.md
- ETAP_01D.md
- ETAP_02A.md
- ETAP_02B.md
- ETAP_02C.md
- ETAP_03A.md

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

W szczególności:

- karty zakończonych etapów zachowują historię i zmienia się je tylko przy
  korekcie błędów rzeczowych;
- kartę bieżącego etapu aktualizuje się w trakcie prac i przy jego zamknięciu.

Aktualny status i następny krok są utrzymywane w `PROJECT_STATE.md`.

---

# Materiały pomocnicze

`docs/trash/info.md` zawiera prywatne, luźne wpisy użytkownika. Plik jest
celowo zachowany i nie stanowi dokumentacji normatywnej projektu.

---

# Zasady prowadzenia dokumentacji

1. Jeden dokument ma jedną odpowiedzialność.
2. Bieżący status utrzymuj wyłącznie w `PROJECT_STATE.md`.
3. Po dodaniu, usunięciu lub przeniesieniu dokumentu zaktualizuj ten indeks
   i [przewodnik Word](DOCUMENTATION_GUIDE.odt).
4. Zasady i momenty aktualizacji dokumentów opisuje przewodnik Word oraz
   [workflow projektu](PROJECT_WORKFLOW.md).
5. `docs/trash/info.md` jest prywatnym notatnikiem i pozostaje poza
   dokumentacją normatywną.
