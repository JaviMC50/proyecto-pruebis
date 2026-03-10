from fastapi import APIRouter, Depends, status
from sqlmodel import Session
from app.core.database import get_session
from app.models.telemetric import Telemetric
from app.repositories.telemetric_repository import TelemetricRepository
from app.services.telemetric_service import TelemetricService

router = APIRouter(prefix="/telemetrics", tags=["Telemetrics"])


# Obtener repository
def get_telemetric_repository(session: Session = Depends(get_session)):
    return TelemetricRepository(session)


# Obtener service
def get_telemetric_service(repository: TelemetricRepository = Depends(get_telemetric_repository)):
    return TelemetricService(repository)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Telemetric)
def create_telemetric(telemetric: Telemetric, service: TelemetricService = Depends(get_telemetric_service)):
    return service.create_telemetric(telemetric)

@router.get("/", response_model=list[Telemetric])
def list_telemetrics(service: TelemetricService = Depends(get_telemetric_service)):
    return service.get_telemetrics()

@router.get("/{item_id}", response_model=Telemetric)
def get_telemetric(item_id: int, service: TelemetricService = Depends(get_telemetric_service)):
    return service.get_telemetric(item_id)

@router.put("/{item_id}", response_model=Telemetric)
def update_telemetric(item_id: int, updated: Telemetric, service: TelemetricService = Depends(get_telemetric_service)):
    return service.update_telemetric(item_id, updated)

@router.delete("/{item_id}")
def delete_telemetric(item_id: int, service: TelemetricService = Depends(get_telemetric_service)):
    return service.delete_telemetric(item_id)
