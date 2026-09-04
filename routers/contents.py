from typing import Sequence, Annotated
from fastapi import APIRouter, HTTPException, Query
from sqlmodel import select
from db import SessionDep
from models import Content

router = APIRouter()

@router.get("/contents")
async def get_contents(
        session: SessionDep,
        offset: int = 0,
        limit: Annotated[int, Query(le=100)] = 100,
        category_id: int | None = None
) -> Sequence[Content]:
    stmt = select(Content).where(Content.category_id == category_id).offset(offset).limit(limit)
    contents = session.exec(stmt).all()
    return contents
    

@router.get("/contents/{slug}")
async def showContent(slug: str, session: SessionDep) -> Content:
    statement = select(Content).where(Content.slug == slug)
    result = session.exec(statement)
    content = result.first()
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content


@router.post("/contents")
async def saveContent(cat: Content, session: SessionDep) -> Content:
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat

@router.get("/contents/{id}")
async def showContent(id: int, session: SessionDep) -> Content:
    content = session.get(Content, id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    return content

@router.delete("/contents/{id}")
async def deleteContent(id: int, session: SessionDep):
    content = session.get(Content, id)
    if not content:
        raise HTTPException(status_code=404, detail="Content not found")
    session.delete(content)
    session.commit()
    return {"ok": True}