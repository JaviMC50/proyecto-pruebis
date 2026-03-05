import pytest
from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy.pool import StaticPool
from fastapi import HTTPException

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService


@pytest.fixture(name="engine")
def engine_fixture():
    """Crea un engine SQLite en memoria para tests."""
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    yield engine


@pytest.fixture(name="session")
def session_fixture(engine):
    """Crea una sesión para cada test."""
    with Session(engine) as session:
        yield session


@pytest.fixture(name="user_service")
def user_service_fixture(session):
    """Instancia del service con repository."""
    repository = UserRepository(session)
    return UserService(repository)


class TestUserService:
    """Tests para UserService - Lógica de negocio."""

    def test_create_user(self, user_service):
        """Test: Crear un usuario."""
        user = User(name="Juan", username="juan123")
        created_user = user_service.create_user(user)
        
        assert created_user.id is not None
        assert created_user.name == "Juan"
        assert created_user.username == "juan123"

    def test_create_user_duplicate_username_fails(self, user_service):
        """Test: No se puede crear usuario con username duplicado."""
        user1 = User(name="Juan", username="juan123")
        user_service.create_user(user1)
        
        user2 = User(name="Otro Juan", username="juan123")
        
        with pytest.raises(HTTPException) as exc_info:
            user_service.create_user(user2)
        
        assert exc_info.value.status_code == 400
        assert "El nombre de usuario ya existe" in exc_info.value.detail

    def test_get_user(self, user_service):
        """Test: Obtener un usuario existente."""
        user = User(name="María", username="maria456")
        created = user_service.create_user(user)
        
        retrieved = user_service.get_user(created.id)
        
        assert retrieved.id == created.id
        assert retrieved.name == "María"

    def test_get_user_not_found(self, user_service):
        """Test: Error al obtener usuario que no existe."""
        with pytest.raises(HTTPException) as exc_info:
            user_service.get_user(9999)
        
        assert exc_info.value.status_code == 404
        assert "Usuario no encontrado" in exc_info.value.detail

    def test_get_users(self, user_service):
        """Test: Obtener lista de usuarios."""
        user1 = User(name="Carlos", username="carlos1")
        user2 = User(name="Ana", username="ana2")
        
        user_service.create_user(user1)
        user_service.create_user(user2)
        
        users = user_service.get_users()
        
        assert len(users) >= 2
        assert any(u.username == "carlos1" for u in users)
