from sqlmodel import Session, select
from app.models.aircraft import Aircraft
from typing import List, Optional

class AircraftRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, aircraft: Aircraft) -> Aircraft:
        self.session.add(aircraft)
        self.session.commit()
        self.session.refresh(aircraft)
        return aircraft

    def get_by_id(self, aircraft_id: int) -> Optional[Aircraft]:
        return self.session.get(Aircraft, aircraft_id)

    def get_all(self) -> List[Aircraft]:
        return self.session.exec(select(Aircraft)).all()

    def update(self, aircraft: Aircraft) -> Aircraft:
        self.session.add(aircraft)
        self.session.commit()
        self.session.refresh(aircraft)
        return aircraft

    def delete(self, aircraft_id: int) -> bool:
        aircraft = self.get_by_id(aircraft_id)
        if aircraft:
            self.session.delete(aircraft)
            self.session.commit()
            return True
        return False