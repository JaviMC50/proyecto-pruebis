from fastapi import APIRouter, Depends
from sqlmodel import Session
from app.core.database import get_session
from app.models.user import User

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/users")
def create_user(user: User, session: Session = Depends(get_session)):
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.get("/users/{user_id}")
def get_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        return {"error": "User not found"}
    return user

@router.put("/users/{user_id}")
def update_user(user_id: int, updated: User, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        return {"error": "User not found"}
    user.name = updated.name
    user.username = updated.username
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

@router.delete("/users/{user_id}")
def delete_user(user_id: int, session: Session = Depends(get_session)):
    user = session.get(User, user_id)
    if not user:
        return {"error": "User not found"}
    session.delete(user)
    session.commit()
    return {"status": "deleted"}