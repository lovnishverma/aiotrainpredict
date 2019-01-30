Cursus Python apps met Flask: MongoDB database(2)
================================================

We gebruiken hier de MongoDB database samen met een AJAX-interactie tussen browser en server.

AJAX
----

AJAX staat voor Asynchronous JAvaScript XML (interactie).
Tegenwoordig wordt in plaats van XML meestal JSON gebruikt.

De belangrijkste elementen van deze interactie zijn:

* de HTTP-requests worden vanuit JavaScript gedaan.
* de response hiervan bestaat uit data in JSON-vorm (in plaats van een HTML-document)
* deze response wordt door de browser asynchroon verwerkt, als de data binnenkomt

De browser blijft tijdens de interactie tussen de browser en de server beschikbaar voor interactie met de gebruiker.

REST interface (CRUD)
---------------------

Voor de basisopdrachten op de database (CRUD) gebruiken we een REST interface.
(Voor een uitleg over REST, zie: https://restfulapi.net)

We gebruiken de volgende URLs voor het AJAX interface:

* `GET /todos` - (R) vraag de actuele lijst met todo's
* `GET /todos/<todoid>` - (R) vraag informatie over een specifieke todo
* `POST /todos` - (C) maak een nieuwe todo aan (de ID wordt bepaald door de server)
* `PUT /todos/<todoid>` - (U) update een bestaande todo
* `DELETE /todos/<todoid>` - (D) verwijder een bestaande todo

NB: POST is niet *idempotent*, de andere HTTP-opdrachten zijn dat wel.
Ook voor de database is "create" niet idempotent!
Immers, elke create resulteert in een nieuwe ID.

We hebben hiervoor ook een andere constructie nodig in de routering:

```Python
@app("/todos/<id>")
def get_todo(id):
   ...
```

Het `<id>`-gedeelte van de URL wordt als parameter meegegeven aan de functie.
In dit geval gaat het om de `id` (key) van een todo: een integer waarde.


Opmerkingen
-----------

**Commit**: vergeet de `conn.commit()` niet bij INSERT of UPDATE.
Veranderingen in de database worden anders mogelijk niet doorgevoerd.

**Fouten**: er kunnen de nodige fouten optreden tijdens het verwerken van een request.
Er is geen enkele garantie dat de client (browser) het interface correct gebruikt.
Requests kunnen ook door andere programma's dan de eigen app gegenereerd worden.

**Security**: we moeten ook rekening houden met een foutief gebruik van de API,
met als doel om de toepassing (inclusief de database) te misbruiken.
Dit betekent dat we in de server de input vanuit de browser altijd moeten controleren.

**for...of**: denk om de `for..of` constructie in JavaScript 
(waar andere talen `for...in` gebruiken).

**jQuery**: het gebruik van AJAX in puur JavaScript is onhandig:
dit is een belangrijke reden om jQuery te gebruiken.

De volgende stappen
-------------------

* statische files
* templates
* gebruik van een database (SQLite)
* AJAX
* sessies
* app-factory
* headers
