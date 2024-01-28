import asyncio
import os
import logging
import aiohttp


class FfxivApiComm:
    def __init__(self):
        # look for a key in the environment variables or pull from keyring.py
        if os.environ.get("ffxivapi_key"):
            self.api_key = os.environ.get("ffxivapi_key")
        else:
            try:
                import keyring
                self.api_key = keyring.keyring.ffxivapi_key
            except ImportError:
                print("No API key found. Please set the environment variable 'ffxivapi_key' to your API key.")
                exit()

    async def request(self, url: str, columns: list = None):
        headers = {
            'User-Agent': '&lt;User-Agent&gt;',
            'columns': ','.join(columns) if columns else None,
            'private_key': self.api_key
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, params=headers) as response:
                return await response.json()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format='%(message)s', datefmt='%H:%M')
    ffxivapicomm = FfxivApiComm()
    loop = asyncio.new_event_loop()
    data = loop.run_until_complete(ffxivapicomm.request(url='http://xivapi.com/Item/1675', columns=['Name']))
    print(data)
