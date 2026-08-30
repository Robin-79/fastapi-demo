from typing import Sequence, Annotated
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from db import SessionDep
from models import User

router = APIRouter()


@router.get("/users")
async def get_users(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[User]:
    users = session.exec(select(User).offset(offset).limit(limit)).all()
    return users

@router.post("/users")
async def save_user(cat: User, session: SessionDep) -> User:
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat

@router.get("/users/{id}")
async def show_users(id: int, session: SessionDep) -> User:
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="Hero not found")
    return user

@router.delete("/users/{id}")
async def delete_users(id: int, session: SessionDep):
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(user)
    session.commit()
    return {"ok": True}