from app.repositories.flight_repository import FlightRepository
from app.models.flight import Flight
from typing import List, Optional
from fastapi import HTTPException

class FlightService:
    def __init__(self, repository: FlightRepository):
        self.repository = repository

    def create_flight(self, flight: Flight) -> Flight:
        # Validación: start_date < end_date
        if flight.start_date >= flight.end_date:
            raise HTTPException(status_code=400, detail="La fecha de inicio debe ser anterior a la fecha de finalización")
        return self.repository.create(flight)

    def get_flight(self, flight_id: int) -> Flight:
        flight = self.repository.get_by_id(flight_id)
        if not flight:
            raise HTTPException(status_code=404, detail="Vuelo no encontrado")
        return flight

    def get_flights(self) -> List[Flight]:
        return self.repository.get_all()

    def update_flight(self, flight_id: int, updated_flight: Flight) -> Flight:
        flight = self.repository.get_by_id(flight_id)
        if not flight:
            raise HTTPException(status_code=404, detail="Vuelo no encontrado")
        # Validación
        if updated_flight.start_date >= updated_flight.end_date:
            raise HTTPException(status_code=400, detail="La fecha de inicio debe ser anterior a la fecha de finalización")
        flight.name = updated_flight.name
        flight.pilot_id = updated_flight.pilot_id
        flight.aircraft_id = updated_flight.aircraft_id
        flight.telemetry_id = updated_flight.telemetry_id
        flight.start_date = updated_flight.start_date
        flight.end_date = updated_flight.end_date
        return self.repository.update(flight)

    def delete_flight(self, flight_id: int) -> dict:
        if self.repository.delete(flight_id):
            return {"status": "deleted"}
        raise HTTPException(status_code=404, detail="Vuelo no encontrado")