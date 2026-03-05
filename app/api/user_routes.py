from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.core.database import get_session
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService


# ============================================================================
# INYECCIÓN DE DEPENDENCIAS
# ============================================================================

def get_user_service(session: Session = Depends(get_session)) -> UserService:
    """Factory para inyectar UserService con sus dependencias."""
    repository = UserRepository(session)
    return UserService(repository)


# ============================================================================
# RUTAS
# ============================================================================

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=User)
def create_user(
    user: User,
    service: UserService = Depends(get_user_service)
) -> User:
    """Crear un nuevo usuario."""
    return service.create_user(user)


@router.get("/", response_model=list[User])
def list_users(
    service: UserService = Depends(get_user_service)
) -> list[User]:
    """Obtener lista de todos los usuarios."""
    return service.get_users()


@router.get("/{user_id}", response_model=User)
def get_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
) -> User:
    """Obtener un usuario específico por ID."""
    return service.get_user(user_id)


@router.put("/{user_id}", response_model=User)
def update_user(
    user_id: int,
    updated: User,
    service: UserService = Depends(get_user_service)
) -> User:
    """Actualizar un usuario existente."""
    return service.update_user(user_id, updated)


@router.delete("/{user_id}")
def delete_user(
    user_id: int,
    service: UserService = Depends(get_user_service)
) -> dict:
    """Eliminar un usuario."""
    return service.delete_user(user_id)