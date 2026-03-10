from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from app.core.database import get_session
from app.models.aircraft import Aircraft
from app.repositories.aircraft_repository import AircraftRepository
from app.services.aircraft_service import AircraftService

router = APIRouter(prefix="/aircrafts", tags=["Aircrafts"])


# Obtener repository
def get_aircraft_repository(session: Session = Depends(get_session)):
    return AircraftRepository(session)


# Obtener service
def get_aircraft_service(repository: AircraftRepository = Depends(get_aircraft_repository)):
    return AircraftService(repository)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Aircraft)
def create_aircraft(aircraft: Aircraft, service: AircraftService = Depends(get_aircraft_service)):
    return service.create_aircraft(aircraft)

@router.get("/", response_model=list[Aircraft])
def list_aircrafts(service: AircraftService = Depends(get_aircraft_service)):
    return service.get_aircrafts()

@router.get("/{item_id}", response_model=Aircraft)
def get_aircraft(item_id: int, service: AircraftService = Depends(get_aircraft_service)):
    return service.get_aircraft(item_id)

@router.put("/{item_id}", response_model=Aircraft)
def update_aircraft(item_id: int, updated: Aircraft, service: AircraftService = Depends(get_aircraft_service)):
    return service.update_aircraft(item_id, updated)

@router.delete("/{item_id}")
def delete_aircraft(item_id: int, service: AircraftService = Depends(get_aircraft_service)):
    return service.delete_aircraft(item_id)
