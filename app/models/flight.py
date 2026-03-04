from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class Flight(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    pilot_id: int = Field(foreign_key="pilot.id")
    aircraft_id: int = Field(foreign_key="aircraft.id")
    telemetry_id: int = Field(foreign_key="telemetric.id")
    start_date: datetime
    end_date: datetime
    
    pilot: Optional["Pilot"] = Relationship(back_populates="flights")
    aircraft: Optional["Aircraft"] = Relationship(back_populates="flights")
    telemetry: Optional["Telemetric"] = Relationship(back_populates="flights")
