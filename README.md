Cursus Python apps met Flask: MongoDB database(3)
================================================

We gebruiken hier de MongoDB database samen met een AJAX-interactie tussen browser en server.

In de vorige stap hebben we het opvragen van alle todo's geïmplementeerd.
In deze stap maken we een nieuwe todo aan.

In het HTML-document introduceren we hiervoor een eenvoudig "formulier",
met een aantal invulvelden. 
(In eerste instantie alleen de naam/beschrijving van de todo.)
We gebruiken het nummer van de todo als key: de gebruiker kan deze niet zelf invullen.


In deze eerste stap veranderen we de server-side rendering van de todo-lijst,
in een client-side rendering.
Met behulp van een JavaScript-functie in een AJAX-interactie vraagt de app de lijst met todo's op van de server.
De server levert de lijst met todo's op in het JSON-formaat.
In de browser wordt dit JSON-formaat omgezet in een JavaScript-object;
daarmee wordt de HTML-tekst aangepast (via DOM-operaties).

In de server verschuift het opzoeken van de todo's van de `home (/)`-functie naar de `get_todos (/todos)`-functie.
De iteratie over alle todo-elementen verschuift van het template (server-side) naar de JavaScript-functie (client-side).

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

**template-caching**: als de html-code niet verandert in de app, 
terwijl je het bestand wel veranderd hebt, dan kun je last hebben van de Python template-caching.
Deze is bedoeld om de server sneller te laten werken,
maar kan je dwars zitten bij veranderingen in de template-tekst.
Je kunt dit omzeilen door in het gebruik van een template de bestandsnaam tijdelijk te veranderen,
en dan weer terug te veranderen.
Bijvoorbeeld: verander `render_template('app.html', ...)` in `render_template('app1.html', ...)` en terug.

**key's (id)**: wat gebruiken we als key voor de todo-documenten?
We kunnen de ingebouwde `ObjectId`-key gebruiken, 
maar deze (i) heeft in het interface met de gebruiker geen betekenis;
en (ii) levert problemen op als onderdeel van een JSON-object.
Voor dat laatste moeten we dan zowel de conversie naar als van JSON-formaat aanpassen. 

Zie ook:

* https://stackoverflow.com/questions/16586180/typeerror-objectid-is-not-json-serializable (voor de Python/server side)
* (en hoe voor de client-side? gewoon als string?)

NB: aan de client-side heb je de keys niet nodig, je hoef alleen maar dezelfde waarden weer terug te geven bij een volgende AJAX-operatie.
De JSON-string-representatie moet de omzetting naar JavaScript en weer terug naar JSON (en BSON) overleven.

**BSON** bevat meer speciale waarden die niet in JSON voorkomen,
in het bijzonder ook Datum/Tijd-waarden. 
Deze wil je mogelijk in JavaScript wel kunnen gebruiken.

De volgende stappen
-------------------

* statische files
* templates
* gebruik van een database (SQLite)
* AJAX
* sessies
* app-factory
* headers
