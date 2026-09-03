from typing import Sequence, Annotated
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select
from db import SessionDep
from models import Category

router = APIRouter()


@router.get("/categories")
async def get_categories(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[Category]:
    categories = session.exec(select(Category).offset(offset).limit(limit)).all()
    return categories

@router.post("/categories")
async def save_category(cat: Category, session: SessionDep) -> Category:
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat

@router.get("/categories/{slug}")
async def show_category(slug: str, session: SessionDep) -> Category:
    statement = select(Category).where(Category.slug == slug)
    result = session.exec(statement)
    category = result.first() # Returns None if not found
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.delete("/categories/{id}")
async def delete_category(id: int, session: SessionDep):
    category = session.get(Category, id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    session.delete(category)
    session.commit()
    return {"ok": True}