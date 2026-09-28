# CSS CHEATSHEET

## Cel dokumentu

Ściąga z właściwości CSS wykorzystywanych w projekcie Report Studio.

Dokument rozwijany wraz z projektem.

---

# Selektory

## ID

CSS:

```css
#backend-info {

}
```

HTML:

```html
<div id="backend-info">
```

Opis:

Odnosi się do jednego, unikalnego elementu.

---

## Class

CSS:

```css
.tool-button {

}
```

HTML:

```html
<button class="tool-button">
```

Opis:

Odnosi się do wielu elementów.

---

# Rozmiary

## width

```css
width: 180px;
```

Ustawia szerokość elementu.

## min-width

```css
min-width: 400px;
```

Minimalna szerokość elementu.

## max-width

```css
max-width: 800px;
```

Maksymalna szerokość elementu.

## width: 100%

```css
width: 100%;
```

Element zajmuje całą szerokość rodzica.

## min-height

```css
min-height: 500px;
```

Minimalna wysokość elementu.

---

# Odstępy

## margin

```css
margin: 20px;
```

Odstęp na zewnątrz elementu.

## margin-top

```css
margin-top: 20px;
```

Odstęp od góry.

## margin-bottom

```css
margin-bottom: 10px;
```

Odstęp od dołu.

## padding

```css
padding: 20px;
```

Wewnętrzny odstęp elementu.

---

# Obramowania

## border

```css
border: 1px solid #cccccc;
```

Dodaje obramowanie.

## border-radius

```css
border-radius: 6px;
```

Zaokrąglenie rogów.

## border: dashed

```css
border: 2px dashed #999999;
```

Przerywane obramowanie.

---

# Kolory

## background-color

```css
background-color: #ffffff;
```

Kolor tła.

---

# Tekst

## font-family

```css
font-family: Arial, sans-serif;
```

Określa używaną czcionkę.

---

# Display

## display: block

Element zajmuje całą szerokość i przechodzi do nowej linii.

## display: inline

Element zachowuje się jak tekst.

## display: inline-block

Element może mieć szerokość i wysokość, ale pozostaje w tej samej linii.

## display: none

Ukrywa element.

## display: flex

Układa elementy obok siebie.

---

# Flexbox

## flex: 1

Element zajmuje całą pozostałą przestrzeń.

## flex-shrink: 0

Element nie jest ściskany przy zmniejszaniu okna.

## flex-direction: row

Elementy obok siebie.

## flex-direction: column

Elementy jeden pod drugim.

## gap

```css
gap: 20px;
```

Odstęp pomiędzy elementami Flexbox.

---

# Responsywność

## Media Query

```css
@media (max-width: 1000px)
```

Reguły wykonywane dla określonej szerokości ekranu.

---

# Zasada projektu

1. Dodaj nową właściwość do dokumentu.
2. Opisz jej działanie.
3. Dopiero potem wykorzystaj ją w projekcie.
