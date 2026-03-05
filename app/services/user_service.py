from app.repositories.user_repository import UserRepository
from app.models.user import User
from typing import List, Optional
from fastapi import HTTPException

class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create_user(self, user: User) -> User:
        # Validación: username único
        existing = self.repository.get_all()
        if any(u.username == user.username for u in existing):
            raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
        return self.repository.create(user)

    def get_user(self, user_id: int) -> User:
        user = self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return user

    def get_users(self) -> List[User]:
        return self.repository.get_all()

    def update_user(self, user_id: int, updated_user: User) -> User:
        user = self.repository.get_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        # Validación: username único si cambia
        if updated_user.username != user.username:
            existing = self.repository.get_all()
            if any(u.username == updated_user.username for u in existing):
                raise HTTPException(status_code=400, detail="El nombre de usuario ya existe")
        user.name = updated_user.name
        user.username = updated_user.username
        return self.repository.update(user)

    def delete_user(self, user_id: int) -> dict:
        if self.repository.delete(user_id):
            return {"status": "deleted"}
        raise HTTPException(status_code=404, detail="Usuario no encontrado")