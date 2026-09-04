from datetime import datetime
from sqlmodel import SQLModel, Field

class Category(SQLModel, table=True):
    __tablename__ = "categories"

    id: int | None = Field(default=None, primary_key=True)
    title: str = Field()
    slug: str = Field()
    description: str = Field()


class Content(SQLModel, table=True):
    __tablename__ = "contents"

    id: int | None = Field(default=None, primary_key=True)
    title: str = Field()
    slug: str = Field()
    category_id: int = Field(foreign_key="categories.id")
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
    updated_at: datetime = Field()

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

class Review(SQLModel, table=True):
    __tablename__="reviews"

    id: int | None = Field(default=None, primary_key=True)
    anime_id: int = Field()
    user_id: int = Field()
    message: str = Field()
    rating: float = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    fullname: str = Field()
    email: str = Field()
    username: str = Field()
    phone: int = Field()
    password: str = Field()
    profile_image: str = Field()
    bio: str = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

class Menu(SQLModel, table=True):
    __tablename__ = "menus"

    id: int | None = Field(default=None, primary_key=True)
    title: str = Field()
    url: str = Field()

class Slider(SQLModel, table=True):
    __tablename__ = "sliders"

    id: int | None = Field(default=None, primary_key=True)
    image: str = Field()
    title: str = Field()
    details: str = Field()
    url: str = Field()
    button_label: str = Field()
