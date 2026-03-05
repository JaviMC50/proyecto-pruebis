from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.aircraft import Aircraft
from app.repositories.aircraft_repository import AircraftRepository
from app.services.aircraft_service import AircraftService

router = APIRouter()

def get_aircraft_service(session: Session = Depends(get_session)) -> AircraftService:
    repository = AircraftRepository(session)
    return AircraftService(repository)

@router.post("/aircrafts")
def create_aircraft(aircraft: Aircraft, service: AircraftService = Depends(get_aircraft_service)):
    return service.create_aircraft(aircraft)

@router.get("/aircrafts")
def list_aircrafts(service: AircraftService = Depends(get_aircraft_service)):
    return service.get_aircrafts()

@router.get("/aircrafts/{item_id}")
def get_aircraft(item_id: int, service: AircraftService = Depends(get_aircraft_service)):
    return service.get_aircraft(item_id)

@router.put("/aircrafts/{item_id}")
def update_aircraft(item_id: int, updated: Aircraft, service: AircraftService = Depends(get_aircraft_service)):
    return service.update_aircraft(item_id, updated)

@router.delete("/aircrafts/{item_id}")
def delete_aircraft(item_id: int, service: AircraftService = Depends(get_aircraft_service)):
    return service.delete_aircraft(item_id)
