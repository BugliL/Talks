# Backup - Esempi di codice Python completi

Questo file contiene gli esempi di codice Python originali che sono stati semplificati nella presentazione principale per renderla più accessibile a un pubblico misto.

## Esempio 1: Test per documento di tipo distinta materiale

```gherkin
Given documento di tipo distinta materiale non firmata digitalmente
When il sistema assegna un colore al documento
Then il colore associato è il GIALLO
```

```python
from behave import given, then, when
from document import Colori, Documento, StatoDocumento, TipoDocumento
from system import System

@given("documento di tipo distinta materiale non firmata digitalmente")
def given_documento_distinta_materiale_non_firmata_digitalmente(context):
    context.distinta = Documento(
        tipo=TipoDocumento.DISTINTA_MATERIALI,
        stato=StatoDocumento.INVIATO,
        firmato=False,
    )

@when("il sistema assegna un colore al documento")
def when_sistema_assegna_colore(context):
    System.assign_color(context.distinta)

@then("il colore associato è il GIALLO")
def then_colore_associato_is_yellow(context):
    assert context.distinta.colore == Colori.GIALLO
```

## Esempio 2: Test per documento in lavorazione di tipo disegno tecnico

```gherkin
Given un documento in lavorazione di tipo "disegno tecnico"
When il sistema assegna un colore al documento
Then il documento deve essere BLU
```

```python
from behave import given, when, then
from document import Colori, Documento, StatoDocumento, TipoDocumento
from system import System

@given('un documento in lavorazione di tipo "disegno tecnico"')
def given_documento_in_lavorazione_disegno_tecnico(context):
    context.documento = Documento(
        tipo=TipoDocumento.DISEGNO_TECNICO,
        stato=StatoDocumento.LAVORAZIONE,
        firmato=False
    )

@when("il sistema assegna un colore al documento")
def when_sistema_assegna_colore(context):
    System.assign_color(context.documento)

@then("il documento deve essere blu")
def then_documento_deve_essere_blu(context):
    assert context.documento.colore == Colori.BLU
```

## Note

Questi esempi mostrano l'implementazione completa usando:
- **behave**: framework BDD per Python
- **context**: oggetto per condividere stato tra gli step
- **Documento**: classe che rappresenta un documento con tipo, stato e flag di firma
- **System.assign_color()**: metodo che applica la logica di assegnazione del colore

Gli esempi sono tecnicamente corretti e possono essere usati in sessioni tecniche più approfondite o workshop per sviluppatori.
