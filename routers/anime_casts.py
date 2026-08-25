from typing import Sequence, Annotated
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from db import SessionDep
from models import AnimeCast

router = APIRouter()

@router.get("/anime_casts")
async def get_anime_casts(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[AnimeCast]:
    anime_casts = session.exec(select(AnimeCast).offset(offset).limit(limit)).all()
    return anime_casts

@router.post("/anime_casts")
async def save_anime_cast(cat: AnimeCast, session: SessionDep) -> AnimeCast:
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat

@router.get("/anime_casts/{id}")
async def show_anime_cast(id: int, session: SessionDep) -> AnimeCast:
    anime_cast = session.get(AnimeCast, id)
    if not anime_cast:
        raise HTTPException(status_code=404, detail="Hero not found")
    return anime_cast

@router.delete("/anime_casts/{id}")
async def delete_anime_cast(id: int, session: SessionDep):
    anime_cast = session.get(AnimeCast, id)
    if not anime_cast:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(anime_cast)
    session.commit()
    return {"ok": True}