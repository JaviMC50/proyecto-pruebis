from unittest.mock import Mock
from fastapi.testclient import TestClient
from app.main import app


def test_create_user():
    """Test simple para crear usuario"""
    # Mock del servicio
    mock_service = Mock()
    mock_user = {"id": 1, "name": "María García", "username": "mariagarcia"}
    mock_service.create_user.return_value = mock_user

    # Configurar el mock en la app
    from app.api.user_routes import get_user_service
    app.dependency_overrides[get_user_service] = lambda: mock_service

    # Crear cliente y hacer la petición
    client = TestClient(app)
    user_data = {"name": "María García", "username": "mariagarcia"}

    response = client.post("/users", json=user_data)

    # Verificar
    assert response.status_code == 201
    assert response.json()["name"] == "María García"

    # Limpiar
    app.dependency_overrides.clear()


def test_read_users():
    """Test simple para leer usuarios"""
    # Mock del servicio
    mock_service = Mock()
    mock_users = [
        {"id": 1, "name": "Juan Pérez", "username": "juanperez"}
    ]
    mock_service.get_users.return_value = mock_users

    # Configurar el mock en la app
    from app.api.user_routes import get_user_service
    app.dependency_overrides[get_user_service] = lambda: mock_service

    # Crear cliente y hacer la petición
    client = TestClient(app)

    response = client.get("/users")

    # Verificar
    assert response.status_code == 200
    users = response.json()
    assert len(users) == 1
    assert users[0]["name"] == "Juan Pérez"

    # Limpiar
    app.dependency_overrides.clear()