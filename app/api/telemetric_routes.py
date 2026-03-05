from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.telemetric import Telemetric
from app.repositories.telemetric_repository import TelemetricRepository
from app.services.telemetric_service import TelemetricService

router = APIRouter()

def get_telemetric_service(session: Session = Depends(get_session)) -> TelemetricService:
    repository = TelemetricRepository(session)
    return TelemetricService(repository)

@router.post("/telemetrics")
def create_telemetric(telemetric: Telemetric, service: TelemetricService = Depends(get_telemetric_service)):
    return service.create_telemetric(telemetric)

@router.get("/telemetrics")
def list_telemetrics(service: TelemetricService = Depends(get_telemetric_service)):
    return service.get_telemetrics()

@router.get("/telemetrics/{item_id}")
def get_telemetric(item_id: int, service: TelemetricService = Depends(get_telemetric_service)):
    return service.get_telemetric(item_id)

@router.put("/telemetrics/{item_id}")
def update_telemetric(item_id: int, updated: Telemetric, service: TelemetricService = Depends(get_telemetric_service)):
    return service.update_telemetric(item_id, updated)

@router.delete("/telemetrics/{item_id}")
def delete_telemetric(item_id: int, service: TelemetricService = Depends(get_telemetric_service)):
    return service.delete_telemetric(item_id)
