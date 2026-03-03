from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.flight import Flight

router = APIRouter()

@router.post("/flights")
def create_flight(flight: Flight, session: Session = Depends(get_session)):
    session.add(flight)
    session.commit()
    session.refresh(flight)
    return flight

@router.get("/flights")
def list_flights(session: Session = Depends(get_session)):
    items = session.query(Flight).all()
    return items

@router.get("/flights/{item_id}")
def get_flight(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Flight, item_id)
    if not item:
        return {"error": "Flight not found"}
    return item

@router.put("/flights/{item_id}")
def update_flight(item_id: int, updated: Flight, session: Session = Depends(get_session)):
    item = session.get(Flight, item_id)
    if not item:
        return {"error": "Flight not found"}
    item.name = updated.name
    item.pilot = updated.pilot
    item.aircraft = updated.aircraft
    item.telemetry = updated.telemetry
    item.start_date = updated.start_date
    item.end_date = updated.end_date
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@router.delete("/flights/{item_id}")
def delete_flight(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Flight, item_id)
    if not item:
        return {"error": "Flight not found"}
    session.delete(item)
    session.commit()
    return {"status": "deleted"}
