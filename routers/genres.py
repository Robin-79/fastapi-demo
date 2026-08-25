from typing import Sequence, Annotated
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from db import SessionDep
from models import Genre

router = APIRouter()


@router.get("/genres")
async def get_genres(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[Genre]:
    genres = session.exec(select(Genre).offset(offset).limit(limit)).all()
    return genres

@router.post("/genres")
async def save_genre(cat: Genre, session: SessionDep) -> Genre:
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat

@router.get("/genres/{id}")
async def show_genre(id: int, session: SessionDep) -> Genre:
    genre = session.get(Genre, id)
    if not genre:
        raise HTTPException(status_code=404, detail="Hero not found")
    return genre

@router.delete("/genres/{id}")
async def delete_genre(id: int, session: SessionDep):
    genre = session.get(Genre, id)
    if not genre:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(genre)
    session.commit()
    return {"ok": True}