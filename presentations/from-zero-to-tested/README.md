---
title: From Zero to Tested
author: Lorenzo Bugli
footer: 2025-11-26 - TSH - Firenze
link: https://buglil.github.io/Talks/from-zero-to-tested/#/
revealOptions:
  transition: none

description: "Molte applicazioni crescono senza test, e anche quando conosciamo
i principi del TDD, è facile perdersi davanti a domande pratiche: da dove
comincio? Quali parti del codice hanno davvero bisogno di test? Quando usare
test unitari, integration test o mock? Tutorial e libri raramente mostrano come
affrontare queste scelte nel codice reale. Ho imparato i principi del TDD
studiando bene la teoria, ma è lavorando su codebase, reali prive di test, che
ho capito come applicarli in maniera efficace. In questo talk condivido la mia
esperienza: come identificare i punti critici di un’applicazione, come decidere
quali test scrivere per primi e come usare mock e altre tecniche che ho trovato
utili per integrare il TDD in progetti già esistenti"
---

# From Zero to Tested

<img class="w-25" width="25%" src="./imgs/slide-qr-code.png" />

Come aggiungere test a un progetto esistente
https://buglil.github.io/Talks/from-zero-to-tested/#/

---

Come ci si trova immischiati <br/>
un progetto privo di test?

---

## Lunedì mattina ore 9:00

---

"Buongiorno Lorenzo,  <br/>
il nostro cliente `Acme.corp` ha un loro `e-commerce`. <br/>
Vogliono una `modifica urgente` entro questo `venerdì`!  <br/>
L'azienda che lo ha sviluppato e' `fallita`, <br/>
e dobbiamo assolutamente occuparcene noi!"
<!-- .element class="align-left" -->

---

"...occuparcene noi!..."

---

## Situazione rosea

- Conoscenza del codice pari a zero 
<!-- .element class="fragment align-left" -->
- Zero test, zero documentazione
<!-- .element class="fragment" -->
- Non so come funziona l'ecommerce del cliente
<!-- .element class="fragment" -->

---

## Il mio primo pensiero?

---

<img class="w-50" src="./imgs/i-hate-mondays.png" />

---

## Il secondo pensiero

---

Cos'e' che devo fare esattamente?

---

## 12 meetings later...

---

## La richiesta del cliente

"Vogliamo aggiungere delle `allerte automatiche` nel nostro `e-commerce`. Quando
un prodotto scende sotto la una soglia di `scorta minima`, il sistema deve
mandare una `email` al responsabile"
<!-- .element class="align-left" -->

---

## I dettagli

- Ogni prodotto ha una propria "scorta minima"
<!-- .element class="fragment" -->
- Il sistema deve controllare ogni ora
<!-- .element class="fragment" -->
- Email con lista prodotti sotto scorta
<!-- .element class="fragment" -->
- Non inviare email duplicate nelle 24h
<!-- .element class="fragment" -->

---

## Martedi' 

---

Un primo sguardo al codice

---

<img class="w-75" src="./imgs/the-what-face.png" />

---

<img class="w-75" src="./imgs/facepalm.png" />

---


---
<!-- Non toccare questa parte -->

## Com'e' andata a finire?

- Consegnato venerdì pomeriggio
<!-- .element class="fragment" -->

- Zero bug aggiunti
<!-- .element class="fragment" -->

- Batteria di test automatici per modifiche future
<!-- .element class="fragment" -->

---

Cliente molto soddisfatto!

---

Il mio capo ha avuto un aumento!

---

Io ovviamente no..

---

Ma sono ugualmente soddisfatto

---

Quella sfida ha portato ad un `framework` utile 
per `combattere` codice `legacy privo di test` <br>
in decine di occasioni 

---

Ma non smettero' mai di odiare i lunedì mattina

<img class="w-25" src="./imgs/i-hate-mondays.png" />

---



# Grazie!

<img class="w-25" width="25%" src="./imgs/slide-qr-code.png" />

Lorenzo Bugli - @BugliL
<!-- .element class="fragment" -->

---



