---
title: Collaborazione Efficace tra Team di Sviluppo e Stakeholder
author: Lorenzo Bugli
footer: 2024-11-26 - Nana Bianca, Firenze
footerIconUrl: https://www.schroedinger-hat.org/assets/sh-logo-big-UQdXK547.png
---

# Collaborazione Efficace tra team di sviluppo e Stakeholder
Costruire Software Funzionante  
con approccio ATDD


## Abstract
<!-- .element: style="display: none" -->
Nel moderno sviluppo software, la stretta collaborazione tra il team di sviluppo
e gli stakeholder è essenziale per creare soluzioni che rispondano efficacemente
ai requisiti di business. Questo talk esplora come l'Acceptance Test-Driven
Development (ATDD) possa guidare questa collaborazione, riducendo sprechi e
garantendo che il software cresca in modo funzionale e allineato alle esigenze
reali.
<!-- .element: style="display: none" -->

L'ATDD permetta al team di sviluppo e agli stakeholder di definire insieme i
requisiti sotto forma di test di accettazione, che guidano la realizzazione
tecnica e assicurano che ogni funzionalità risponda ai bisogni reali. Questo
approccio aiuti a prevenire incomprensioni a ridurre gli sprechi, concentrando
il lavoro su ciò che è essenziale e immediatamente verificabile.
<!-- .element: style="display: none" -->

Il processo test-first crea un sistema di verifica continua, garantendo che il
software funzioni correttamente e soddisfi costantemente le aspettative degli
utenti.
<!-- .element: style="display: none" -->

Con esempi pratici e casi di studio veri, i partecipanti scopriranno come a
partire da un'analisi preliminare, tutto il lavoro successivo affrontato con
l'ATDD trasformi la collaborazione tra team di sviluppo e stakeholder orientata
ai risultati e capace di produrre software di qualità che soddisfi i bisogni del
business fin dalle prime iterazioni.
<!-- .element: style="display: none" -->

---

Collaborazione Efficace  
tra team di sviluppo e <span class="fragment highlight-current-blue" data-fragment-index="2">Stakeholder</span>

---

## Stakeholder?

<!-- hidden-start --> 
> Wikipedia - un soggetto coinvolto in un progetto con interessi legati
all’esecuzione o dall’andamento del progetto stesso.

Da questa definizione possiamo capire che uno stakeholder è una persona che ha
un interesse diretto o indiretto in un progetto. Essendo il significato molto
generico, il termine indica persone diverse a seconda del contesto in cui viene
utilizzato.

Uno stakeholder di un progetto software e' qualcuno che interesse nella sua
realizzazione, potrebbe essere un utente vero e proprio oppure un manager che
aumenta la produttivita' dei propri dipendenti con l'adozione di un software
specifico oppure un utente, un utilizzatore vero e proprio del software.

Nel caso di una software house che sviluppa software per terze parti, la parola
stakeholder identifica principalmente il cliente che commissiona il lavoro, che
prende il nome di *committente*.

Nel caso di un'azienda che sviluppa software per uso interno, la parola
stakeholder assume un significato piu' esteso. In questo caso si tende a
identificare tutti i soggetti coinvolti nello scrivere le specifiche funzionali
del software, tutte le persone a cui chiedere chiarimenti quando si deve
progettare una nuova funzionalita' ed ovviamente tutti i manager interessati
nella riuscita del progetto.

<!-- hidden-end --> 

In questo contesto gli stakeholder sono tutti coloro che possiedono la
conoscenza da inserire all'interno del software.  
<!-- .element: class="fragment align-left" -->

I detentori della conoscenza di dominio.
<!-- .element: class="fragment align-left" -->

---

<!-- hidden-start --> 
Alla luce di queste considerazioni possiamo sostituire la definizione della
parola *stakeholder* con quella di *detentore della conoscenza di dominio*.
<!-- hidden-end --> 

<span class="fragment highlight-current-blue" data-fragment-index="1">Collaborazione Efficace</span> 
tra team di sviluppo e <span class="fragment highlight-current-blue" data-fragment-index="0">detentori della conoscenza di dominio</span>

---

## Collaborazione efficace?

<!-- hidden-start --> 
Un collaborazione tra più persone consiste in un insieme di azioni coordinate
per raggiungere un obiettivo comune, nel caso di sviluppo software e' la
realizzazione dello stesso. 

Detentori della conoscenza di dominio e sviluppatori devono lavorare insieme per
creare un software che risolve un problema, un software che funzioni.

La collaborazione tra le persone e' scontata, tutti lavorano insieme per
conseguire un obiettivo almeno condiviso ma non sempre si fa in modo efficace.
Capita spesso di dover ripetere piu' volte la stessa cosa, di dover spiegare piu'
volte la stessa cosa in meeting interminabili. 

Collaborare in modo efficace significa farlo nel modo migliore possibile,
riducendo sprechi di tempo e di risorse il piu' possibile.
<!-- hidden-end -->

Lavorare insieme per un obiettivo comune minimizzando le energie utilizzate
nello svolgere il proprio lavoro.
<!-- .element: class="fragment" -->

---

<!-- hidden-start --> 
Adesso possiamo sostituire anche la definizione di *Collaborazione efficace*
<!-- hidden-end --> 


<span class="fragment highlight-current-blue" data-fragment-index="0">
Collaborazione </span> tra team di sviluppo e detentori della conoscenza di
dominio 
<span class="fragment highlight-current-blue" data-fragment-index="0">
per <span class="fragment highlight-current-blue" data-fragment-index="1"> sviluppare software </span>
minimizzando le energie spese nello svolgere il proprio lavoro</span>


<!-- hidden-start --> 
Per poter capire come ATDD aiuti a svolgere il proprio lavoro va capito in cosa
consiste nella pratica lo sviluppo di un software.
<!-- hidden-end --> 

---

## Sviluppare un software

<svg xmlns="http://www.w3.org/2000/svg" viewBox="25.7654 77.4812 554.5891 333.8141" width="560px" height="350px">
    <defs>
        <marker id="arrow" markerWidth="10" markerHeight="10" refX="0" refY="3" orient="auto">
            <polygon points="0 0, 10 3, 0 6" fill="#FFF"/>
        </marker>
    </defs>
    <g>
        <circle cx="65.112" cy="217.001" r="50" fill="#4CAF50" transform="matrix(1.3855040073394775, 0, 0, 0.730679988861084, 4.827639102935791, 137.2889251708984)" style=""/>
        <text x="65.112" y="217.001" text-anchor="middle" alignment-baseline="middle" fill="white" font-size="18" style="white-space: pre; font-size: 18px;" transform="matrix(1.3855040073394775, 0, 0, 1.4667739868164062, 4.3534369468688965, -18.83134651184082)">Specifiche</text>
    </g>
    <!-- .element: class="fragment" -->
    <line x1="120.188" y1="254.137" x2="165.873" y2="164.013" stroke-width="2" marker-end="url(#arrow)" style="stroke: rgb(255, 255, 255);"/>
    <!-- .element: class="fragment" -->
    <g class="fragment">
        <circle cx="179.391" cy="90.891" r="50" fill="#2196F3" style="" transform="matrix(1.804677963256836, 0, 0, 0.6837040185928345, -84.07099151611328, 49.52389907836914)"/>
        <text x="179.391" y="90.891" text-anchor="middle" alignment-baseline="middle" fill="white" font-size="18" style="white-space: pre; font-size: 18px;" transform="matrix(1.3855040073394775, 0, 0, 1.4667739868164062, -4.5809268951416025, -21.12238311767578)">Progettazione</text>
    </g>
    <!-- .element: class="fragment" -->
    <line x1="337.138" y1="131.323" x2="421.981" y2="182.702" stroke-width="2" marker-end="url(#arrow)" style="stroke: rgb(255, 255, 255);"/>
    <!-- .element: class="fragment" -->
    <g>
        <circle cx="317.19" cy="110.303" r="50" fill="#FF9800" style="" transform="matrix(2.118403911590576, 0, 0, 0.6253920197486877, -197.5022735595703, 164.11874389648435)"/>
        <text x="338.956" y="171.921" text-anchor="middle" alignment-baseline="middle" fill="white" font-size="18" style="white-space: pre; font-size: 18px;" transform="matrix(1.3855040073394775, 0, 0, 1.4667739868164062, 4.3534369468688965, -18.83134651184082)">Implementazione</text>
    </g>
    <!-- .element: class="fragment" -->
    <line x1="446.788" y1="270.789" x2="375.648" y2="347.26" stroke-width="2" marker-end="url(#arrow)" style="stroke: rgb(255, 255, 255);"/>
    <!-- .element: class="fragment" -->
    <g> 
        <circle cx="212.258" cy="276.671" r="48.992" fill="#F44336" transform="matrix(1.3855040073394775, 0, 0, 0.6161110401153564, 10.05459213256836, 210.6507873535156)" style=""/>
        <text x="212.258" y="276.671" text-anchor="middle" alignment-baseline="middle" fill="white" font-size="18" style="white-space: pre; font-size: 18px;" transform="matrix(1.3855040073394775, 0, 0, 1.4667739868164062, 10.690991401672363, -24.157814025878906)">Feedback</text>
    </g>
    <!-- .element: class="fragment" -->
    <line x1="229.298" y1="382.92" x2="165.151" y2="336.923" stroke-width="2" marker-end="url(#arrow)" style="stroke: rgb(255, 255, 255);"/>
    <!-- .element: class="fragment" -->
</svg>

<!-- hidden-start -->

Lo sviluppo di un software puo' essere suddiviso in 4 fasi principali: 
 - Raccolta delle specifiche
 - Progettazione del sistema
 - Implementazione del software
 - Verifiche e feedback

Sia in un sistema Agile che in uno tradizionale, queste fasi sono presenti e
sono tutti passaggi obbligatori per la realizzazione di un software funzionante.
Questi cicli sono ripetuti piu' volte fino alla realizzazione del software.

### Raccolta delle specifiche
Questa e' una fase delicata in cui si cerca di capire cosa il software deve fare
e sopratutto qual'e' il problema che deve risolvere.

Si interrogano le persone che commissionano il software cercando di capire il 
problema da risolvere e quali sono le funzionalita' da realizzare.

### Progettazione del sistema
Questa e' la fase in cui si cerca di capire come realizzare il software da un
punto di vista tecnico e funzionale. Si definiscono a grandi linee
l'architettura del software e le funzionalita' da costruire.

### Implementazione del software
Questa e' la fase in cui si realizza il software vero e proprio. Si scrive il
codice e si realizzano le funzionalita' previste nella fase di progettazione.

Si crea l'architettura a supporto e si realizzano le funzionalita' previste.

### Verifiche e feedback
Dopo la realizzazione si presenta il software ai committenti e si chiede un
feedback sulle funzionalita' sviluppate. Si cerca di capire se il software
realizzato risolve il problema ed in caso di incongruenze si torna alla raccolta
delle specifiche ed alla progettazione del software.

<!-- hidden-end -->

---

## Problemi nello sviluppo software 

Specifiche errate o incomplete
<!-- .element: class="fragment" -->

Cattiva comunicazione con gli stakeholder
<!-- .element: class="fragment" -->

 


---

<!-- hidden-start -->

# Domande
- Cosa consiste lo sviluppo software
  - Quali sono le fasi principali
  - Quali sono gli sprechi
    - Bug e funzionalita' rotte
    - cosa possiamo fare per ridurli
        - TDD 
    - come si puo' usare i test per ridurre gli errori dall'inizio

  
- Quali sono i vantaggi dell'ATDD nella pratica
    - Differenza tra averli e non averli per lo sviluppo
    - Come si possono usare per collaborare nel team

<!-- hidden-end -->

---

<div class="sources">

### Fonti 

- [Wikipedia - Stakeholder](https://it.wikipedia.org/wiki/Stakeholder)
- [Zero uno web](https://www.zerounoweb.it/software/gli-stakeholder-e-il-loro-punto-di-vista/)


### Libri
<!-- .element: class="mt-1" -->

- [ATDD by Example: A Practical Guide to Acceptance Test-Driven Development](https://www.amazon.it/ATDD-Example-Practical-Acceptance-Test-Driven/dp/0321784154)

</div>

<!-- hidden-start --> 
## Fegatelli

Gli sprechi sono le principali cause di fallimento di un progetto e

Per minimizzazione delle energie non si intendono solo quelle legate alla
scrittura del codice, ai bug ma anche quelle legate alla comunicazione, alla
comprensione dei requisiti e alla verifica del software stesso. 

Costruire Software Funzionante
con approccio <span class="fragment highlight-current-blue" data-fragment-index="1">ATDD</span>

## Minimizzare il lavoro nello sviluppo software?
Come si puo' minimizzare il lavoro nello sviluppo software?

Spesso si fanno degli errori nella raccolta delle specifiche e tutte le fasi
successive ne risentono creando sprechi di tempo e di risorse. Nei casi migliori
si riesce a correggere il tiro in fase di progettazione, nei casi peggiori si
finisce per realizzare un software che non svolge
<!-- hidden-end --> 