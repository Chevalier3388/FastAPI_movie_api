import asyncio

from fastapi import APIRouter, HTTPException
from rep_api.interaction_api import RepApi
from rep_db.crud import DataBaseRep
from schemas.schemas import MovieSchem

router_get = APIRouter(
    prefix="/movie",
    tags=["Фильмы"],
    )


@router_get.get(
    "/movies/{quantity_films}",
    summary="Получить несколько фильмов",
    description="Отправляет запрос на сторонний API, что бы получить данные о нескольких фильмах"
)
async def get_movies(quantity_films: int):
    responses = await RepApi.get_movies(quantity_films)
    tasks = []
    if not responses:
        raise HTTPException(status_code=404, detail=f"Что-то поломалось")
    for response in responses:
        if response:
            film_data = MovieSchem(kinopoiskId=response["kinopoiskId"],
                                   nameRu=response["nameRu"] or "Без названия",
                                   ratingKinopoisk=response["ratingKinopoisk"],
                                   genres=response.get("genres", []))
            tasks.append(DataBaseRep.add_film(film_data))
    await asyncio.gather(*tasks)

    return {"message": f"Добавлено {len(tasks)}",
            "response": responses}

@router_get.get(
    "/{id_movie}",
    summary="Получить новую киношку",
    description="Отправляет запрос на сторонний API, что бы получить данные о киношке"
)
async def get_movie(id_movie: int):
    response = await RepApi.get_movie_by_id(id_movie)
    if not response:
        raise HTTPException(status_code=404, detail=f"Что-то поломалось и мы не смогли найти фильм с id: {id_movie}")

    film_data = MovieSchem(kinopoiskId=response["kinopoiskId"],
    nameRu=response["nameRu"] or "Без названия",
    ratingKinopoisk=response["ratingKinopoisk"],
    genres=response.get("genres", []))

    await DataBaseRep.add_film(film_data)

    return response

