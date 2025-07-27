import asyncio
import aiohttp

servidor = f"http://nginx/productos/"
peticiones_simultaneas = 2000
num_peticion = 0


async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            global num_peticion
            num_peticion += 1
            print(f"Petición número: {num_peticion}")
            print(f"Respuesta: {await response.read()}")
            return await response.read()


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(peticiones_simultaneas):
            tasks.append(fetch_data(servidor))
        await asyncio.gather(*tasks)


asyncio.run(main())
