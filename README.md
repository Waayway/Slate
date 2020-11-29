# D&D Helper

## Usage

All Reponses will have the form;

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response dedinitions will only detail the expected value of the `data field`

### List all Characters

**Definition**

`GET /characters`

**Response**

- `200 OK` on success

```json
[
    {
        "name": "Character-Name",
        "Stats": {
            "Strength": 20,
            "Dexterity": 20,
            "Constitution": 20,
            "Wisdom": 20,
            "Intelligence": 9001,
            "Charisma": 0
        },
        "Not sure yet": ""
    }
]
```

### Registering a new Character

**Definition**

`POST /characters`

**Arguments**
- `"name":string` A global identifier for a character
- `"stats": dict` The stats of the char, if left empty all stats will be 0

- `201 Created` on success

```json
[
    {
        "name": "Character-Name",
        "identifier": some number,
        "Stats": {
            "Strength": 20,
            "Dexterity": 20,
            "Constitution": 20,
            "Wisdom": 20,
            "Intelligence": 9001,
            "Charisma": 0
        },
        "Not sure yet": ""
    }
]
```

## Lookup Character Details

`GET /character/<identifier>`

**Response**

- `404 Not Found` If the Character does not exist.
- `200 OK` on success

```json
[
    {
        "name": "Character-Name",
        "identifier": some number,
        "Stats": {
            "Strength": 20,
            "Dexterity": 20,
            "Constitution": 20,
            "Wisdom": 20,
            "Intelligence": 9001,
            "Charisma": 0
        },
        "Not sure yet": ""
    }
]
```

## Delete a device

**Definition**

`DELETE /character/<identifier>`

**Response**

- `404 Not Found` If the character does not exist
- `204 No Content` IF Succesful
