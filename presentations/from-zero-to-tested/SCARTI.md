
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














---

```python
def daily_sales_report():
    global connection, cursor, total_sales, yesterday_date, email_server
    # ...
```

---

```python[8,16|22]
def daily_sales_report():
    # ...
    
    for s in sales:
        total_sales += s[3]
        report_text = report_text + "Vendita ID: " + str(s[0]) + " - "
        if s[4] == 1:
            cursor.execute("UPDATE customer_stats SET visits = visits + 1 WHERE id = " + str(s[7]))
            cash_sales += s[3]
            report_text = report_text + "PICCOLO - "
        else:
            report_text = report_text + "CARTA - "
            card_sales += s[3] * 0.95
            discount_amount += s[3] * 0.05
            now = datetime.now()
            cursor.execute("INSERT INTO promotions_used VALUES (" + str(s[0]) + ", 'CARD_DISCOUNT', '" + str(now) + "')")
            report_text = report_text + "SCONTO CARTA 5% - "
        report_text = report_text + "€" + str(s[3]) + "\n"
    
    # ...

    email_server.sendmail("manager@acme.com", report_text)
    cursor.execute("INSERT INTO email_log VALUES ('" + str(datetime.now()) + "', 'manager@acme.com', 'REPORT_SENT')")
    f = open("/tmp/sales_" + str(datetime.now().date()) + ".txt", "w")
    f.write(report_text)
    f.close()
    cursor.execute("UPDATE stats SET last_report = '" + str(datetime.now()) + "'")
    cursor.execute("UPDATE stats SET total_reports = total_reports + 1")
    connection.commit()
```
<!-- .element class="fullscreen"  -->
---
