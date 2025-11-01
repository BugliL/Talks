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

Perdita di tempo in debugging 

---

Impossibile aggiungere nuove funzionalita' <br>
senza paura di rompere qualcosa

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

## La situazione che tutti conosciamo

---

## Lunedì mattina, ore 9:00

---

Il cliente ci ha chiesto una modifica su questo progetto

---

Lo seguiva Franco, si e' licenziato 3 mesi fa <br>
Sei la persona piu' adatta per farlo!

---

So che non conosci il codice, ma che sara' mai!

---

Mi racommando, fallo entro venerdì e con 0 downtime!

---

## Cosa trovi davanti?

- Codice scritto da qualcun altro
<!-- .element class="fragment" -->
- Zero test, zero documentazione
<!-- .element class="fragment" -->
- Funziona... ma non sai come
<!-- .element class="fragment" -->
- E devi modificarlo
<!-- .element class="fragment" -->

---

Dovete aggiungere una nuova feature <br>
toccando codice vecchio integrandone altro

---

## Da dove si inizia iniziamo?

---