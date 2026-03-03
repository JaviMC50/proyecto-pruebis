from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.pilot import Pilot

router = APIRouter()

@router.post("/pilots")
def create_pilot(pilot: Pilot, session: Session = Depends(get_session)):
    session.add(pilot)
    session.commit()
    session.refresh(pilot)
    return pilot

@router.get("/pilots")
def list_pilots(session: Session = Depends(get_session)):
    items = session.query(Pilot).all()
    return items

@router.get("/pilots/{item_id}")
def get_pilot(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Pilot, item_id)
    if not item:
        return {"error": "Pilot not found"}
    return item

@router.put("/pilots/{item_id}")
def update_pilot(item_id: int, updated: Pilot, session: Session = Depends(get_session)):
    item = session.get(Pilot, item_id)
    if not item:
        return {"error": "Pilot not found"}
    item.name = updated.name
    item.last_name = updated.last_name
    item.license = updated.license
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@router.delete("/pilots/{item_id}")
def delete_pilot(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Pilot, item_id)
    if not item:
        return {"error": "Pilot not found"}
    session.delete(item)
    session.commit()
    return {"status": "deleted"}
