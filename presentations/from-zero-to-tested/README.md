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

## Il mio primo pensiero?

---

*@#!$%&!?*

<img class="w-25" src="./imgs/i-hate-mondays.png" />

---

## Il secondo pensiero

---

Cosa devo fare esattamente?

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

# 1. Analisi del software ma come utente

---

# TODO: spiegare l'importanza di capire il contesto da un punto di vista
# dell'utilizzatore prima di addentrarsi nel codice spiegando che mi sono 
# messo accanto ad un operatore ed ho chiesto direttamente come lavora e come
# la richiesta fosse utile

---

# 2. Analisi struttura del software 

---

## I moduli del software

- 📊 La gestione dell'inventario
<!-- .element class="fragment" -->
- ⏰ Un sistema di scheduling  
<!-- .element class="fragment" -->
- 📧 L'invio di email
<!-- .element class="fragment" -->
- 🗄️ Il database per le configurazioni
<!-- .element class="fragment" -->

---

## Il problema

Non so dove sono questi pezzi nel codice!
<!-- .element class="fragment" -->

E se li rompo mentre li modifico?
<!-- .element class="fragment" -->

---

## Passo 1: Capire il contesto

Prima di scrivere un singolo test
<!-- .element class="fragment" -->

Devo capire cosa sto guardando
<!-- .element class="fragment" -->

---

## Analisi della struttura

- Come è organizzato il progetto?
<!-- .element class="fragment" -->
- Quali tecnologie usa?
<!-- .element class="fragment" -->  
- Che pattern architetturali?
<!-- .element class="fragment" -->
- Database? API esterne? File system?
<!-- .element class="fragment" -->

---

## Cosa fa operativamente?

Non mi interessa il codice
<!-- .element class="fragment" -->

Mi interessa il business
<!-- .element class="fragment" -->

"Questo gestionale cosa gestisce esattamente?"
<!-- .element class="fragment" -->

---

## Il mio approccio

📂 Esploro la struttura delle cartelle
<!-- .element class="fragment" -->

🔍 Cerco file di configurazione
<!-- .element class="fragment" -->

📄 Leggo README, commenti, documentazione (se esiste)
<!-- .element class="fragment" -->

🚀 Avvio l'applicazione e la uso
<!-- .element class="fragment" -->

---

## Nel caso di Acme.corp

Era un gestionale magazzino
<!-- .element class="fragment" -->

- Carico merce
<!-- .element class="fragment" -->
- Scarico merce  
<!-- .element class="fragment" -->
- Inventario
<!-- .element class="fragment" -->
- Report per il management
<!-- .element class="fragment" -->

---

## Architettura scoperta

- Frontend: PHP con jQuery
<!-- .element class="fragment" -->
- Backend: MySQL database
<!-- .element class="fragment" -->
- File CSV per import/export
<!-- .element class="fragment" -->
- Nessun framework, tutto custom
<!-- .element class="fragment" -->

---

## Il punto di partenza

Ora so COSA testa
<!-- .element class="fragment" -->

Non come testarlo ancora
<!-- .element class="fragment" -->

Ma so quale comportamento devo preservare
<!-- .element class="fragment" -->

---

## Passo 2: Creare la rete di sicurezza

---

## Il principio

Prima di cambiare qualsiasi cosa
<!-- .element class="fragment" -->

Devo sapere se ho rotto qualcosa
<!-- .element class="fragment" -->

I test sono i miei sensori
<!-- .element class="fragment" -->

---

## Che tipo di test?

Non test unitari!
<!-- .element class="fragment" -->

Test che verificano il comportamento esistente
<!-- .element class="fragment" -->

"Characterization tests"
<!-- .element class="fragment" -->

---

## I miei test di caratterizzazione

✅ **End-to-End**: Testo i flussi principali dall'interfaccia
<!-- .element class="fragment" -->

✅ **Integration**: Testo database e file CSV
<!-- .element class="fragment" -->

✅ **Contract**: Verifico che le API interne funzionino
<!-- .element class="fragment" -->

---

## Esempio concreto

Test E2E per "Carico merce":
<!-- .element class="fragment" -->

1. Apro la pagina di carico
<!-- .element class="fragment" -->
2. Inserisco: Prodotto X, Quantità 10
<!-- .element class="fragment" -->
3. Clicco "Salva"
<!-- .element class="fragment" -->
4. Verifico che appaia nella lista magazzino
<!-- .element class="fragment" -->

---

## Il risultato

Non so come funziona il codice
<!-- .element class="fragment" -->

Ma so che questo comportamento deve rimanere
<!-- .element class="fragment" -->

Se il test fallisce, ho rotto qualcosa
<!-- .element class="fragment" -->

---
