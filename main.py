from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import create_db_and_tables
from routers import categories, animes, genres, anime_casts, menus, users, reviews

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
app.include_router(reviews.router)
app.include_router(users.router)
app.include_router(menus.router)
