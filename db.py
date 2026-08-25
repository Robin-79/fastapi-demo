from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "mysql+pymysql://root:@localhost:3306/aksaria"

engine = create_engine(DATABASE_URL)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]