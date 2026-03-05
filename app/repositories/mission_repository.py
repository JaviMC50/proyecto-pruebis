from sqlmodel import Session, select
from app.models.mission import Mission
from typing import List, Optional

class MissionRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, mission: Mission) -> Mission:
        self.session.add(mission)
        self.session.commit()
        self.session.refresh(mission)
        return mission

    def get_by_id(self, mission_id: int) -> Optional[Mission]:
        return self.session.get(Mission, mission_id)

    def get_all(self) -> List[Mission]:
        return self.session.exec(select(Mission)).all()

    def update(self, mission: Mission) -> Mission:
        self.session.add(mission)
        self.session.commit()
        self.session.refresh(mission)
        return mission

    def delete(self, mission_id: int) -> bool:
        mission = self.get_by_id(mission_id)
        if mission:
            self.session.delete(mission)
            self.session.commit()
            return True
        return False