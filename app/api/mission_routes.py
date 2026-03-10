from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from app.core.database import get_session
from app.models.mission import Mission
from app.repositories.mission_repository import MissionRepository
from app.services.mission_service import MissionService

router = APIRouter(prefix="/missions", tags=["Missions"])


# Obtener repository
def get_mission_repository(session: Session = Depends(get_session)):
    return MissionRepository(session)


# Obtener service
def get_mission_service(repository: MissionRepository = Depends(get_mission_repository)):
    return MissionService(repository)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Mission)
def create_mission(mission: Mission, service: MissionService = Depends(get_mission_service)):
    return service.create_mission(mission)

@router.get("/", response_model=list[Mission])
def list_missions(service: MissionService = Depends(get_mission_service)):
    return service.get_missions()

@router.get("/{item_id}", response_model=Mission)
def get_mission(item_id: int, service: MissionService = Depends(get_mission_service)):
    return service.get_mission(item_id)

@router.put("/{item_id}", response_model=Mission)
def update_mission(item_id: int, updated: Mission, service: MissionService = Depends(get_mission_service)):
    return service.update_mission(item_id, updated)

@router.delete("/{item_id}")
def delete_mission(item_id: int, service: MissionService = Depends(get_mission_service)):
    return service.delete_mission(item_id)
