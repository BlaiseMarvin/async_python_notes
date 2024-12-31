import asyncio
from random import randint

from req_http import JSONObject, http_get

# the highest pokemon ID
MAX_POKEMON = 898

async def get_pokemon(pokemon_id: int) -> JSONObject:
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    return await http_get(pokemon_url)

async def main()