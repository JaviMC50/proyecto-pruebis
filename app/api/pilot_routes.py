from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.pilot import Pilot
from app.repositories.pilot_repository import PilotRepository
from app.services.pilot_service import PilotService

router = APIRouter()

def get_pilot_service(session: Session = Depends(get_session)) -> PilotService:
    repository = PilotRepository(session)
    return PilotService(repository)

@router.post("/pilots")
def create_pilot(pilot: Pilot, service: PilotService = Depends(get_pilot_service)):
    return service.create_pilot(pilot)

@router.get("/pilots")
def list_pilots(service: PilotService = Depends(get_pilot_service)):
    return service.get_pilots()

@router.get("/pilots/{item_id}")
def get_pilot(item_id: int, service: PilotService = Depends(get_pilot_service)):
    return service.get_pilot(item_id)

@router.put("/pilots/{item_id}")
def update_pilot(item_id: int, updated: Pilot, service: PilotService = Depends(get_pilot_service)):
    return service.update_pilot(item_id, updated)

@router.delete("/pilots/{item_id}")
def delete_pilot(item_id: int, service: PilotService = Depends(get_pilot_service)):
    return service.delete_pilot(item_id)
