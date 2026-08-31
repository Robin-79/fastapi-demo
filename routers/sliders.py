from typing import Sequence, Annotated
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from db import SessionDep
from models import Slider 

router = APIRouter()


@router.get("/sliders")
async def get_sliders(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[Slider]:
    sliders = session.exec(select(Slider).offset(offset).limit(limit)).all()
    return sliders

@router.post("/sliders")
async def save_slider(cat: Slider, session: SessionDep) -> Slider:
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat

@router.get("/sliders/{id}")
async def show_sliders(id: int, session: SessionDep) -> Slider:
    slider = session.get(Slider, id)
    if not slider:
        raise HTTPException(status_code=404, detail="Slider not found")
    return slider

@router.delete("/sliders/{id}")
async def delete_slider(id: int, session: SessionDep):
    slider = session.get(Slider, id)
    if not slider:
        raise HTTPException(status_code=404, detail="Slider not found")
    session.delete(slider)
    session.commit()
    return {"ok": True}