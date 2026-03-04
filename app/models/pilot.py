from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Pilot(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    last_name: str
    license: str
    
    flights: list["Flight"] = Relationship(back_populates="pilot")
