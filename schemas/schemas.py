from typing import Optional, List

from pydantic import BaseModel, ConfigDict, Field



class MovieSchem(BaseModel):

    kinopoisk_id: int = Field(..., description="id фильма кинопоиске", alias="kinopoiskId")
    nameRu: str = Field(..., description="Название фильма")
    ratingKinopoisk: Optional[float] = Field(None, description="рейтинг фильма в кинопоиске")
    genres: list[dict] = Field(..., description="жанры фильма")


class MovieInDbSchem(MovieSchem):

    id: int = Field(..., description="id фильма в базе")

    model_config = ConfigDict(from_attributes=True)

