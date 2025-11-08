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

## Lunedì mattina ore 9:00 - Il briefing

---

"Buongiorno Lorenzo,  <br/>
il nostro cliente `Acme.Corp` è un supermercato con un gestionale custom. 
Vogliono una `nuova funzionalità` entro questo `venerdì`!
L'azienda che lo ha sviluppato è `fallita` e dobbiamo assolutamente occuparcene noi!"
<!-- .element class="align-left" -->

---

"...occuparcene noi!..."

---

## Situazione rosea

- Conoscenza del codice pari a zero 
<!-- .element class="fragment align-left" -->
- Zero test, zero documentazione
<!-- .element class="fragment" -->
- Non so come funziona il programma
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

## Il contesto

- Tutti i prodotti hanno una proprietà che 
  indica quanti `giorni` mancano alla `data di scadenza`.

- Tutti i prodotti hanno una proprietà che 
  denota il `valore` dell'articolo

---

## Il contesto

- Alla `fine di ogni giornata` il sistema `decrementa`
  entrambe le proprietà per ogni prodotto 

- Alcuni prodotti hanno `regole speciali`, come le
  `promozioni speciali` che hanno regole personalizzate

---

## Maggiori dettagli

"Metteremo in vendita una nuova categoria di prodotti, i `prodotti biologici`.
Questi prodotti perdono qualità più velocemente ogni giorno. Dobbiamo
aggiornare il sistema per gestire delle `nuove regole personalizzate` e
aggiungere una voce per il report delle vendite giornaliere.
<!-- .element class="align-left" -->

<!-- C'e' un altra funzionalita' da integrare ma stiamo ancora definendo i dettagli."-->

---

Ho concluso la giornata portandomi il `codice in locale` con un `backup`
del `database` per poter iniziare a guardare il codice e sopratutto `provare`
il `software` .
<!-- .element class="align-left" -->

---

Alla fine la richiesta del cliente e' semplice, no?

---

Ingenuo...

---

## Martedi' 

---

## Un primo sguardo al codice

---

Prendiamo un pezzo a caso del codice

---

<img class="w-75" src="./imgs/the-what-face.png" />

---

```python
def update_products_end_of_day():
  cursor.execute("SELECT id, name, exp_days, quality FROM products")
  for item in cursor.fetchall():
    if item.name != "Formaggio Brie" and item.name != "Promozione Speciale":
      if item.quality > 0:
        if item.name != "Miele":
          item.quality = item.quality - 1
    else:
      if item.quality < 50:
        item.quality = item.quality + 1
        if item.name == "Promozione Speciale":
          if item.exp_days < 11:
            if item.quality < 50:
                            item.quality = item.quality + 1
          if item.exp_days < 6:
            if item.quality < 50:
                            item.quality = item.quality + 1
    if item.name != "Miele":
      item.exp_days = item.exp_days - 1
    if item.exp_days < 0:
      if item.name != "Formaggio Brie":
        if item.name != "Promozione Speciale":
          if item.quality > 0:
            if item.name != "Miele":
                            item.quality = item.quality - 1
        else:
          item.quality = item.quality - item.quality
      else:
        if item.quality < 50:
          item.quality = item.quality + 1
  for item in items:
    cursor.execute(
      "UPDATE products SET exp_days = ?, quality = ? WHERE id = ?",
      (item.exp_days, item.quality, item.id)
    )
  connection.commit()
```
<!-- .element class="fullscreen"  -->

---

<img class="w-75" src="./imgs/facepalm.png" />

---

## Caratteristiche principali del codice

- Wall of code unico `non strutturato`
<!-- .element class="fragment" -->

- Impossibile da toccare `senza rompere` qualcosa
<!-- .element class="fragment" -->

---

Quella modifica che doveva essere fatta <br/>
in `mezza giornata` non era possibile

---

Come si affronta un mostro del genere?

---

Si capisce la `funzionalita' alto livello` del sistema
<!-- .element class="align-left" -->

Si ricerca nel codice `dove` e `come` e' stata implementata
<!-- .element class="fragment align-left" -->

---

Il risultato di questa prima analisi dovrebbe essere:

- Una descrizione del `comportamento attuale` 
<!-- .element class="fragment" -->

- Un mapping tra la descrizione e il `codice sorgente`
<!-- .element class="fragment" -->

---

```python
def update_products_end_of_day():
  cursor.execute("SELECT id, name, exp_days, quality FROM products")
  for item in cursor.fetchall():
    if item.name != "Formaggio Brie" and item.name != "Promozione Speciale":
      if item.quality > 0:
        if item.name != "Miele":
          item.quality = item.quality - 1
    else:
      if item.quality < 50:
        item.quality = item.quality + 1
        if item.name == "Promozione Speciale":
          if item.exp_days < 11:
            if item.quality < 50:
                            item.quality = item.quality + 1
          if item.exp_days < 6:
            if item.quality < 50:
                            item.quality = item.quality + 1
    if item.name != "Miele":
      item.exp_days = item.exp_days - 1
    if item.exp_days < 0:
      if item.name != "Formaggio Brie":
        if item.name != "Promozione Speciale":
          if item.quality > 0:
            if item.name != "Miele":
                            item.quality = item.quality - 1
        else:
          item.quality = item.quality - item.quality
      else:
        if item.quality < 50:
          item.quality = item.quality + 1
  for item in items:
    cursor.execute(
      "UPDATE products SET exp_days = ?, quality = ? WHERE id = ?",
      (item.exp_days, item.quality, item.id)
    )
  connection.commit()
```
<!-- .element class="fullscreen"  -->

---


```python
def update_products_end_of_day():
  cursor.execute("SELECT id, name, exp_days, quality FROM products")

  for item in cursor.fetchall():
    # .... condizioni varie

  for item in items:
    cursor.execute(
      "UPDATE products SET exp_days = ?, quality = ? WHERE id = ?",
      (item.exp_days, item.quality, item.id)
    )
  connection.commit()
```

---

## Si scrivono dei <br/> `characterization tests`

---

## Characterization tests

Sono test che verificano il `comportamento esistente` del sistema
non di come dovrebbe funzionare
<!-- .element class="align-left" -->

Hanno lo scopo di creare uno `snapshot funzionale`
per poter cambiare il codice in sicurezza
<!-- .element class="fragment align-left" -->

---

## Characterization tests

Sono dei test `ad alto livello`, spesso `end-to-end` oppure `di integrazione`
<!-- .element class="align-left" -->

Testano blocchi di codice `grandi` oppure `sezioni intere` del sistema
<!-- .element class="fragment align-left" -->

---

<img class="w-60" src="./imgs/tdd.png" />

---

## Characterization tests vs TDD

- Si scrivono dei test `verdi`, senza toccare la funzionalita'
<!-- .element class="fragment align-left" -->

- Si `rifattorizza` il codice mantenendo i test verdi
<!-- .element class="fragment align-left" -->

- Si aggiunge la `nuova funzionalita'` mantenendo i test verdi
<!-- .element class="fragment align-left" -->

---

```python
def update_products_end_of_day():
  cursor.execute("SELECT id, name, exp_days, quality FROM products")
  for item in cursor.fetchall():
    if item.name != "Formaggio Brie" and item.name != "Promozione Speciale":
      if item.quality > 0:
        if item.name != "Miele":
          item.quality = item.quality - 1
    else:
      if item.quality < 50:
        item.quality = item.quality + 1
        if item.name == "Promozione Speciale":
          if item.exp_days < 11:
            if item.quality < 50:
                            item.quality = item.quality + 1
          if item.exp_days < 6:
            if item.quality < 50:
                            item.quality = item.quality + 1
    if item.name != "Miele":
      item.exp_days = item.exp_days - 1
    if item.exp_days < 0:
      if item.name != "Formaggio Brie":
        if item.name != "Promozione Speciale":
          if item.quality > 0:
            if item.name != "Miele":
                            item.quality = item.quality - 1
        else:
          item.quality = item.quality - item.quality
      else:
        if item.quality < 50:
          item.quality = item.quality + 1
  for item in items:
    cursor.execute(
      "UPDATE products SET exp_days = ?, quality = ? WHERE id = ?",
      (item.exp_days, item.quality, item.id)
    )
  connection.commit()
```
<!-- .element class="fullscreen"  -->

---


---

## Mercoledi' 

---

## Rifattorizzazione

---


```python
def update_products_end_of_day():
  cursor.execute("SELECT id, name, exp_days, quality FROM products")

  for item in cursor.fetchall():
    # .... condizioni varie

  for item in items:
    cursor.execute(
      "UPDATE products SET exp_days = ?, quality = ? WHERE id = ?",
      (item.exp_days, item.quality, item.id)
    )
  connection.commit()
```

--- 

## Introduce variable

Per disaccoppiare il codice il piu' possibile
si puo' introdurre una variabile temporanea `items`
che contenga i prodotti letti dal database

---

```python
def update_products_end_of_day():
  cursor.execute("SELECT id, name, exp_days, quality FROM products")
  items = cursor.fetchall()

  for item in items:
    # .... condizioni varie

  for item in items:
    cursor.execute(
      "UPDATE products SET exp_days = ?, quality = ? WHERE id = ?",
      (item.exp_days, item.quality, item.id)
    )
  connection.commit()
```

---

Toccare il codice senza `characterization tests` e' pericoloso, 
va fatto con `cautela` e `molta attenzione`

---

#TODO: CONTINUE HERE

---


## Giovedi'

---

Implementazione della funzionalita'

---

<!-- Non toccare questa parte -->

## Venerdi' 

---

## La conclusione

---

## Com'e' andata a finire?

- Consegnate tutte le modifiche
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

Io una pacca sulla spalla

---

Ma sono ugualmente soddisfatto...

---

Quella sfida ha portato ad un `framework` utile 
per `combattere` codice `legacy privo di test` <br>
in decine di occasioni
<!-- .element class="align-left" -->

---

... in ogni caso

---

<img class="w-50" src="./imgs/i-hate-mondays.png" />

---



# Grazie!

<img class="w-25" width="25%" src="./imgs/slide-qr-code.png" />

Lorenzo Bugli - @BugliL
<!-- .element class="fragment" -->

---

# Riferimenti

- [Gilded Rose Kata](https://github.com/NotMyself/GildedRose)
- Working Effectively with Legacy Code <br/>
  *Michael Feathers*

- Refactoring: Improving the Design of Existing Code <br/>
  *Martin Fowler*

