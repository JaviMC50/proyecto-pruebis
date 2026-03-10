from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.core.database import get_session
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


# Obtener repository
def get_user_repository(session: Session = Depends(get_session)):
    return UserRepository(session)


# Obtener service
def get_user_service(repository: UserRepository = Depends(get_user_repository)):
    return UserService(repository)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(user: User, service: UserService = Depends(get_user_service)):
    return service.create_user(user)


@router.get("/", response_model=list[User])
def list_users(service: UserService = Depends(get_user_service)):
    return service.get_users()


@router.get("/{user_id}", response_model=User)
def get_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.get_user(user_id)


@router.put("/{user_id}", response_model=User)
def update_user(user_id: int, user: User, service: UserService = Depends(get_user_service)):
    return service.update_user(user_id, user)


@router.delete("/{user_id}")
def delete_user(user_id: int, service: UserService = Depends(get_user_service)):
    return service.delete_user(user_id)