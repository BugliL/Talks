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

<img class="w-25" src="./slide-qr-code.png" />

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

# Presentiamoci 

<div class="flex">
    <div class="w-50"><img class="circular-img" src="./profile.jpg" /></div>
    <div class="align-left mt-1 ml-1">
        <b>Lorenzo Bugli</b> - Senior software engineer presso <span class="text-blue-highlight">Fiscozen</span>
        faccio parte della community di <span class="text-blue-highlight">Schroedinger Hat</span>
    </div>
</div>
<br />
<div class="flex">
    <div class="align-left">
        Schroedinger Hat e' un'associazione no profit che promuove l'opensource 
        attraverso progetti di sviluppo software ed eventi
    </div>
    <div class="w-75">
        <img src="./sh-logo.png" />
    </div>
</div>

---

<div class="flex">
    <div>
        <img class="w-50" src="./linkedin.png" /><br />
        Profilo Linkedin 
    </div>
    <div>
        <img class="w-50" src="./schroedinger-hat-qr-code.png" /><br />
        Sito Schroedinger 
    </div>
</div>

---

Cosa vuol dire sviluppare un software?

---

Sviluppare un software significa \
creare un <span class="text-blue-highlight">modello computerizzato</span> \
per <span class="text-blue-highlight">risolvere</span> un <span class="text-blue-highlight">problema specifico</span>

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

<br /> Capita che per problemi di comunicazione
il modello rappresentativo non rispetta i requisiti
<!-- .element: class="left-col align-left" -->

![analisys-misanderstanding](./analisys-misunderstanding.png)
<!-- .element: class="right-col" -->

---

<span class="text-blue-highlight">Acceptance Test-Driven Development</span> 
puo' aiutare a ridurre i problemi di comunicazione collaborando alla 
<span class="text-blue-highlight">scrittura</span> parte dei 
<span class="text-blue-highlight">test</span> agli 
<span class="text-blue-highlight">stakeholder</span>

---

# Un caso reale
## Gestione documenti

---

Mario e' un dirigente di un'azienda di progettazione di <span class="text-blue-highlight">impianti industriali</span>
che ha bisogno di un <span class="text-blue-highlight">software documentale</span> che aiuti il lavoro di tutti i giorni.

---

Mario commissiona il lavoro di sviluppo a Bob.

---

Una delle feature chiave del software e' quella di 
<span class="text-blue-highlight">associare ai documenti</span>
dei <span class="text-blue-highlight">colori</span> in base ai
<span class="text-blue-highlight">campi</span> del documento

---

I campi del documento che fanno variare il colore:
- Tipo di documento
- Stato del documento
- Firma digitale applicata

---

Specifica software scritta da Mario
```text
Il sistema deve associare a tutti i documenti firmati 
digitalmente il colore verde.  

Tutti i documenti di tipo distinte materiale devono 
essere associati al colore giallo.  

I documenti in lavorazione devono essere associati al 
colore rosso a meno che non siano di tipo disegno tecnico, 
in quel caso devono avere il colore blu.
```

Niente di strano?
<!-- .element: class="fragment" -->

Cosa succede per le distinte materiali in lavorazione?
<!-- .element: class="fragment" -->

Cosa succede per i disegni tecnici in lavorazione firmati digitalmente?
<!-- .element: class="fragment" -->

---

Bob si sente confidante e inizia a sviluppare il software

---

Dopo l'implementazione di Bob il software sembrava funzionare 
ma Mario si e' accorto che i documenti firmati digitalmente 
in lavorazione non avevano il colore rosso

---

Suona familiare?
![analisys-misanderstanding](./analisys-misunderstanding.png)

---

Bob cambia approccio e decide di scrivere insieme a Mario
le specifiche sottoforma di test di accettazione

---

# Parte "A" di ATDD

Un specifica software scritta da Mario insieme a BOB

```text[1-4|5|6]
Dato un documento 
    firmato digitalmente, 
    di qualsiasi tipo, 
    in stato di lavorazione
quando gli viene associato un colore
allora il colore associato e' il ROSSO
```

---

# Cosa e' successo?
- Il formato della specifica risulta piu' chiaro
<!-- .element: class="fragment" -->
- Il test di accettazione non fa riferimento a nessun costrutto software
<!-- .element: class="fragment" -->
- Bob e Mario hanno concordato sul comportamento del software
<!-- .element: class="fragment" -->

---

Come utilizza Bob la specifica fornita?

Parte TDD di ATDD
<!-- .element: class="fragment" -->

---

# Parte "TDD" di ATDD
## Test Driven Development

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

<img class="w-25" src="./code-qr-code.png" />

Repository con il codice di esempio

---


# Cos'e' TDD?
1. Scrivere un test che fallisce

```python [0-9|10-23]
@dataclass
class Documento:
    protocollo: str
    tipo: TipoDocumento
    stato: StatoDocumento
    firmato: bool

    def colore(self) -> Colors:
        pass

class ColoreDocumentoShould(TestCase):
    def test_colore_rosso(self):
        documento = Documento(
            protocollo="123",
            tipo=TipoDocumento.DISTINTA_MATERIALI,
            stato=StatoDocumento.IN_LAVORAZIONE,
            firmato=True,
        )

        self.assertEqual(
            documento.colore(), 
            Colori.ROSSO
        )
```

---

```text [1,10,15]
> python -m unittest 000_first_acceptance_test.py 
F
======================================================================
FAIL: test_colore_rosso_quando_viene_associato_dato_un_documento_firmato_digitalmente_in_stato_di_lavorazione (010_documentale.000_first_acceptance_test.ColoreDocumentoShould.test_colore_rosso_quando_viene_associato_dato_un_documento_firmato_digitalmente_in_stato_di_lavorazione)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/Fiscozen/Progetti/ATTD_Talk/src/010_documentale/000_first_acceptance_test.py", line 25, in test_colore_rosso_quando_viene_associato_dato_un_documento_firmato_digitalmente_in_stato_di_lavorazione
    self.assertEqual(documento.colore(), "ROSSO")
    ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: None != 'ROSSO'

----------------------------------------------------------------------
Ran 1 test in 0.000s

FAILED (failures=1)
```

---

2. Implementare il codice minimo per far passare il test
```python [8-9]
@dataclass
class Documento:
    protocollo: str
    tipo: TipoDocumento
    stato: StatoDocumento
    firmato: bool

    def colore(self) -> Colors:
        return Colori.ROSSO

```

---

```text [1,4]
> python -m unittest 000_first_acceptance_test.py 
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
```

---

3. Rifattorizzare mantenendo i test verdi
```python [8-11]
@dataclass
class Documento:
    protocollo: str
    tipo: TipoDocumento
    stato: StatoDocumento
    firmato: bool

    def colore(self) -> Colors:
        if self.stato == StatoDocumento.IN_LAVORAZIONE \
            and self.firmato:
            return Colori.ROSSO
```

---

```text [1,4]
> python -m unittest 000_first_acceptance_test.py 
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
```

---

```python 
def test_colore_rosso(self):
    documento = Documento(
        protocollo="123",
        tipo=TipoDocumento.DISTINTA_MATERIALI,
        stato=StatoDocumento.IN_LAVORAZIONE,
        firmato=True,
    )

    self.assertEqual(documento.colore(), Colori.ROSSO)
```
```python 
def colore(self) -> Colors:
    if self.stato == StatoDocumento.IN_LAVORAZIONE \
        and self.firmato:
        return Colori.ROSSO
```
```text [1,4]
> python -m unittest 000_first_acceptance_test.py 
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
```

---

# Qual'e' la fase piu' importante?

1. Scrivere un test che fallisce
<!-- .element class="fragment fade-out" data-fragment-index="2" -->

2. Implementare il <span style="color: #ffaa00 ">codice minimo</span> per far
passare il test

1. Rifattorizzare mantenendo i test verdi
<!-- .element class="fragment fade-out" data-fragment-index="2" -->

---

# La fase 2
```python 
    def colore(self) -> Colors:
        return Colori.ROSSO
```

<br>

- Verifica che il test sia inerente al comportamento corretto
<!-- .element: class="fragment" -->

- Ancora di salvezza per il CTRL + Z 
<!-- .element: class="fragment" -->

- Chiude il binding test-codice, \
crea un legame tra il test ed il codice scritto.
<!-- .element: class="fragment" -->

---

Un secondo esempio

```text[1-4|5|6]
Dato un documento 
    di tipo distinta materiale
    a prescindere dallo stato,
    a prescindere dalla firma digitale
quando gli viene associato un colore
allora il colore associato è il GIALLO
```

---

1. Scrivere un test che fallisce

```python [0-11|12-22]
@dataclass
class Documento:
    protocollo: str
    tipo: TipoDocumento
    stato: StatoDocumento
    firmato: bool

    def colore(self) -> Colors:
        if self.stato == StatoDocumento.IN_LAVORAZIONE \
            and self.firmato:
            return Colori.ROSSO

class ColoreDocumentoShould(TestCase):
    def test_colore_giallo(self):
        documento = Documento(
            protocollo="125",
            tipo=TipoDocumento.DISTINTA_MATERIALI,
            stato=StatoDocumento.INVIATO,
            firmato=False,
        )
        self.assertEqual(documento.colore(), Colori.GIALLO)
```

---

2. Implementare il codice minimo per far passare il test

```python
    def colore(self) -> Colors:
        if self.tipo == TipoDocumento.DISTINTA_MATERIALI:
            return Colori.GIALLO

        if self.stato == StatoDocumento.IN_LAVORAZIONE \
            and self.firmato:
            return Colori.ROSSO
```

---

3. Rifattorizzare mantenendo i test verdi

```python
    def colore(self) -> Colors:
        if self.tipo == TipoDocumento.DISTINTA_MATERIALI:
            return Colori.GIALLO

        if self.stato == StatoDocumento.IN_LAVORAZIONE \
            and self.firmato:
            return Colori.ROSSO
```

Nessuna modifica necessaria

---

# Retrospettiva

---

# Mario

- Si e' reso conto che la specifica iniziale era ambigua
<!-- .element: class="fragment" -->

- Ha capito come descrivere le specifiche in un formato utile per Bob
<!-- .element: class="fragment" -->

---

# Bob

- Ha integrato la specifica direttamente nel codice
<!-- .element: class="fragment" -->

- Ogni specifica integrata ha validato il comportamento del software
<!-- .element: class="fragment" -->

---

# Vantaggi di entrambi

- Documentazione di funzionamento gratis
<!-- .element: class="fragment" -->

---

# Gherkin pattern
## Given-When-Then

---

# Gherkin pattern

```text
Given [stato iniziale o precondizioni] 

When [succede una determinata azione che modifica lo stato]

Then [variazione di stato oppure risultato atteso]
```

---


# Gherkin pattern

```text 
Dato un documento 
    di tipo distinta materiale
    a prescindere dallo stato,
    a prescindere dalla firma digitale
quando gli viene associato un colore
allora il colore associato è il GIALLO
```

- Semplice da scrivere e veloce da leggere
<!-- .element: class="fragment" -->
- Forza a ragionare in termini di condizioni iniziali/finali/azioni
<!-- .element: class="fragment" -->
- E' scritto nel Linguaggio di Dominio
<!-- .element: class="fragment" -->
- Si traduce facilmente in dei test
<!-- .element: class="fragment" -->

---

Il Gherkin pattern puo' essere utilizzato in qualsiasi
contesto per descrivere un caso specifico

---

# La piramide dei test

<img class="w-50" src="./test-pyramid.png" />

---

```python [|2|3-4|6-7|9-11]
class CarrelloShould(unittest.TestCase):
    def test_given_empty_cart_when_product_added_then_cart_contains_product(self):
        # Given
        carrello = Carrello()

        # When
        carrello.aggiungi_prodotto("Laptop")

        # Then
        self.assertEqual(carrello.totale_prodotti(), 1)
        self.assertIn("Laptop", carrello.prodotti)
```
---

Ci sono dei sistemi piu' avanzati per scrivere test di accettazione?

---

<img class="w-50" src="./cucumber-logo.png" />

[https://cucumber.io/](https://cucumber.io/)

<img class="w-25" src="./cucumber-qr-code.png" />

Tools & techniques that elevate teams to greatness

---


# Gherkin

```gherkin
Feature: showing off behave

  Scenario: run a simple test
     Given we have behave installed
      When we implement a test
      Then behave will test it for us!
```
File: tutorial.feature

---

# Behave - Libreria python

```python [|3-5|7-9|11-13]
from behave import *

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement a test')
def step_impl(context):
    assert True is not False

@then('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
```
File: tutorial.py

---

```text [1|3|5-8|10-13]
> behave

Feature: showing off behave # features/tutorial.feature:1

  Scenario: run a simple test        # features/tutorial.feature:3
    Given we have behave installed   # features/steps/tutorial_steps.py:4 0.000s
    When we implement a test         # features/steps/tutorial_steps.py:9 0.000s
    Then behave will test it for us! # features/steps/tutorial_steps.py:14 0.000s

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.000s
```

---

Riscriviamo il vecchio test

```text 
Dato un documento 
    di tipo distinta materiale
    a prescindere dallo stato,
    a prescindere dalla firma digitale
quando gli viene associato un colore
allora il colore associato è il GIALLO
```

---

```gherkin
Feature: Assegnazione colore documento

  Scenario: Assegnamento colore documento distinta materiale
    Given documento di tipo distinta materiale
    When associato un colore
    Then il colore associato è il GIALLO
```

---

```gherkin
Feature: Assegnazione colore documento

  Scenario: Assegnamento colore documento distinta materiale
    Given documento di tipo distinta materiale
    Then il colore associato è il GIALLO
```

---

```python [4-11|13-17]
from behave import given, then, when
from document import Colori, Documento, StatoDocumento, TipoDocumento

@given("documento di tipo distinta materiale")
def step_given_documento_distinta_materiale(context):
    context.documento = Documento(
        tipo=TipoDocumento.DISTINTA_MATERIALI,
        stato=StatoDocumento.INVIATO,
        protocollo="125",
        firmato=False,
    )

@then("il colore associato è il GIALLO")
def step_then_colore_associato(context):
    assert context.documento.colore() == Colori.GIALLO


```

---

Possiamo anche generalizzare il test

```python 
@then("il colore associato è il GIALLO")
def step_then_colore_associato(context):
    assert context.documento.colore() == Colori.GIALLO
```

```python
@then("il colore associato è il {colore}")
def step_then_colore_associato(context):
    assert context.documento.colore() == Colori[colore]
```

---

Possiamo specificare piu' scenari

```gherkin
Feature: Assegnazione colore documento

  Scenario: Assegnamento colore documento distinta materiale
    Given documento di tipo distinta materiale
    Then il colore associato è il GIALLO

  Scenario: Assegnamento colore documento in lavorazione
    Given documento in stato di lavorazione, firmato
    Then il colore associato è il ROSSO
```

---

```python [1-8|11-18|21-26]
@given("documento di tipo distinta materiale")
def step_given_documento_distinta_materiale(context):
    context.documento = Documento(
        tipo=TipoDocumento.DISTINTA_MATERIALI,
        stato=StatoDocumento.INVIATO,
        protocollo="125",
        firmato=False,
    )


@given("documento in stato di lavorazione, firmato")
def step_given_documento_in_lavorazione(context):
    context.documento = Documento(
        tipo=TipoDocumento.FATTURA,
        stato=StatoDocumento.IN_LAVORAZIONE,
        protocollo="125",
        firmato=True,
    )


@then("il colore associato è il {colore}")
def step_then_colore_associato(context, colore):
    assert context.documento.colore() == Colori[colore]
    

```

---

Utilizzo di template

```gherkin
Feature: Assegnazione colore documento

  Scenario Outline: Assegnamento colore documento
    Given documento di tipo <tipo>, nello stato <stato>, firmato <firmato>
    Then il colore associato è il <colore>

    Examples:
      | tipo        | stato           | firmato     | colore |
      | DISTINTA    | ANY             | ANY         | GIALLO |
      | FATTURA     | IN_LAVORAZIONE  | True        | ROSSO  |
```

---

```python [1-8|11-18|21-26]
@given("documento di tipo {tipo}, nello stato {stato}, firmato {firmato}")
def step_given_documento_distinta_materiale(context, tipo, stato, firmato):

    tipo = TipoDocumento[tipo] if tipo != "ANY" else random.choice(list(TipoDocumento))
    stato = StatoDocumento[stato] if stato != "ANY" else random.choice(list(StatoDocumento))
    firmato = bool(firmato == "True") if firmato != "ANY" else random.choice([True, False])

    context.documento = Documento(tipo=tipo, stato=stato, protocollo="125", firmato=firmato)


@then("il colore associato è {colore}")
def step_then_colore_associato(context, colore):
    assert context.documento.colore() == Colori[colore]


```

---

# Specifica per esempi

- Impossibile da fraintendere
<!-- .element: class="fragment" -->

- Facile da reperire
<!-- .element: class="fragment" -->

- Un unico test e' in grado di testare piu' scenari
<!-- .element: class="fragment" -->

- Tutti gli esempi successivi li forniscono gli stakeholder
<!-- .element: class="fragment" -->


---


Un esempio un po' piu' complesso

```gherkin [|2-4|6-10|12-16||2-4]
Feature: Versionamento documenti
  Come utente del sistema documentale 
  Voglio salvare una nuova versione di un documento 
  Per tenere traccia delle modifiche effettuate

  Scenario: Caricamento di una nuova versione di un documento
    Given il documento "Contratto.docx" ha la versione 1.0
    When viene caricato una nuova versione del "Contratto.docx"
    Then il sistema aggiorna il documento alla versione 1.1
    AND il sistema aggiorna lo storico versioni del "Contratto.docx"

  Scenario: Visualizzazione storico versioni
    Given il documento "Contratto.docx" con tre versioni salvate
    Then il sistema mostra le versioni 1.0, 1.1, e 1.2 con data e autore delle modifiche
```

---

# User story

> Una user story e' un placeholder per un'intera conversazione
<!-- .element: class="align-left" -->


```gherkin
As <role> I want <feature> so that <benefit>
```

```text
  Come utente del sistema documentale
  Voglio salvare una nuova versione di un documento
  Per tenere traccia delle modifiche effettuate
```

---

# User stories

- Focus sul valore della funzionalita'
<!-- .element: class="fragment" -->

- Specificano lo scopo per cui una funzionalita' e' sviluppata
<!-- .element: class="fragment" -->

- Non spiegano il come, ma il cosa e soprattutto il perche'
<!-- .element: class="fragment" -->

---


Quando una feature e' troppo grossa non 
si puo' implementare il codide direttamente tutto
in un volta sola

---

# Ciclo di sviluppo di ATTD

1. Scrivere un test di accettazione
<!-- .element: class="fragment" -->
2. Implementare le funzionalita' 
<!-- .element: class="fragment" -->
    - Scrivere uno Unit test 
    <!-- .element: class="fragment" -->
    - Scrivere codice minimo per far passare il test
    <!-- .element: class="fragment" -->
    - Rifattorizzare il codice mantenendo i test verdi
    <!-- .element: class="fragment" -->
    - Ripetere il ciclo fino ad acceptant test verde
    <!-- .element: class="fragment" -->
3. Rifattorizzare il codice mantenendo i test verdi
<!-- .element: class="fragment" -->

---

1. Scriivere un test di accettazione

```gherkin
Scenario: Caricamento di una nuova versione di un documento
    Given il documento "Contratto.docx" ha la versione 1.0
    When viene caricato una nuova versione del "Contratto.docx"
    Then il sistema aggiorna il documento alla versione 1.1
    AND il sistema aggiorna lo storico versioni del "Contratto.docx"
```

```python [|1-4|6-9|10-16]
@given('il documento "{nome}" ha la versione {versione}')
def step_given_documento_con_versione(context, nome, versione):
    context.gestore = GestoreDocumenti()
    context.gestore.aggiungi_documento(nome, versione, autore="Mario Rossi")

@when('viene caricata una nuova versione del "{nome}"')
def step_when_nuova_versione(context, nome):
    context.gestore.nuova_versione(nome, autore="Mario Rossi")

@then("il sistema aggiorna il documento alla versione {nuova_versione}")
def step_then_versione_aggiornata(context, nuova_versione):
    documento = context.gestore.storico_versioni("Contratto.docx")
    ultima_versione = documento[-1].numero
    assert ultima_versione == nuova_versione

```
---

2. Implementare le funzionalita'

```python [|1-6|8-19|]

@dataclass
class Versione:
    numero: str
    data: datetime
    autore: str

class GestoreDocumenti:
    def __init__(self):
        self.documenti = {}

    def aggiungi_documento(self, nome, versione_iniziale, autore):
        pass

    def nuova_versione(self, nome, autore):
        pass

    def storico_versioni(self, nome):
        pass

```

---

2. Implementare le funzionalita'
    - Scrivere uno Unit test

```python [|7|7-15]
class TestGestoreDocumenti(unittest.TestCase):

    def setUp(self):
        """Setup eseguito prima di ogni test"""
        self.gestore = GestoreDocumenti()

    def test_crea_versione_iniziale_documento_when_aggiungi_documento_called(self):
        """Test che il metodo aggiunga correttamente un documento"""
        self.gestore.aggiungi_documento("Contratto.docx", "1.0", "Mario Rossi")

        # Verifica che il documento sia stato aggiunto correttamente
        documenti = self.gestore.storico_versioni("Contratto.docx")
        self.assertEqual(len(documenti), 1)
        self.assertEqual(documenti[0].numero, "1.0")
        self.assertEqual(documenti[0].autore, "Mario Rossi")
```

---

2. Implementare le funzionalita'
    - Scrivere codice minimo per far passare il test

```python [5-7]
class GestoreDocumenti:
    def __init__(self):
        self.documenti = {}

    def aggiungi_documento(self, nome, versione_iniziale, autore):
        versione = Versione(numero="1.0", data=datetime.now(), autore="Mario Rossi")
        self.documenti[nome] = [versione]

    def storico_versioni(self, nome):
        return self.documenti.get(nome, [])
```

---

2. Implementare le funzionalita'
    - Rifattorizzare il codice mantenendo i test verdi

```python [5-11]
class GestoreDocumenti:
    def __init__(self):
        self.documenti = {}

    def aggiungi_documento(self, nome, versione_iniziale, autore):
        versione = Versione(
            numero=versione_iniziale,
            data=datetime.now(),
            autore=autore,
        )
        self.documenti[nome] = [versione]

    def storico_versioni(self, nome):
        return self.documenti.get(nome, [])
```

---

2. Implementare le funzionalita'
    - Scrivere uno Unit test

```python 
    def test_aggiorna_versione_when_nuova_version_called_with_correct_data(self):
        """Test che il metodo aggiunga una nuova versione a un documento esistente"""
        self.gestore.aggiungi_documento("Contratto.docx", "1.0", "Mario Rossi")
        self.gestore.nuova_versione("Contratto.docx", "Luigi Bianchi")

        # Verifica che sia stata aggiunta una nuova versione
        documenti = self.gestore.storico_versioni("Contratto.docx")
        self.assertEqual(len(documenti), 2)
        self.assertEqual(documenti[-1].numero, "1.1")  # La versione dovrebbe essere 1.1
        self.assertEqual(documenti[-1].autore, "Luigi Bianchi")
```

---

2. Implementare le funzionalita'
    - Scrivere codice minimo per far passare il test

```python
class GestoreDocumenti:
    def nuova_versione(self, nome, autore):
        Versione(
            numero="1.1",
            data=datetime.now(),
            autore="Luigi Bianchi",
        )
        storico.append(nuova_versione)

```

---

2. Implementare le funzionalita'
    - Rifattorizzare il codice mantenendo i test verdi

```python
class GestoreDocumenti:
    def nuova_versione(self, nome, autore):
        storico = self.documenti.get(nome)
        if not storico:
            raise ValueError("Documento non trovato")

        # Ottieni l'ultima versione e calcola la nuova
        ultima_versione = storico[-1]
        nuova_versione_num = f"{float(ultima_versione.numero) + 0.1:.1f}"
        nuova_versione = Versione(
            numero=nuova_versione_num,
            data=datetime.now(),
            autore=autore,
        )
        storico.append(nuova_versione)

```
---

3. Test verdi - Rifattorizzare con test verdi

```text [1-2|5-10|11-13|14-17|18-21]
> behave features/versionamento-documenti.feature
Feature: Versionamento documenti 
  Come utente del sistema documentale
  Voglio salvare una nuova versione di un documento
  Per tenere traccia delle modifiche effettuate
  Scenario: Caricamento di una nuova versione di un documento        
    Given il documento "Contratto.docx" ha la versione 1.0           
    When viene caricata una nuova versione del "Contratto.docx"      
    Then il sistema aggiorna il documento alla versione 1.1          
    And il sistema aggiorna lo storico versioni del "Contratto.docx" 

  Scenario: Visualizzazione storico versioni                                           
    Given il documento "Contratto.docx" con tre versioni salvate                       
    Then il sistema mostra le versioni 1.0, 1.1, 1.2 con data e autore delle modifiche 

1 feature passed, 0 failed, 0 skipped
2 scenarios passed, 0 failed, 0 skipped
6 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.000s
```
<!-- .element: class="fs-06" -->


---

Bob ha portato a termine il progetto insieme a Mario \
Una funzionalita' alla volta

---

# Cosa abbiamo visto

- Accettazione con Gherkin syntax
- Test di accettazione per sviluppare codice
- Test di accettazione come documentazione
- Test di accettazione come verita'

---

# Cosa abbiamo visto
- Given, When, Then
- As a, I want, So that
- TDD e ATDD

---

Ed Alice?

---

Alice ha imparato ad utilizzare ATDD
e quando sara' lei a scappare in Brasile 
potra' lasciare il programmatore successivo con serenita'

---

Perche' e' importante ricordare di...

---

> Scrivere software come se il programmatore che prendera' in mano il vostro
> codice fosse uno psicopatico che sa dove abitate


---

# Grazie per l'attenzione