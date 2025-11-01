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

Ci sono diverse risposte...

---

"Dobbiamo rilasciare entro ieri!"
<!-- .element class="fragment" -->

"Non c'e' tempo per sviluppare anche i test!"
<!-- .element class="fragment" -->

---

"Sono inutili, l'applicazione funziona lo stesso senza!"
<!-- .element class="fragment" -->

"Perche' perdere tempo per fare lavoro in piu' ?"
<!-- .element class="fragment" -->

---

"Lascia stare i test, lo facciamo provare a mano!"

---

"Li possiamo sempre aggiungere dopo!"

---

## Il risultato?

---

"Non lo cambiare oppure non funziona piu'!"
<!-- .element class="fragment" -->

"Non lo toccare, non so cosa fa quel codice!"
<!-- .element class="fragment" -->

"Come non funzionano piu' le email? <br/> Ho cambiato solo un'etichetta!"
<!-- .element class="fragment" -->

---


## In breve...

---

Spaghetti code instabile e fragile

---

Impossibile aggiungere nuove funzionalita' <br>
senza paura di rompere qualcosa

---

Perdita di tempo in debugging 

---

# 😭

Conviene quasi buttare tutto <br>
il codice e ricominciare da zero

---

# 🤔

oppure no...

---

## Da “zero” al primo test

---

## Il caso peggiore

---

## Il caso peggiore

Sapendo come gestire il caso peggiore, tutti gli altri sono
casi piu' semplici e meno complicati

---

## Il caso peggiore

- Vi trovate su un progetto che non conoscete
<!-- .element class="fragment" -->
- L'applicazione e' in produzione e sta funzionando correttamente.
<!-- .element class="fragment" -->
- Documentazione.... che?
<!-- .element class="fragment" -->
- Chi ci ha lavoravo e' scappato in Brasile
<!-- .element class="fragment" -->

---

## In poche parole

- Non sapete da dove partire 
<!-- .element class="fragment" -->
- I rilasci non si possono fare alla leggera
<!-- .element class="fragment" -->
- La sola documentazione e' il codice 
<!-- .element class="fragment" -->
- Non avete nessuno a cui chiedere
<!-- .element class="fragment" -->

---

Dovete aggiungere una nuova feature <br>
modificando codice gia' scritto e aggiungerne altro

---

## Qual'e' la prima cosa da fare?

---

Panoramica ad alto livello

- Capire quali sono i sistemi coinvolti
<!-- .element class="fragment" -->
- Capire la struttura del software da modificare
<!-- .element class="fragment" -->

---

TODO:



<!-- TODO: Slide Talk is cheap, show me the code -->
<!-- TODO: Dimostrare come i mock salvano la vita -->
<!-- TODO: Approfondimento per microservizi -->