from app.repositories.mission_repository import MissionRepository
from app.models.mission import Mission
from typing import List, Optional
from fastapi import HTTPException

class MissionService:
    def __init__(self, repository: MissionRepository):
        self.repository = repository

    def create_mission(self, mission: Mission) -> Mission:
        # Validación: start_date < end_date
        if mission.start_date >= mission.end_date:
            raise HTTPException(status_code=400, detail="La fecha de inicio debe ser anterior a la fecha de finalización")
        return self.repository.create(mission)

    def get_mission(self, mission_id: int) -> Mission:
        mission = self.repository.get_by_id(mission_id)
        if not mission:
            raise HTTPException(status_code=404, detail="Misión no encontrada")
        return mission

    def get_missions(self) -> List[Mission]:
        return self.repository.get_all()

    def update_mission(self, mission_id: int, updated_mission: Mission) -> Mission:
        mission = self.repository.get_by_id(mission_id)
        if not mission:
            raise HTTPException(status_code=404, detail="Misión no encontrada")
        # Validación
        if updated_mission.start_date >= updated_mission.end_date:
            raise HTTPException(status_code=400, detail="La fecha de inicio debe ser anterior a la fecha de finalización")
        mission.name = updated_mission.name
        mission.description = updated_mission.description
        mission.start_date = updated_mission.start_date
        mission.end_date = updated_mission.end_date
        return self.repository.update(mission)

    def delete_mission(self, mission_id: int) -> dict:
        if self.repository.delete(mission_id):
            return {"status": "deleted"}
        raise HTTPException(status_code=404, detail="Misión no encontrada")