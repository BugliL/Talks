---
title: Collaborazione Efficace tra Team di Sviluppo e Stakeholder
author: Lorenzo Bugli
footer: 2024-11-27 - Nana Bianca, Firenze
footerIconUrl: https://www.schroedinger-hat.org/assets/sh-logo-big-UQdXK547.png
revealOptions:
  transition: none
source-code: https://github.com/BugliL/ATTD_TALK
---

# Collaborazione Efficace tra Team di Sviluppo e Stakeholder

Costruire Software Funzionante con approccio ATDD

---

## Introduzione

- **Relatore:** Lorenzo Bugli, Senior Software Engineer presso Fiscozen
- **Community:** Membro di Schroedinger Hat, associazione no profit che promuove l'opensource attraverso progetti di sviluppo software ed eventi

---

## Cos'è l'ATDD?

- **Acceptance Test-Driven Development (ATDD):** Metodologia di sviluppo software che prevede la creazione e l'esecuzione di test di accettazione prima di scrivere codice :contentReference[oaicite:0]{index=0}.
- **Obiettivo:** Allineare lo sviluppo ai requisiti aziendali attraverso la collaborazione tra sviluppatori, tester e stakeholder :contentReference[oaicite:1]{index=1}.

---

## Sfide nella Collaborazione

- **Comunicazione inefficace:** Malintesi tra team di sviluppo e stakeholder.
- **Requisiti ambigui:** Specifiche poco chiare o incomplete.
- **Disallineamento delle aspettative:** Differenze tra ciò che viene sviluppato e ciò che gli stakeholder si aspettano.

---

## Come l'ATDD Migliora la Collaborazione

- **Coinvolgimento degli stakeholder:** Definizione congiunta dei test di accettazione.
- **Chiarezza dei requisiti:** Specifiche tradotte in test concreti e misurabili.
- **Riduzione delle discrepanze:** Allineamento tra requisiti e implementazione.

---

## Processo ATDD

1. **Definizione dei requisiti:** Collaborazione tra sviluppatori e stakeholder per creare criteri di accettazione chiari :contentReference[oaicite:2]{index=2}.
2. **Scrittura dei test di accettazione:** Creazione di test automatizzati basati sui criteri definiti.
3. **Implementazione guidata dai test:** Sviluppo del codice per soddisfare i test di accettazione.
4. **Validazione continua:** Esecuzione dei test per garantire la conformità ai requisiti.

---

## Esempio Pratico

**Scenario:** Assegnazione di colori a documenti in base al loro stato e tipo.

- **Requisito:** I documenti in lavorazione devono essere associati al colore rosso, a meno che non siano di tipo disegno tecnico; in tal caso, devono avere il colore blu.
- **Test di Accettazione:**

  ```gherkin
  Scenario: Assegnazione colore a documenti in lavorazione
    Dato un documento in lavorazione
    E il documento è di tipo disegno tecnico
    Quando viene assegnato un colore
    Allora il colore assegnato deve essere BLU
  ```

---

## Strumenti per l'ATDD

- Framework di testing: Strumenti come Cucumber o SpecFlow per la scrittura di test in linguaggio naturale.
- Piattaforme di collaborazione: Tool come JIRA o Trello per la gestione dei requisiti e dei test.

---

## Best Practices
- Collaborazione attiva: Coinvolgere tutte le parti interessate nella definizione dei test.
- Chiarezza e precisione: Scrivere test con criteri di accettazione chiari e misurabili.
- Automazione dei test: Implementare test automatizzati per garantire efficienza e ripetibilità.

---

## Conclusione
- Riepilogo: L'ATDD facilita una collaborazione efficace tra team di sviluppo e stakeholder, migliorando la qualità del software prodotto.
- Incoraggiamento: Adottare l'ATDD per allineare lo sviluppo ai requisiti aziendali e soddisfare le aspettative degli stakeholder.



