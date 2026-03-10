from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from app.core.database import get_session
from app.models.pilot import Pilot
from app.repositories.pilot_repository import PilotRepository
from app.services.pilot_service import PilotService

router = APIRouter(prefix="/pilots", tags=["Pilots"])


# Obtener repository
def get_pilot_repository(session: Session = Depends(get_session)):
    return PilotRepository(session)


# Obtener service
def get_pilot_service(repository: PilotRepository = Depends(get_pilot_repository)):
    return PilotService(repository)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Pilot)
def create_pilot(pilot: Pilot, service: PilotService = Depends(get_pilot_service)):
    return service.create_pilot(pilot)

@router.get("/", response_model=list[Pilot])
def list_pilots(service: PilotService = Depends(get_pilot_service)):
    return service.get_pilots()

@router.get("/{item_id}", response_model=Pilot)
def get_pilot(item_id: int, service: PilotService = Depends(get_pilot_service)):
    return service.get_pilot(item_id)

@router.put("/{item_id}", response_model=Pilot)
def update_pilot(item_id: int, updated: Pilot, service: PilotService = Depends(get_pilot_service)):
    return service.update_pilot(item_id, updated)

@router.delete("/{item_id}")
def delete_pilot(item_id: int, service: PilotService = Depends(get_pilot_service)):
    return service.delete_pilot(item_id)
