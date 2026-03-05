import pytest
from sqlmodel import create_engine, Session, SQLModel
from sqlalchemy.pool import StaticPool

from app.models.user import User
from app.repositories.user_repository import UserRepository


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


@pytest.fixture(name="user_repository")
def user_repository_fixture(session):
    """Instancia del repository con sesión."""
    return UserRepository(session)


class TestUserRepository:
    """Tests para UserRepository - Acceso a datos."""

    def test_create_user(self, user_repository):
        """Test: Crear un usuario."""
        user = User(name="Juan", username="juan123")
        created_user = user_repository.create(user)
        
        assert created_user.id is not None
        assert created_user.name == "Juan"
        assert created_user.username == "juan123"

    def test_get_user_by_id(self, user_repository):
        """Test: Obtener un usuario por ID."""
        user = User(name="María", username="maria456")
        created_user = user_repository.create(user)
        
        retrieved_user = user_repository.get_by_id(created_user.id)
        
        assert retrieved_user is not None
        assert retrieved_user.name == "María"
        assert retrieved_user.username == "maria456"

    def test_get_all_users(self, user_repository):
        """Test: Obtener todos los usuarios."""
        user1 = User(name="Carlos", username="carlos1")
        user2 = User(name="Ana", username="ana2")
        
        user_repository.create(user1)
        user_repository.create(user2)
        
        users = user_repository.get_all()
        
        assert len(users) >= 2
        assert any(u.username == "carlos1" for u in users)
        assert any(u.username == "ana2" for u in users)
