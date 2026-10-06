# Architektura frontendu

## Aktualny widok

```text
Report Studio (index.html)
├── Toolbox
├── Canvas
├── Properties
├── System Status
└── Shortcuts
```

## Inicjalizacja i komunikacja z API

```text
DOMContentLoaded
       |
       +--> GET /api/v1/info --> aktualizacja System Status
       |
       +--> inicjalizacja Toolbox i skrótów klawiaturowych
```

## Cykl życia obiektu na canvasie

```text
Kliknięcie Toolbox
       |
       v
canvasObjects (pamięć strony)
       |
       v
renderCanvas() --> elementy DOM
                       |
                  kliknięcie
                       v
              selectedObjectId
                       |
                       v
                  Properties
                       |
               klawisz Delete
                       v
             usunięcie obiektu
```

## Granice implementacji

Panele są obecnie elementami HTML, a obiekty canvasu są renderowane w DOM
i przechowywane w pamięci przeglądarki. Konva.js oraz GSAP są planowane;
szczegóły etapów opisuje [roadmapa](../architecture/ROADMAP.md).
