from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from app.core.database import get_session
from app.models.flight import Flight
from app.repositories.flight_repository import FlightRepository
from app.services.flight_service import FlightService

router = APIRouter(prefix="/flights", tags=["Flights"])


# Obtener repository
def get_flight_repository(session: Session = Depends(get_session)):
    return FlightRepository(session)


# Obtener service
def get_flight_service(repository: FlightRepository = Depends(get_flight_repository)):
    return FlightService(repository)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Flight)
def create_flight(flight: Flight, service: FlightService = Depends(get_flight_service)):
    return service.create_flight(flight)

@router.get("/", response_model=list[Flight])
def list_flights(service: FlightService = Depends(get_flight_service)):
    return service.get_flights()

@router.get("/{item_id}", response_model=Flight)
def get_flight(item_id: int, service: FlightService = Depends(get_flight_service)):
    return service.get_flight(item_id)

@router.put("/{item_id}", response_model=Flight)
def update_flight(item_id: int, updated: Flight, service: FlightService = Depends(get_flight_service)):
    return service.update_flight(item_id, updated)

@router.delete("/{item_id}")
def delete_flight(item_id: int, service: FlightService = Depends(get_flight_service)):
    return service.delete_flight(item_id)
