Cursus Python apps met Flask: templates
=======================================

Bij een dynamische website past de server de webpagina's aan op grond van de toestand van de server.
Voor deze toestand gebruik je meestal een database:
daar gaan we later verder op in.

De waarden die je uit de toestand krijgt, moet je verwerken in de webpagina (html-code).
Hiervoor gebruik je *templates*.

In dit eenvoudige voorbeeld hangt de webpagina af van een *omgevings-variabele*:
in het template vullen we voor `naam`de waarde van `os.environment("MADE_BY")` in.

Over templates
--------------

Een *template* (sjabloon) is een tekst (string) waarin elementen opengelaten zijn om deze later in te vullen.
Het invullen van deze opengelaten elementen noemen we *rendering*.

De opengelaten elementen noteren we in de *template-taal* die bij deze rendering gebruikt wordt.
De template-taal van Flask is [Jinja-2](http://jinja.pocoo.org).

In het template geef je een opengelaten element (variabele) aan met `{{ maker }}`:
een naam tussen `{{ }}`-haken.

```html
    <h1>Welkom bij {{ maker }}'s app</h1>
```

Bij de rendering geeft je dan een stringwaarde om in te vullen voor deze variabele: 

```python
   render_template("app.html", maker="Hans")
```

Naast deze eenvoudige template-variabelen zijn er nog meer constructies,
die we in het geval van Jinja-2 aangeven met `{% %}`-haken.
In volgende voorbeelden geven we daarvan meer voorbeelden.

Templates zijn in veel situaties handig.
Jinja-2 en andere template-talen kun je ook in andere toepassingen dan webservers of html goed gebruiken.
Maar voor een webserver gebruik je wel bijna altijd een template-taal.
(PHP is van oorsprong een template-taal die uitgegroeid is tot een complete programmeertaal.)




**Opdrachten**

1. voeg aan de functie `hello` een opdracht toe om de waarde van
   `os.environ.get("MADE_BY")` af te drukken.
   Het resultaat van een print-opdracht vind je terug in de Log:
   deze krijg je te zien door te klikken op "Logs" in de linker-zijbalk.
2. 

Over dit voorbeeld
------------------

**App-structuur**

De app-structuur is in dit geval iets uitgebreider:
we geven aan `Flask` de naam van de map met de statische bestanden mee.

```Python
from flask import Flask, render_template


app = Flask(__name__, static_folder='public', template_folder='views')
...
if __name__ == '__main__':
    app.run()
```

**Routering** 
Een URL `/naam` van de app worden verwerkt door een functie van de vorm:

```Python
@app.route('/naam', methods=['GET', 'POST'])
def naam():
    return ...
```

De naam van de functie mag je vrij kiezen; 
vaak gebruiken we daarvoor de naam in de URL.
Als `methods=['GET']`, kun je dit weglaten (*default*)

De Python-constructie `@app.route(url) def naam(...) ...` heet een *decorator* voor de functie `naam`.
In andere talen gebruik je hier vaak de constructie:

```
route(url, function naam (...) {...})
```
In beide gevallen betekent dit: bind de functie `naam` aan de url `url`,
zodat deze functie aangeroepen wordt als we een *request* voor `url` krijgen.


**Opdrachten**

1. Verander (in `server.py`) de tekst die de functie `hello` oplevert, 
   en controleer het resultaat in de "live" app.
2. Voeg een tweede functie toe, op dezelfde manier als `hello`, voor de url `/hi`. 
   Test deze via de live app.
   
**Opmerking** Als je niet de meest recente versie in de browser te zien krijgt,
kan het zijn dat dit ligt aan de browser: de Glitch-server levert altijd de nieuwste versie.

- in Safari: Ontwikkel/Leeg caches (Alt-Cmd-E)

Aan de serverkant kan er ook sprake zijn van een oudere versie,
als je één van de statische bestanden aanpast.
In dat geval helpt een "kleine aanpassing" van `server.py`,
bijvoorbeeld het toevoegen en verwijderen van een spatie.

Over de Glitch omgeving
-----------------------

- `.gitconfig`
- `.env` - map waarin je niet-publieke gegevens ("secrets") van de app kunt opslaan. Dit is een shell-bestand waarin je environment-variabelen kunt zetten die je in je Python-programma's kunt gebruiken.
- in de map `assets` kun je plaatjes, muziek e.d. voor de app plaatsen.

De volgende stappen
-------------------

* statische files
* templates
* gebruik van een database (SQLite)
* sessies
* app-factory
* headers
