from typing import Sequence, Annotated
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select

from db import SessionDep
from models import Review

router = APIRouter()

@router.get("/reviews")
async def get_reviews(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[Review]:
    reviews = session.exec(select(Review).offset(offset).limit(limit)).all()
    return reviews

@router.post("/reviews/")
async def save_review(cat: Review, session: SessionDep) -> Review:
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat

@router.get("/reviews/{id}")
async def show_review(id: int, session: SessionDep) -> Review:
    review = session.get(Review, id)
    if not review:
        raise HTTPException(status_code=404, detail="Hero not found")
    return review

@router.delete("/reviews/{id}")
async def delete_review(id: int, session: SessionDep):
    review = session.get(Review, id)
    if not review:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete()
    session.commit()
    return {"ok": True}