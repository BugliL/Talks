---
title: Hello world presentation test§
revealOptions:
  transition: 'fade'
---

# Test presentation
## This is a test presentation.

This presentation is used to group templates and slides to
do things

---

## Slide with code

```python
def hello_world():
    print("Hello, world!")
```

---

## Sequence of Fragments

- "First text here" 
<!-- .element class="fragment fade-left" data-fragment-index="1" -->

- "Second text here" 
<!-- .element class="fragment shrink" data-fragment-index="2" -->

- "Third text here" 
<!-- .element: class="fragment shrink" data-fragment-index="2" -->

---

## Cucumber

<div class="fragment" data-fragment-index="2">
- bread
</div>
<div class="fragment" data-fragment-index="1">
- cheese
     - cake
     - sandwich
     - ...
</div>
<div class="fragment" data-fragment-index="3">
- **eggs**
    - tomato
    - banana
</div>

---

## Code with highlights

```js [1-2|3|4]
let a = 1;
let b = 2;
let c = x => 1 + 2 + x;
c(3);
```
<!-- .element: class="fragment fade" data-fragment-index="0" -->

---

## Code already highlighted

```js [|1-2|3|4]
let a = 1;
let b = 2;
let c = x => 1 + 2 + x;
c(3);
```
<!-- .element: class="fragment fade" data-fragment-index="0" -->

---

## Hidden text

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
<!-- .element: style="display: none" -->

This is an hidden text and the real text is not visible.
<!-- .element: class="fragment" data-fragment-index="0" -->