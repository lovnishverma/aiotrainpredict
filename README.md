Cursus Python apps met Flask: templates
=======================================

Bij een dynamische website past de server de inhoud van de webpagina's aan op grond van de toestand van de server.
Een uitgebreide toestand houd je meestal bij in een database.



In dit voorbeeld maken we een statische website:
de webserver levert de bestanden op die in de `public` map staan,
waarbij de URL overeenkomt met het pad van het bestand.
Dit kunnen html, css en javascript-bestanden zijn.

**Opdrachten**

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
