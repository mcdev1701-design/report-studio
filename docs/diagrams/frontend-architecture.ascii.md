# Frontend Architecture

## Aktualna architektura

```text
+--------------------------------------+
|           Report Studio              |
+--------------------------------------+

+------------+----------------+--------+
| Toolbox    | Canvas         | Props  |
+------------+----------------+--------+
```

---

## Przepływ zdarzeń

```text
Użytkownik
      |
      v
+-------------+
| ToolboxPanel|
+-------------+
      |
      v
JavaScript
      |
      v
canvasObjects
      |
      v
renderCanvas()
      |
      v
CanvasPanel
```

---

## Zaznaczanie obiektów

```text
Canvas Object
      |
      v
Click
      |
      v
selectedObjectId
      |
      v
PropertyPanel
```

---

## Aktualna hierarchia UI

```text
Report Studio

├── SystemStatusPanel
│
├── DesignerLayout
│   │
│   ├── ToolboxPanel
│   │
│   ├── CanvasPanel
│   │
│   └── PropertyPanel
│
└── ShortcutsPanel
```

---

## Kierunek rozwoju

```text
ToolboxPanel
       |
       v
CanvasPanel
       |
       v
PropertyPanel
       |
       v
Konva.js
       |
       v
Visual Report Designer
```
