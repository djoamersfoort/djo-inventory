REST Api voor inventarisatie van DJO/Bitlair onderdelen.

Elke call heeft altijd een "result" veld en bevat "ok" = ok, of de foutmelding.

# Installatie howto
Om te testen / ontwikkelen:

- pip3 install -r requirements.txt
- cp inventory/settings.py.example inventory/settings.py
- aanpassen settings.py naar wens
  (voor nu alleen SECRET_KEY invullen/aanpassen en evt. DATABASE als je geen sqlite wilt)
- ./migrate.py migrate (maakt sqlite database aan)
- ./migrate.py createsuperuser  (maak de 1e admin account aan)
- ./migrate.py runserver

Nu draait er een debug servertje op localhost:8000 waartegen je kunt testen.
ga naar http://localhost:8000/admin/ om users en items/locaties te beheren

# CALLS

## GET /api/v1/items:
input: none

Geeft de complete lijst met items terug

output:
```json
{
 "result": "ok",
 "items": [
     {
        "id": "<id van het item>",
        "name": "<Naam van het item>",
        "description": "<Omschrijving van het item>",
        "location": "Locatie van het item (naam)",
        "location_id": "Locatie id van het item",
        "url": "<URL naar beschrijving / spec / docu van dit item"
     },
     {
        "id": "<id van volgend item>",
        "name": "<Naam van het 2e item>",
        enz. enz...
     }
   ]
}
```

curl example:
```
curl http://localhost:8000/api/v1/items
```


## GET /api/v1/item/\<id\>
input: none

Haal de details van 1 item op.

output:
```json
{
  "result": "ok",
  "item": {
     "id": "<id>",
     "name": "<Naam van het item>",
     "description": "<Omschrijving van het item>",
     "location": "Locatie van het item (naam)",
     "location_description": "Omschrijving van de locatie van het item",
     "location_id": "Locatie id van het item",
     "url": "<URL naar beschrijving / spec / docu van dit item",
     "properties": ["Transistor", "NPN", "<Andere properties van dit item>"]
  }
}
```


## GET /api/v1/items/search/\<keyword\>
input: none

Zoek naar items in de database en geef alle matches terug.
De velden naam en omschrijving worden gematched (geen regex)

output:
```json
{
 "result": "ok",
 "items": [
     {
        "id": "<id van het item>",
        "name": "<Naam van het item>",
        "description": "<Omschrijving van het item>",
        "location": "Locatie van het item (naam)",
        "location_description": "Omschrijving van de locatie van het item",
        "location_id": "Locatie id van het item",
        "url": "<URL naar beschrijving / spec / docu van dit item"
     },
     {
        "id": "<id van het 2e item>",
        "name": "<Naam van het 2e item>",
        enz. enz...
     }
   ]
}
```


## GET api/v1/location/\<int:location_id\>

Haal de details van een locatie op, inclusief een base64 encoded foto
(kan je direct in een img src="<base64 troep>" gooien)

output:
```json
{
 "result": "ok",
 "location": {
   "id": "<locatie id>",
   "name": "<Locatie naam",
   "description": "Omschrijving van de locatie",
   "photo": "<base64 encoded foto van de locatie"
  }
}
```

## GET api/v1/location/\<int:location_id\>/photo

Geef direct een 'image' terug (content-type: image/png). Deze url kun je
gebruiken in een \<img\ src=''> tag.

output:
image/png
