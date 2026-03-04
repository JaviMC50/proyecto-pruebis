from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Aircraft(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    producer: str
    model: str
    serial_number: str
    max_velocity: float
    
    flights: list["Flight"] = Relationship(back_populates="aircraft")
