import pytest
from unittest.mock import Mock
from app.repositories.user_repository import UserRepository
from app.models.user import User


def test_user_repository_create():
    """Test del repositorio: crear usuario"""
    # Mock de la sesión de base de datos
    mock_session = Mock()

    # Crear repositorio con sesión mockeada
    repo = UserRepository(mock_session)

    # Usuario a crear
    user = User(name="María García", username="mariagarcia")

    # Mockear el comportamiento de SQLAlchemy
    mock_session.add.return_value = None
    mock_session.commit.return_value = None
    mock_session.refresh.return_value = None
    # Simular que SQLAlchemy asigna el ID
    user.id = 1

    # Ejecutar
    result = repo.create(user)

    # Verificar
    assert result.id == 1
    assert result.name == "María García"
    assert result.username == "mariagarcia"
    mock_session.add.assert_called_once_with(user)
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(user)


def test_user_repository_get_by_id():
    """Test del repositorio: obtener usuario por ID"""
    # Mock de la sesión
    mock_session = Mock()
    mock_user = User(id=1, name="Juan Pérez", username="juanperez")

    # Configurar el mock para que session.get devuelva el usuario
    mock_session.get.return_value = mock_user

    # Crear repositorio
    repo = UserRepository(mock_session)

    # Ejecutar
    result = repo.get_by_id(1)

    # Verificar
    assert result.id == 1
    assert result.name == "Juan Pérez"
    mock_session.get.assert_called_once_with(User, 1)


def test_user_repository_get_by_id_not_found():
    """Test del repositorio: usuario no encontrado"""
    # Mock de la sesión
    mock_session = Mock()

    # Configurar el mock para que session.get devuelva None
    mock_session.get.return_value = None

    # Crear repositorio
    repo = UserRepository(mock_session)

    # Ejecutar
    result = repo.get_by_id(999)

    # Verificar
    assert result is None
    mock_session.get.assert_called_once_with(User, 999)


def test_user_repository_get_all():
    """Test del repositorio: obtener todos los usuarios"""
    # Mock de la sesión
    mock_session = Mock()
    mock_users = [
        User(id=1, name="Juan Pérez", username="juanperez"),
        User(id=2, name="María García", username="mariagarcia")
    ]

    # Configurar el mock para session.exec
    class DummyResult:
        def __init__(self, data):
            self._data = data
        def all(self):
            return self._data
    mock_session.exec.return_value = DummyResult(mock_users)

    # Crear repositorio
    repo = UserRepository(mock_session)

    # Ejecutar
    result = repo.get_all()

    # Verificar
    assert len(result) == 2
    assert result[0].name == "Juan Pérez"
    assert result[1].name == "María García"
    # check that exec was called with a select(User) expression
    from sqlmodel import select
    mock_session.exec.assert_called_once()



def test_user_repository_update():
    """Test del repositorio: actualizar usuario"""
    # Mock de la sesión
    mock_session = Mock()
    user = User(id=1, name="Juan Pérez", username="juanperez")

    # Ajustar mocks: update uses add/commit/refresh
    mock_session.add.return_value = None
    mock_session.commit.return_value = None
    mock_session.refresh.return_value = None

    # Crear repositorio
    repo = UserRepository(mock_session)

    # Ejecutar
    result = repo.update(user)

    # Verificar
    assert result.id == 1
    assert result.name == "Juan Pérez"
    mock_session.add.assert_called_once_with(user)
    mock_session.commit.assert_called_once()
    mock_session.refresh.assert_called_once_with(user)


def test_user_repository_delete():
    """Test del repositorio: eliminar usuario"""
    # Mock de la sesión
    mock_session = Mock()
    user = User(id=1, name="Juan Pérez", username="juanperez")

    # Configurar el mock para get_by_id dentro de delete
    mock_session.get.return_value = user
    mock_session.delete.return_value = None
    mock_session.commit.return_value = None

    # Crear repositorio
    repo = UserRepository(mock_session)

    # Ejecutar
    result = repo.delete(1)

    # Verificar
    assert result is True
    mock_session.delete.assert_called_once_with(user)
    mock_session.commit.assert_called_once()


def test_user_repository_delete_not_found():
    """Test del repositorio: eliminar usuario que no existe"""
    # Mock de la sesión
    mock_session = Mock()

    # Configurar el mock para que get devuelva None
    mock_session.get.return_value = None

    # Crear repositorio
    repo = UserRepository(mock_session)

    # Ejecutar
    result = repo.delete(999)

    # Verificar
    assert result is False
    mock_session.get.assert_called_once_with(User, 999)