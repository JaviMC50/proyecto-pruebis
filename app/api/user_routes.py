from fastapi import APIRouter, Depends
from sqlmodel import Session
from fastapi import status
from app.core.database import get_session
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

def get_user_service(session: Session = Depends(get_session)) -> UserService:
    repository = UserRepository(session)
    return UserService(repository)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_user(user: User, service: UserService = Depends(get_user_service)):
    return service.create_user(user)

@router.get("/{user_id}")
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_user(user_id)

@router.put("/{user_id}")
def update_user(user_id: int, updated: User, service: UserService = Depends(get_user_service)):
    return service.update_user(user_id, updated)

@router.delete("/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.delete_user(user_id)

@router.get("/")
def get_users(service: UserService = Depends(get_user_service)):
    return service.get_users()