Welkom bij de cursus Python apps met Flask
==============================================

Klik `"Show"` bovenin om de app "live" te bekijken.
Aanpassingen in je code worden direct verwerkt:
je ziet dit direct in de app.

Glitch (zie [Over Glitch](https://glitch.com/about)) is een omgeving ("zandbak", "speeltuin") voor ontwikkelaars waarin je een echte web-app kunt maken met direct resultaat.

We gaan ervan uit dat je de volgende voorkennis hebt:

- enige kennis van programmeren en van Python
- kennis van html, css en javascript ("front end")
- enige kennis van databases (SQL)

Over dit voorbeeld
------------------

Dit voorbeeld geeft de minimale opzet voor een website met Python en Flask.
We gebruiken Python als scriptingtaal voor de website.
Flask is een *framework* voor het maken van websites met Python.
We zullen in de volgende lessen met een aantal aspecten van Flask kennismaken.
We gaan ervan uit dat je enige kennis van programmeren en van Python hebt.

- het hoofdprogramma van de app is `server.py`
- de Python-packages en frameworks die de app gebruikt staan in `requirements.txt`
- de front-end bestanden (html, css, javascript) voor de app staan in de mappen `public` en `views`.

In dit voorbeeld demonstreert twee aspecten van Flask:

1. de minimale *boiler plate*: de import-statements,
2. de *routering*

Voor een Flask-app heb je het Flask-framework nodig.
Hiermee maak je een `app`-object voor de applicatie:

```Python
from flask import Flask

app = Flask(__name__)
```

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

1. Verander de tekst die de functie `hello` oplevert, en controleer het resultaat in de "live" app.
2. 

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
