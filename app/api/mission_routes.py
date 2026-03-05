from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.mission import Mission
from app.repositories.mission_repository import MissionRepository
from app.services.mission_service import MissionService

router = APIRouter()

def get_mission_service(session: Session = Depends(get_session)) -> MissionService:
    repository = MissionRepository(session)
    return MissionService(repository)

@router.post("/missions")
def create_mission(mission: Mission, service: MissionService = Depends(get_mission_service)):
    return service.create_mission(mission)

@router.get("/missions")
def list_missions(service: MissionService = Depends(get_mission_service)):
    return service.get_missions()

@router.get("/missions/{item_id}")
def get_mission(item_id: int, service: MissionService = Depends(get_mission_service)):
    return service.get_mission(item_id)

@router.put("/missions/{item_id}")
def update_mission(item_id: int, updated: Mission, service: MissionService = Depends(get_mission_service)):
    return service.update_mission(item_id, updated)

@router.delete("/missions/{item_id}")
def delete_mission(item_id: int, service: MissionService = Depends(get_mission_service)):
    return service.delete_mission(item_id)
