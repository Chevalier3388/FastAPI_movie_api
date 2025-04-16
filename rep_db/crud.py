from sqlalchemy import select, update, insert
from rep_db.database import async_session
from schemas.schemas import MovieSchem
from rep_db.models import MovieOrm


class DataBaseRep:

    @classmethod
    async def add_film(cls, data: MovieSchem):
        """
        Добавляет данные о фильме в базу
        """
        async with async_session() as session:
            film = data.model_dump()
            query = (
                insert(MovieOrm)
                .values(film)
                .returning(MovieOrm)
            )

            result = await session.execute(query)
            new_film = result.scalar_one()
            await session.commit()
            return new_film

