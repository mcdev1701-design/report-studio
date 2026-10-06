# Frontend

## Zakres

Frontend udostępnia w przeglądarce podstawowy interfejs projektanta raportów.
Jest serwowany przez FastAPI i komunikuje się z backendem przez REST API.
Opis przedstawia aktualną implementację; funkcje planowane są oznaczone
osobno.

## Stos technologiczny

### Aktualnie używane

- HTML i szablony Jinja2 - struktura strony.
- CSS - układ, wygląd i responsywność.
- Vanilla JavaScript - komunikacja z API, obsługa zdarzeń i aktualizacja DOM.
- FastAPI - serwowanie strony oraz endpointów.

### Planowane

- Konva.js - renderowanie i interakcje na canvasie.
- GSAP - animacje interfejsu.

Frontend nie korzysta obecnie z frameworka SPA.

## Pliki

```text
backend/app/
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

`index.html` definiuje panele i elementy DOM. `style.css` odpowiada za
układ i wygląd. `app.js` inicjalizuje interfejs po zdarzeniu
`DOMContentLoaded`.

## Interfejs

Widok zawiera:

- **Toolbox** - przyciski Text, Field, Image i Chart.
- **Canvas** - obszar wyświetlania obiektów.
- **Properties** - informacje o wybranym narzędziu lub obiekcie.
- **System Status** - informacje pobrane z backendu.
- **Shortcuts** - podpowiedzi dostępnych skrótów.

Panele są elementami HTML, a ich układ opiera się na CSS Flexbox. Przy
szerokości okna do 1000 px układ przechodzi w orientację pionową.

## Aktualne interakcje

1. Po załadowaniu strony frontend pobiera `GET /api/v1/info` i wyświetla
   nazwę aplikacji, wersję oraz status backendu.
2. Kliknięcie przycisku Toolbox tworzy prosty obiekt DOM na canvasie
   i aktualizuje panel Properties.
3. Kliknięcie obiektu zaznacza go i pokazuje jego typ oraz identyfikator.
4. Klawisz Delete usuwa zaznaczony obiekt.

Obiekty są przechowywane w tablicy `canvasObjects` w pamięci strony.
Odświeżenie strony usuwa bieżący stan projektu; zapisywanie raportu nie
zostało jeszcze zaimplementowane.

## Granice aktualnej implementacji

- Canvas jest renderowany jako DOM, nie przez Konva.js.
- Właściwości obiektów są wyświetlane, ale nie można ich jeszcze edytować.
- Nie ma przeciągania, zmiany rozmiaru ani siatki przyciągania.
- Toolbox tworzy placeholdery; nie implementuje jeszcze pełnej semantyki
  obiektów raportu.
- Integracja z modelem raportu jest rozwijana w ETAP_03A.

Plan etapów opisuje [roadmapa](../architecture/ROADMAP.md), a bieżący stan
projektu - [PROJECT_STATE.md](../../PROJECT_STATE.md).
