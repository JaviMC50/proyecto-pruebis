from sqlmodel import Session, select
from app.models.user import User
from typing import List, Optional


class UserRepository:
    """Repository para acceso a datos de Users."""

    def __init__(self, session: Session):
        self.session = session

    def create(self, user: User) -> User:
        """Crear un nuevo usuario."""
        return self._save(user)

    def get_by_id(self, user_id: int) -> Optional[User]:
        """Obtener usuario por ID."""
        return self.session.get(User, user_id)

    def get_all(self) -> List[User]:
        """Obtener todos los usuarios."""
        return self.session.exec(select(User)).all()

    def update(self, user: User) -> User:
        """Actualizar un usuario existente."""
        return self._save(user)

    def delete(self, user_id: int) -> bool:
        """Eliminar un usuario por ID."""
        user = self.get_by_id(user_id)
        if user:
            self.session.delete(user)
            self.session.commit()
            return True
        return False

    def _save(self, user: User) -> User:
        """Persistir cambios de usuario (CREATE/UPDATE)."""
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user