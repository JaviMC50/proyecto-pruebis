from sqlmodel import create_engine, SQLModel, Session
from typing import Generator

DATABASE_URL = "postgresql://postgres:postgres@db:5432/app"

engine = create_engine(DATABASE_URL, echo=True)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session