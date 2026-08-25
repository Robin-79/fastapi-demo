from typing import Sequence, Annotated
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select
from db import SessionDep
from models import Anime

router = APIRouter()

@router.get("/animes")
async def get_animes(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[Anime]:
    animes = session.exec(select(Anime).offset(offset).limit(limit)).all()
    return animes

@router.post("/animes")
async def saveAnime(cat: Anime, session: SessionDep) -> Anime:
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat

@router.get("/animes/{id}")
async def showAnime(id: int, session: SessionDep) -> Anime:
    anime = session.get(Anime, id)
    if not anime:
        raise HTTPException(status_code=404, detail="Hero not found")
    return anime

@router.delete("/animes/{id}")
async def deleteAnime(id: int, session: SessionDep):
    anime = session.get(Anime, id)
    if not anime:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(anime)
    session.commit()
    return {"ok": True}