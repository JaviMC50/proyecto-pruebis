from app.repositories.aircraft_repository import AircraftRepository
from app.models.aircraft import Aircraft
from typing import List, Optional
from fastapi import HTTPException

class AircraftService:
    def __init__(self, repository: AircraftRepository):
        self.repository = repository

    def create_aircraft(self, aircraft: Aircraft) -> Aircraft:
        # Validación: serial_number único
        existing = self.repository.get_all()
        if any(a.serial_number == aircraft.serial_number for a in existing):
            raise HTTPException(status_code=400, detail="El número de serie ya existe")
        return self.repository.create(aircraft)

    def get_aircraft(self, aircraft_id: int) -> Aircraft:
        aircraft = self.repository.get_by_id(aircraft_id)
        if not aircraft:
            raise HTTPException(status_code=404, detail="Aeronave no encontrada")
        return aircraft

    def get_aircrafts(self) -> List[Aircraft]:
        return self.repository.get_all()

    def update_aircraft(self, aircraft_id: int, updated_aircraft: Aircraft) -> Aircraft:
        aircraft = self.repository.get_by_id(aircraft_id)
        if not aircraft:
            raise HTTPException(status_code=404, detail="Aeronave no encontrada")
        # Validación
        if updated_aircraft.serial_number != aircraft.serial_number:
            existing = self.repository.get_all()
            if any(a.serial_number == updated_aircraft.serial_number for a in existing):
                raise HTTPException(status_code=400, detail="El número de serie ya existe")
        aircraft.producer = updated_aircraft.producer
        aircraft.model = updated_aircraft.model
        aircraft.serial_number = updated_aircraft.serial_number
        aircraft.max_velocity = updated_aircraft.max_velocity
        return self.repository.update(aircraft)

    def delete_aircraft(self, aircraft_id: int) -> dict:
        if self.repository.delete(aircraft_id):
            return {"status": "deleted"}
        raise HTTPException(status_code=404, detail="Aeronave no encontrada")