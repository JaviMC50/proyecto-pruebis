from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.mission import Mission

router = APIRouter()

@router.post("/missions")
def create_mission(mission: Mission, session: Session = Depends(get_session)):
    session.add(mission)
    session.commit()
    session.refresh(mission)
    return mission

@router.get("/missions")
def list_missions(session: Session = Depends(get_session)):
    items = session.query(Mission).all()
    return items

@router.get("/missions/{item_id}")
def get_mission(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Mission, item_id)
    if not item:
        return {"error": "Mission not found"}
    return item

@router.put("/missions/{item_id}")
def update_mission(item_id: int, updated: Mission, session: Session = Depends(get_session)):
    item = session.get(Mission, item_id)
    if not item:
        return {"error": "Mission not found"}
    item.name = updated.name
    item.description = updated.description
    item.start_date = updated.start_date
    item.end_date = updated.end_date
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

@router.delete("/missions/{item_id}")
def delete_mission(item_id: int, session: Session = Depends(get_session)):
    item = session.get(Mission, item_id)
    if not item:
        return {"error": "Mission not found"}
    session.delete(item)
    session.commit()
    return {"status": "deleted"}
