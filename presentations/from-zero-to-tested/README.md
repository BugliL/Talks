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

# Maggiori dettagli

"Metteremo in vendita una nuova categoria di prodotti, i `prodotti biologici`.
Questi prodotti perdono qualità più velocemente ogni giorno.
Dobbiamo aggiornare il sistema per gestire delle `regole personalizzate`!"
<!-- .element class="align-left" -->

---

## Martedi' 

---

Un primo sguardo al codice

---

<img class="w-75" src="./imgs/the-what-face.png" />

---

```python
def update_products_end_of_day(self):
  for item in get_items():
    if item.name != "Formaggio Brie" and item.name != "Promozione Speciale":
      if item.quality > 0:
        if item.name != "Miele":
          item.quality = item.quality - 1
    else:
      if item.quality < 50:
        item.quality = item.quality + 1
        if item.name == "Promozione Speciale":
          if item.expiration_days < 11:
            if item.quality < 50:
                            item.quality = item.quality + 1
          if item.expiration_days < 6:
            if item.quality < 50:
                            item.quality = item.quality + 1

    if item.name != "Miele":
      item.expiration_days = item.expiration_days - 1

    if item.expiration_days < 0:
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
```
<!-- .element class="fullscreen"  -->

---

<img class="w-75" src="./imgs/facepalm.png" />

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

# Riferimenti

- [Gilded Rose Kata](https://github.com/NotMyself/GildedRose)

