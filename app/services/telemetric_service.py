from app.repositories.telemetric_repository import TelemetricRepository
from app.models.telemetric import Telemetric
from typing import List, Optional
from fastapi import HTTPException

class TelemetricService:
    def __init__(self, repository: TelemetricRepository):
        self.repository = repository

    def create_telemetric(self, telemetric: Telemetric) -> Telemetric:
        # Validación: valores positivos
        if telemetric.max_height <= 0 or telemetric.max_velocity <= 0:
            raise HTTPException(status_code=400, detail="La altura máxima y la velocidad máxima deben ser positivas")
        return self.repository.create(telemetric)

    def get_telemetric(self, telemetric_id: int) -> Telemetric:
        telemetric = self.repository.get_by_id(telemetric_id)
        if not telemetric:
            raise HTTPException(status_code=404, detail="Telemetría no encontrada")
        return telemetric

    def get_telemetrics(self) -> List[Telemetric]:
        return self.repository.get_all()

    def update_telemetric(self, telemetric_id: int, updated_telemetric: Telemetric) -> Telemetric:
        telemetric = self.repository.get_by_id(telemetric_id)
        if not telemetric:
            raise HTTPException(status_code=404, detail="Telemetría no encontrada")
        # Validación
        if updated_telemetric.max_height <= 0 or updated_telemetric.max_velocity <= 0:
            raise HTTPException(status_code=400, detail="La altura máxima y la velocidad máxima deben ser positivas")
        telemetric.max_height = updated_telemetric.max_height
        telemetric.max_velocity = updated_telemetric.max_velocity
        return self.repository.update(telemetric)

    def delete_telemetric(self, telemetric_id: int) -> dict:
        if self.repository.delete(telemetric_id):
            return {"status": "deleted"}
        raise HTTPException(status_code=404, detail="Telemetría no encontrada")