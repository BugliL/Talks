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
il nostro cliente `Acme.corp` ha un gestionale interno. <br/>
Vogliono una `modifica urgente` entro questo `venerdì`! <br/>
L'azienda che lo ha sviluppato e' `fallita`, e dobbiamo assolutamente 
occuparcene noi!"
<!-- .element class="align-left" -->

---

"...occuparcene noi!..."

---

## Situazione rosea

- Conoscenza del codice pari a zero 
<!-- .element class="fragment align-left" -->
- Zero test, zero documentazione
<!-- .element class="fragment" -->
- Conosco l'azienda <br>
  ma non so come funziona il programma
<!-- .element class="fragment" -->

---

Il mio primo pensiero?

---

*@#!$%&!? 

<img class="w-25" width="10%" src="./imgs/i-hate-mondays.png" />

---

## Da dove ho iniziato?

---
