from sqlmodel import Session, select
from app.models.flight import Flight
from typing import List, Optional

class FlightRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, flight: Flight) -> Flight:
        self.session.add(flight)
        self.session.commit()
        self.session.refresh(flight)
        return flight

    def get_by_id(self, flight_id: int) -> Optional[Flight]:
        return self.session.get(Flight, flight_id)

    def get_all(self) -> List[Flight]:
        return self.session.exec(select(Flight)).all()

    def update(self, flight: Flight) -> Flight:
        self.session.add(flight)
        self.session.commit()
        self.session.refresh(flight)
        return flight

    def delete(self, flight_id: int) -> bool:
        flight = self.get_by_id(flight_id)
        if flight:
            self.session.delete(flight)
            self.session.commit()
            return True
        return False