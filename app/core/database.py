from sqlmodel import create_engine, SQLModel

DATABASE_URL = "postgresql://admin:5467@db:5432/proyecto-pruebas"

engine = create_engine(DATABASE_URL, echo=True)