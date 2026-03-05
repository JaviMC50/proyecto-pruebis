from sqlmodel import Session, select
from app.models.telemetric import Telemetric
from typing import List, Optional

class TelemetricRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, telemetric: Telemetric) -> Telemetric:
        self.session.add(telemetric)
        self.session.commit()
        self.session.refresh(telemetric)
        return telemetric

    def get_by_id(self, telemetric_id: int) -> Optional[Telemetric]:
        return self.session.get(Telemetric, telemetric_id)

    def get_all(self) -> List[Telemetric]:
        return self.session.exec(select(Telemetric)).all()

    def update(self, telemetric: Telemetric) -> Telemetric:
        self.session.add(telemetric)
        self.session.commit()
        self.session.refresh(telemetric)
        return telemetric

    def delete(self, telemetric_id: int) -> bool:
        telemetric = self.get_by_id(telemetric_id)
        if telemetric:
            self.session.delete(telemetric)
            self.session.commit()
            return True
        return False