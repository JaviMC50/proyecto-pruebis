from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.flight import Flight
from app.repositories.flight_repository import FlightRepository
from app.services.flight_service import FlightService

router = APIRouter()

def get_flight_service(session: Session = Depends(get_session)) -> FlightService:
    repository = FlightRepository(session)
    return FlightService(repository)

@router.post("/flights")
def create_flight(flight: Flight, service: FlightService = Depends(get_flight_service)):
    return service.create_flight(flight)

@router.get("/flights")
def list_flights(service: FlightService = Depends(get_flight_service)):
    return service.get_flights()

@router.get("/flights/{item_id}")
def get_flight(item_id: int, service: FlightService = Depends(get_flight_service)):
    return service.get_flight(item_id)

@router.put("/flights/{item_id}")
def update_flight(item_id: int, updated: Flight, service: FlightService = Depends(get_flight_service)):
    return service.update_flight(item_id, updated)

@router.delete("/flights/{item_id}")
def delete_flight(item_id: int, service: FlightService = Depends(get_flight_service)):
    return service.delete_flight(item_id)
