import asyncio
from random import randint
from typing import AsyncIterable
import time
from req_http import http_get

# the highest pokemon ID
MAX_POKEMON = 898

async def get_random_pokemon_name() -> str:
    pokemon_id = randint(1, MAX_POKEMON)
    pokemon_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}"
    pokemon = await http_get(pokemon_url)
    return str(pokemon["name"])

async def next_pokemon(total: int) -> AsyncIterable[str]:
    for _ in range(total):
        name = await get_random_pokemon_name()
        yield name

async def main():
    # retrieve the next 10 pokemon names
    start = time.perf_counter()
    async for name in next_pokemon(10):
        print(name)
    end = time.perf_counter()
    print(f"Task 1 Duration: {round(end-start, 2)}")

    start = time.perf_counter()
    # asynchronous list comprehensions
    names = [name async for name in next_pokemon(10)]
    print(names)
    end = time.perf_counter()
    print(f"Task 2 Duration: {round(end-start, 2)}")

asyncio.run(main())