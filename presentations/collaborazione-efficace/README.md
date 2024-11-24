---
title: Collaborazione Efficace tra Team di Sviluppo e Stakeholder
author: Lorenzo Bugli
footer: 2024-11-26 - Nana Bianca, Firenze
footerIconUrl: https://www.schroedinger-hat.org/assets/sh-logo-big-UQdXK547.png
revealOptions:
  transition: none
source-code: https://github.com/BugliL/ATTD_TALK
---

# Collaborazione Efficace tra team di sviluppo e Stakeholder
Costruire Software Funzionante  
con approccio ATDD


---

Ogni mattina Bob si sveglia

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

Ogni mattina Alice si sveglia

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

Non e' presente alcuna documentazione \
sullo sviluppo del software in produzione

---

Il vecchio sviluppatore e' scappato in Brasile

---

Alice non sa da dove partire

---

Che tu sia Bob oppure Alice \
l'importante e' che tu sappia usare ATTD \
per arrivare a fine giornata

---

TODO: Slide di presentazione

Slide bicolonna con
- Chi sono
- Schroedinger Hat

---

Cosa vuol dire sviluppare un software?

---

Sviluppare un software significa \
creare un modello <span class="text-blue">compiuterizzato</span> \
per risolvere un problema del mondo reale

---

## Fasi dello sviluppo software

![development lifecycle](./software-lifecycle.png)
<!-- .element: class="right-col" -->

<br/>
<br/>

- Analisi
- Progettazione
- Implementazione
- Testing

---

## Fasi dello sviluppo software

![develop tree](./develop-tree.png)

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
