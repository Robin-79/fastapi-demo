from typing import Sequence, Annotated
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from db import SessionDep
from models import Menu 

router = APIRouter()


@router.get("/menus")
async def get_menus(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[Menu]:
    menus = session.exec(select(Menu).offset(offset).limit(limit)).all()
    return menus

@router.post("/menus")
async def save_menu(cat: Menu, session: SessionDep) -> Menu:
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat

@router.get("/menus/{id}")
async def show_menu(id: int, session: SessionDep) -> Menu:
    menu = session.get(Menu, id)
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    return menu

@router.delete("/menus/{id}")
async def delete_menu(id: int, session: SessionDep):
    menu = session.get(Menu, id)
    if not menu:
        raise HTTPException(status_code=404, detail="Menu not found")
    session.delete(menu)
    session.commit()
    return {"ok": True}