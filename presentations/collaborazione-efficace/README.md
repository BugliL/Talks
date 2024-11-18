---
title: Collaborazione Efficace tra Team di Sviluppo e Stakeholder
author: Lorenzo Bugli
footer: 2024-11-26 - Nana Bianca, Firenze
footerIconUrl: https://www.schroedinger-hat.org/assets/sh-logo-big-UQdXK547.png
revealOptions:
  transition: none
---

# Collaborazione Efficace tra team di sviluppo e Stakeholder
Costruire Software Funzionante  
con approccio ATDD


---

La storia di Bob

---

Bob e' uno sviluppatore freelance a cui \
viene commissionato lo sviluppo di un software gestionale per un'azienda che
produce carta.

---

Bob non sa niente di come \
si vende o si produce la carta.

---

Ma gli viene fornita una documentazione \
lunga quanto le cronache di Narnia

---

La documentazione contiene delle \
discrepanze tra varie sezioni.

---

Bob non sa da dove partire

---

La storia di Alice

---

Alice e' l'unica sviluppatrice in un'agenzia viaggi, neoassunta la scorsa
settimana e deve iniziare ad integrare il programma interno all'azienda.

---

Il software e' gia' in produzione \
ed Alice non sa come funziona 

---

Fortunatamente ha gia' costruito altre applicazioni per delle agenzie viaggi,
conosce l'argomento, deve solo capire quali sono le customizzazioni

---

Non e' presente alcuna documentazione

---

Il vecchio sviluppatore e' scappato in Brasile

---

Alice non sa da dove partire

---

## Cosa hanno in comune Bob e Alice?

- Devono sviluppare un software
<!-- .element class="fragment" -->
- Non hanno idea da dove partire 
<!-- .element class="fragment" -->
- Dovranno parlare con qualcuno per capire da dove iniziare
<!-- .element class="fragment" -->

---

Sia Bob che Alice dovranno parlare con i propri stakeholder
ed entrambi possono usare ATDD per facilitarsi il lavoro

---

Un po' di contesto

---




---

# Cos'e' TDD? 
# (Test Driven Development)

---

Test first 

code later
<!-- .element: class="fragment" -->

---

# TDD in pratica

1. Scrivere un test che fallisce
<!-- .element class="fragment" -->

2. Implementare il <span style="color: #ffaa00 ">codice minimo</span> per far
passare il test
<!-- .element class="fragment" -->

1. Rifattorizzare mantenendo i test verdi
<!-- .element class="fragment" -->

---

# Cos'e' TDD?
1. Scrivere un test che fallisce
```python [4,5]
import unittest

class UppercaseTestFunctionShould(unittest.TestCase):
    def test_return_uppercase_string_given_string(self):
        self.assertEqual(uppercase(string='foo'), 'FOO')
```
```python 
def uppercase(string: str) -> str:
    pass
```

---

```text [1,10,15]
> python -m unittest tdd_example.py

======================================================================
FAIL: test_return_uppercase_string_given_string (tdd_example.UppercaseTestFunctionShould.test_return_uppercase_string_given_string)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/Fiscozen/Progetti/ATTD_Talk/src/000_introduction/tdd_example.py", line 10, in test_return_uppercase_string_given_string
    self.assertEqual(uppercase(string='foo'), 'FOO')
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: None != 'FOO'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

---

2. Implementare il codice minimo per far passare il test
```python 
def uppercase(string: str) -> str:
    return "FOO"
```

---

```text [1,4]
> python -m unittest tdd_example.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
```

---

3. Rifattorizzare mantenendo i test verdi
```python 
def uppercase(string: str) -> str:
    return string.upper()
```

---

```text [1,4]
> python -m unittest tdd_example.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
```

---

```python [4,5]
import unittest

class UppercaseTestFunctionShould(unittest.TestCase):
    def test_return_uppercase_string_given_string(self):
        self.assertEqual(uppercase(string='foo'), 'FOO')
```
```python 
def uppercase(string: str) -> str:
    return string.upper()
```
```text [1,4]
> python -m unittest tdd_example.py
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
```

---

1. Scrivere un test che fallisce
2. Implementare il codice minimo per far passare il test
3. Rifattorizzare mantenendo i test verdi


La parte 2 e' importante, serve a verificare la correttezza del test.
