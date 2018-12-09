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
 "items": {
     "1": {
        "name": "<Naam van het item>",
        "description": "<Omschrijving van het item>",
        "location": "Locatie van het item (naam)",
        "location_id": "Locatie id van het item",
        "url": "<URL naar beschrijving / spec / docu van dit item"
     },
     "2": {
        "name": "<Naam van het 2e item>",
        enz. enz...
     }
   }
}
```

curl example:
```
curl http://localhost:8000/api/v1/items
```


## GET /api/v1/item/\<id\>
input: none

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
     "url": "<URL naar beschrijving / spec / docu van dit item"
  }
}
```


api/v1/items/search/<str:keyword>

## GET /api/v1/items/search/\<keyword\>
input: none

output:
```json
{
 "result": "ok",
 "items": {
     "1": {
        "name": "<Naam van het item>",
        "description": "<Omschrijving van het item>",
        "location": "Locatie van het item (naam)",
        "location_description": "Omschrijving van de locatie van het item",
        "location_id": "Locatie id van het item",
        "url": "<URL naar beschrijving / spec / docu van dit item"
     },
     "2": {
        "name": "<Naam van het 2e item>",
        enz. enz...
     }
   }
}
```
