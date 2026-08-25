from datetime import datetime
from sqlmodel import SQLModel, Field

class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: int | None = Field(default=None, primary_key=True)
    title: str = Field()
    slug: str = Field()
    description: str = Field()


class Anime(SQLModel, table=True):
    __tablename__ = "anime"

    id: int | None = Field(default=None, primary_key=True)
    title: str = Field()
    slug: str = Field()
    description: str = Field()
    poster_image: str = Field()
    release_date: datetime = Field()
    total_episodes: int = Field()
    runtime: float = Field()
    budget: float = Field()
    language: str = Field()
    country: str = Field()
    director: str = Field()
    created_at: datetime = Field()
    update_at: datetime = Field()

class AnimeCast(SQLModel, table=True):
    __tablename__ = "anime_casts"

    id: int | None = Field(default=None, primary_key=True)
    anime_id: int = Field()
    cast_name: str = Field()
    gender: str = Field()
    photo: str = Field()
    character_name: str = Field()
    description: str = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

class Genre(SQLModel, table=True):
    __tablename__ = "genres"

    id: int | None = Field(default=None, primary_key=True)
    title: str = Field()
    slug: str = Field()
    description: str = Field()
    created_at: datetime = Field()
    update_at: datetime = Field()