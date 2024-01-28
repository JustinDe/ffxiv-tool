import asyncio
import os
import logging
import aiohttp
import pyxivapi
from pyxivapi.models import Filter, Sort

if os.environ.get("ffxivapi_key"):
    api_key = os.environ.get("ffxivapi_key")
else:
    try:
        import keyring
        api_key = keyring.keyring.ffxivapi_key
    except ImportError:
        print("No API key found. Please set the environment variable 'ffxivapi_key' to your API key.")
        exit()


async def fetch_example_results():
    client = pyxivapi.XIVAPIClient(api_key=api_key)

    # Search ingame data for matches against a given query. Includes item, minion, mount & achievement descriptions, quest dialog & more.
    lore = await client.lore_search(
        query="Summons",
        language="en"
    )

    print(lore)

    await client.session.close()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='%H:%M')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(fetch_example_results())
