from typing import Optional
from sqlmodel import SQLModel, Field

class Telemetric(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    max_height: float
    max_velocity: float
