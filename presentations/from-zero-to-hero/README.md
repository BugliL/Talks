---
title: From Zero to Tested
author: Lorenzo Bugli
footer: 2025-11-26 - TSH - Firenze
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

---

## Perche' i software sono privi di test automatici?

---

Nei team sono presenti una o piu' persone che si oppongono allo sviluppo dei
test

---

## 🏃🏻‍➡️ L'impaziente

Dobbiamo correre, il progetto e' in ritardo!
<!-- .element class="fragment" -->

Dobbiamo rilasciare entro ieri! 
<!-- .element class="fragment" -->

Non c'e' tempo per sviluppare anche i test!
<!-- .element class="fragment" -->

---

## 🤷🏻‍♂️ L'ignaro

Se il codice e' scritto bene non servono!
<!-- .element class="fragment" -->

I test sono inutili per far funzionare l'applicazione!
<!-- .element class="fragment" -->

---

## 🦸🏻‍♂️ L'impavido

Lascia stare i test, lo facciamo provare a mano!
<!-- .element class="fragment" -->

I test lo faranno i clienti in produzione su casi reali!
<!-- .element class="fragment" -->

---

## 😎 L'ottimista

Non li facciamo adesso, ci sara' tempo dopo!
<!-- .element class="fragment" -->

Li possiamo sempre aggiungere dopo! 
<!-- .element class="fragment" -->

---

## Il risultato?

---

Non lo cambiare oppure non funziona piu'!
<!-- .element class="fragment" -->

Non lo toccare, non so cosa fa quel codice!
<!-- .element class="fragment" -->

Come non funzionano piu' le email? <br/> Ho cambiato solo un'etichetta!
<!-- .element class="fragment" -->

---

## Il risultato?

Codice instabile
<!-- .element class="fragment" -->

Rallenta lo sviluppo di nuove funzionalita' a causa dei bug
<!-- .element class="fragment" -->

Conviene buttare tutto e ricominciare da zero
<!-- .element class="fragment" -->

---

oh forse no...

non e' mai troppo tardi!
<!-- .element class="fragment" -->

---

## Da “zero” al primo test

---

## Progetto di esempio
Un'applicazione web per la gestione di un e-commerce

---