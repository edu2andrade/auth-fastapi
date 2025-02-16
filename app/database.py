import os
from dotenv import load_dotenv
from typing import Annotated
from sqlalchemy import engine
from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

def drop_db_and_tables():
    SQLModel.metadata.drop_all(engine)

SessionDep = Annotated[Session, Depends(get_session)]