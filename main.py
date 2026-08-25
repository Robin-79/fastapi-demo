from fastapi import FastAPI

from db import create_db_and_tables
from routers import categories, animes, genres, anime_casts

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(categories.router)
app.include_router(animes.router)
app.include_router(genres.router)
app.include_router(anime_casts.router)