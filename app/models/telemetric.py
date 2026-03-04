from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Telemetric(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    max_height: float
    max_velocity: float
    
    flights: list["Flight"] = Relationship(back_populates="telemetry")
