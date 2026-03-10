import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    """Cliente de prueba para tests de API"""
    return TestClient(app)


@pytest.fixture
def mock_service():
    """Fixture base para crear servicios mockeados"""
    from unittest.mock import Mock
    return Mock()