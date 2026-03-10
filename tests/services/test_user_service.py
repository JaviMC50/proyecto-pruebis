import pytest
from unittest.mock import Mock
from app.services.user_service import UserService
from app.models.user import User


def test_user_service_create_user():
    """Test del servicio: crear usuario"""
    # Mock del repositorio
    mock_repo = Mock()
    mock_user = User(id=1, name="María García", username="mariagarcia")
    mock_repo.create.return_value = mock_user
    mock_repo.get_all.return_value = []  # No hay usuarios existentes

    # Crear servicio con repo mockeado
    service = UserService(mock_repo)

    # Ejecutar
    user_data = User(name="María García", username="mariagarcia")
    result = service.create_user(user_data)

    # Verificar
    assert result.name == "María García"
    assert result.username == "mariagarcia"
    mock_repo.create.assert_called_once()


def test_user_service_get_users():
    """Test del servicio: obtener todos los usuarios"""
    # Mock del repositorio
    mock_repo = Mock()
    mock_users = [
        User(id=1, name="Juan Pérez", username="juanperez"),
        User(id=2, name="María García", username="mariagarcia")
    ]
    mock_repo.get_all.return_value = mock_users

    # Crear servicio con repo mockeado
    service = UserService(mock_repo)

    # Ejecutar
    result = service.get_users()

    # Verificar
    assert len(result) == 2
    assert result[0].name == "Juan Pérez"
    assert result[1].name == "María García"
    mock_repo.get_all.assert_called_once()


def test_user_service_duplicate_username():
    """Test del servicio: error de username duplicado"""
    # Mock del repositorio
    mock_repo = Mock()
    existing_users = [User(id=1, name="Juan Pérez", username="juanperez")]
    mock_repo.get_all.return_value = existing_users

    # Crear servicio con repo mockeado
    service = UserService(mock_repo)

    # Intentar crear usuario con username existente
    user_data = User(name="Juan Duplicado", username="juanperez")

    # Debería lanzar excepción
    with pytest.raises(Exception):  # HTTPException
        service.create_user(user_data)


def test_user_service_get_user_by_id():
    """Test del servicio: obtener usuario por ID"""
    # Mock del repositorio
    mock_repo = Mock()
    mock_user = User(id=1, name="Juan Pérez", username="juanperez")
    mock_repo.get_by_id.return_value = mock_user

    # Crear servicio con repo mockeado
    service = UserService(mock_repo)

    # Ejecutar
    result = service.get_user(1)

    # Verificar
    assert result.id == 1
    assert result.name == "Juan Pérez"
    mock_repo.get_by_id.assert_called_once_with(1)


def test_user_service_get_user_not_found():
    """Test del servicio: usuario no encontrado"""
    # Mock del repositorio
    mock_repo = Mock()
    mock_repo.get_by_id.return_value = None  # Usuario no existe

    # Crear servicio con repo mockeado
    service = UserService(mock_repo)

    # Debería lanzar excepción
    with pytest.raises(Exception):  # HTTPException 404
        service.get_user(999)