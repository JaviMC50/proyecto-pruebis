from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.telemetric import Telemetric

router = APIRouter()

@router.post("/telemetrics")
def create_telemetric(telemetric: Telemetric, session: Session = Depends(get_session)):
    session.add(telemetric)
    session.commit()
    session.refresh(telemetric)
    return telemetric

@router.get("/telemetrics")
def list_telemetrics(session: Session = Depends(get_session)):
    items = session.query(Telemetric).all()
    return items

@router.get("/telemetrics/{item_id}")
def get_telemetric(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Telemetric, item_id)
    if not item:
        return {"error": "Telemetric not found"}
    return item

@router.put("/telemetrics/{item_id}")
def update_telemetric(item_id: int, updated: Telemetric, session: Session = Depends(get_session)):
    item = session.get(Telemetric, item_id)
    if not item:
        return {"error": "Telemetric not found"}
    item.max_height = updated.max_height
    item.max_velocity = updated.max_velocity
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@router.delete("/telemetrics/{item_id}")
def delete_telemetric(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Telemetric, item_id)
    if not item:
        return {"error": "Telemetric not found"}
    session.delete(item)
    session.commit()
    return {"status": "deleted"}
