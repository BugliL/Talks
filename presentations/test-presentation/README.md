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

- "First text here" {.fragment .grow}
- "Second text here" {.fragment .fade-up}
- "Third text here" {.fragment .highlight-blue .shrink}

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