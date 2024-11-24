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
creare un <span class="text-blu-highlight">modello compiuterizzato</span> \
per <span class="text-blu-highlight">risolvere</span> un <span class="text-blu-highlight">problema specifico</span>

---

## Fasi dello sviluppo software - teoria

![development lifecycle](./software-lifecycle.png)
<!-- .element: class="fragment right-col" data-fragment-index="5" -->

<br/>
<br/>

- Scrittura dei requisiti
<!-- .element: class="fragment" data-fragment-index="1" -->
- Progettazione del sistema
<!-- .element: class="fragment" data-fragment-index="2"  -->
- Implementazione del codice
<!-- .element: class="fragment" data-fragment-index="3"  -->
- Testing delle funzionalita'
<!-- .element: class="fragment" data-fragment-index="4"  -->

---

## Fasi dello sviluppo software - teoria

![development lifecycle](./software-lifecycle.png)
<!-- .element: class="right-col" -->

<br/>

Qualsiasi sia il framework di sviluppo 
le macro aree del ciclo di vita del software 
sono sempre le stesse 
<!-- .element: class="align-left" -->

---

Bella la teoria ma cosa succede poi nella pratica?

---

## Fasi dello sviluppo software - pratica

![develop tree](./develop-tree.png)

---

# Cosa e' successo? 

<br /> La causa piu' comune sono i problemi di comunicazione tra il team di
sviluppo e gli esperti di dominio.
<!-- .element: class="left-col align-left" -->


![analisys-misanderstanding](./analisys-misunderstanding.png)
<!-- .element: class="right-col" -->

---

# Cosa e' successo?

- Troppe specifiche (il caso di Bob)
<!-- .element: class="fragment" -->
- Poche specifiche (il caso di Alice)
<!-- .element: class="fragment" -->
- Specifiche poco chiare
<!-- .element: class="fragment" -->
- Realizzazione difforme dalle specifiche
<!-- .element: class="fragment" -->

---

## Acceptance Test-Driven Development

Minimizza i problemi di comunicazione <span class="text-blu-highlight">plasmando</span> \
le <span class="text-blu-highlight">specifiche</span>
per essere integrate direttamente all'interno del <span class="text-blu-highlight">processo di sviluppo</span>
<!-- .element: class="align-left" -->

---

TODO: Prerequisiti all'ATDD
 
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

# Qual'e' la fase piu' importante?

1. Scrivere un test che fallisce

2. Implementare il <span style="color: #ffaa00 ">codice minimo</span> per far
passare il test

1. Rifattorizzare mantenendo i test verdi

---

# La fase 2

```python [2]
def uppercase(string: str) -> str:
    return "FOO"
```
<br>

- Chiude il binding test-codice, \
crea un legame tra il test ed il codice scritto.
<!-- .element: class="fragment" -->
- Verifica che il test sia inerente al comportamento corretto
<!-- .element: class="fragment" -->


---

# Cos'e' ATDD?

---

Consiste nell'estendere la pratica di TDD \
creando dei test di accettazione

---

# ATDD - Acceptance Test Driven Development

1. Scrivere un test di accettazione che fallisce
2. Implementare tutto il codice necessario per far passare il test
3. Rifattorizzare mantenendo i test verdi

---
