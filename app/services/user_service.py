from app.repositories.user_repository import UserRepository
from app.models.user import User
from typing import List
from fastapi import HTTPException


class UserService:
    """Service con lógica de negocio para Users."""

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user: User) -> User:
        """Crear un nuevo usuario con validaciones."""
        return self.repository.create(user)

    def get_user(self, user_id: int) -> User:
        """Obtener usuario por ID o lanzar excepción si no existe."""
        user = self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user

    def get_users(self) -> List[User]:
        """Obtener lista de todos los usuarios."""
        return self.repository.get_all()

    def update_user(self, user_id: int, updated_user: User) -> User:
        """Actualizar usuario existente con validaciones."""
        user = self.get_user(user_id)  # Valida que exista
        
        # Actualizar campos
        user.name = updated_user.name
        user.username = updated_user.username
        return self.repository.update(user)

    def delete_user(self, user_id: int) -> dict:
        """Eliminar usuario existente."""
        if not self.repository.delete(user_id):
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {"status": "deleted"}

   