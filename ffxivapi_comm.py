import keyring
import asyncio
import logging

import aiohttp
import pyxivapi
from pyxivapi.models import Filter, Sort


async def fetch_example_results():
    client = pyxivapi.XIVAPIClient(api_key=keyring.keyring.ffxivapi_key)

    # Search Lodestone for a character
    character = await client.character_search(
        world="odin", 
        forename="lethys", 
        surname="lightpaw"
    )

print(Keyring.keyring.ffxivapi_key)