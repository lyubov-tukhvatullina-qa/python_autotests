import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'указать токен'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "покемон",
    "photo_id": 19
}

body_change = {
    "pokemon_id": "377078",
    "name": "покемончик",
    "photo_id": 19
}

body_pokeball = {
    "pokemon_id": "377078"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response.text)

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)