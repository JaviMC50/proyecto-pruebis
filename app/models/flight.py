from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Flight(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    pilot: str
    aircraft: str
    telemetry: str
    start_date: datetime
    end_date: datetime
