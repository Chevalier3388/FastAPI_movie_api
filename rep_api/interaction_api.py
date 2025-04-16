import asyncio
from pprint import pprint

from httpx import AsyncClient
from config import settings


class RepApi:

    @classmethod
    async def get_movie_by_id(cls, id_movie:int):
        url = f"{settings.URL}30{id_movie}"
        headers = settings.headers

        async with AsyncClient() as client:
            response = await client.get(url, headers=headers)

        if response.status_code == 200:
            data = response.json()
            return data

        else:
            return {"Ошибка": f"{response.status_code}"}


    @classmethod
    async def get_movies(cls, quantity_films: int):
            tasks = [cls.get_movie_by_id(id) for id in range(1, 1 + quantity_films)]
            result = await asyncio.gather(*tasks)
            pprint(result)
            return result



