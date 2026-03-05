from app.repositories.pilot_repository import PilotRepository
from app.models.pilot import Pilot
from typing import List, Optional
from fastapi import HTTPException

class PilotService:
    def __init__(self, repository: PilotRepository):
        self.repository = repository

    def create_pilot(self, pilot: Pilot) -> Pilot:
        # Validación: license única
        existing = self.repository.get_all()
        if any(p.license == pilot.license for p in existing):
            raise HTTPException(status_code=400, detail="La licencia ya existe")
        return self.repository.create(pilot)

    def get_pilot(self, pilot_id: int) -> Pilot:
        pilot = self.repository.get_by_id(pilot_id)
        if not pilot:
            raise HTTPException(status_code=404, detail="Piloto no encontrado")
        return pilot

    def get_pilots(self) -> List[Pilot]:
        return self.repository.get_all()

    def update_pilot(self, pilot_id: int, updated_pilot: Pilot) -> Pilot:
        pilot = self.repository.get_by_id(pilot_id)
        if not pilot:
            raise HTTPException(status_code=404, detail="Piloto no encontrado")
        # Validación: license única si cambia
        if updated_pilot.license != pilot.license:
            existing = self.repository.get_all()
            if any(p.license == updated_pilot.license for p in existing):
                raise HTTPException(status_code=400, detail="La licencia ya existe")
        pilot.name = updated_pilot.name
        pilot.last_name = updated_pilot.last_name
        pilot.license = updated_pilot.license
        return self.repository.update(pilot)

    def delete_pilot(self, pilot_id: int) -> dict:
        if self.repository.delete(pilot_id):
            return {"status": "deleted"}
        raise HTTPException(status_code=404, detail="Piloto no encontrado")