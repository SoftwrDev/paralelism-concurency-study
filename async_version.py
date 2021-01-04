from datetime import timedelta
import time
import asyncio
import aiohttp

async def main(max_range):
    async with aiohttp.ClientSession() as client:
        await asyncio.gather(*(get_google(client) for _ in range(max_range)))

def start_process(max_range=50):
    started_at = time.time()
    asyncio.run(main(max_range))
    elapsed_time = timedelta(seconds=time.time()-started_at)
    return f"Elapsed time with asyncio {elapsed_time}"

async def get_google(client):
    async with client.get("https://www.google.com.br") as response:
        assert response.status == 200
        return await response.read()
