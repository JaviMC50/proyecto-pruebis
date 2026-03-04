from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_search_user_juan():
    # Obtener todos los usuarios
    response = client.get("/users")

    assert response.status_code == 200

    users = response.json()

    # Filtrar usuarios que se llamen Juan
    juan_users = [user for user in users if user["name"] == "Juansito"]

    # Verificamos que exista al menos uno
    assert len(juan_users) > 0

    # Opcional: comprobar estructura
    for user in juan_users:
        assert user["name"] == "Juan"