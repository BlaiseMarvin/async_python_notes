import asyncio
import requests

# a few handy JSON types
JSON = int | str | float | bool | None | dict[str, "JSON"] | list["JSON"]
JSONObject = dict[str, JSON]

def http_get_sync(url:str) -> JSONObject:
    response = requests.get(url)
    return response.json()

async def http_get(url: str) -> JSONObject:
    return await asyncio.to_thread(http_get_sync, url)
