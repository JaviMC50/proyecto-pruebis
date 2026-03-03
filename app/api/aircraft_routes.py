from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.aircraft import Aircraft

router = APIRouter()

@router.post("/aircrafts")
def create_aircraft(aircraft: Aircraft, session: Session = Depends(get_session)):
    session.add(aircraft)
    session.commit()
    session.refresh(aircraft)
    return aircraft

@router.get("/aircrafts")
def list_aircrafts(session: Session = Depends(get_session)):
    items = session.query(Aircraft).all()
    return items

@router.get("/aircrafts/{item_id}")
def get_aircraft(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Aircraft, item_id)
    if not item:
        return {"error": "Aircraft not found"}
    return item

@router.put("/aircrafts/{item_id}")
def update_aircraft(item_id: int, updated: Aircraft, session: Session = Depends(get_session)):
    item = session.get(Aircraft, item_id)
    if not item:
        return {"error": "Aircraft not found"}
    item.producer = updated.producer
    item.model = updated.model
    item.serial_number = updated.serial_number
    item.max_velocity = updated.max_velocity
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@router.delete("/aircrafts/{item_id}")
def delete_aircraft(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Aircraft, item_id)
    if not item:
        return {"error": "Aircraft not found"}
    session.delete(item)
    session.commit()
    return {"status": "deleted"}
