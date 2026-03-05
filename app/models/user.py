from typing import Optional
from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    """Modelo de usuario para base de datos."""

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(min_length=1, max_length=100)
    username: str = Field(unique=False, min_length=3, max_length=50)