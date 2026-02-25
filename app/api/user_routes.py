from fastapi import APIRouter
from sqlmodel import Session, select
from app.core.database import engine
from app.models.user import User

router = APIRouter()

@router.post("/users")
def create_user(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        session.refresh(user)
        return user