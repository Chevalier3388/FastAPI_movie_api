from typing import Optional

from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table
from sqlalchemy.orm import relationship
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY, JSON



class Model(DeclarativeBase):
    pass



class MovieOrm(Model):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    kinopoiskId: Mapped[int] = mapped_column(nullable=False)
    nameRu: Mapped[str] = mapped_column(String(200), nullable=False)
    ratingKinopoisk: Mapped[Optional[float]] = mapped_column(nullable=True)
    genres: Mapped[list[dict]] = mapped_column(JSON, nullable=False)


