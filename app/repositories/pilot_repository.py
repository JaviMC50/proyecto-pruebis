from sqlmodel import Session, select
from app.models.pilot import Pilot
from typing import List, Optional

class PilotRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, pilot: Pilot) -> Pilot:
        self.session.add(pilot)
        self.session.commit()
        self.session.refresh(pilot)
        return pilot

    def get_by_id(self, pilot_id: int) -> Optional[Pilot]:
        return self.session.get(Pilot, pilot_id)

    def get_all(self) -> List[Pilot]:
        return self.session.exec(select(Pilot)).all()

    def update(self, pilot: Pilot) -> Pilot:
        self.session.add(pilot)
        self.session.commit()
        self.session.refresh(pilot)
        return pilot

    def delete(self, pilot_id: int) -> bool:
        pilot = self.get_by_id(pilot_id)
        if pilot:
            self.session.delete(pilot)
            self.session.commit()
            return True
        return False