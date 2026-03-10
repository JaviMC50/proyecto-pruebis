
## Ejecutar Tests

```bash
# Todos los tests
docker-compose exec api pytest

# Solo tests de API
docker-compose exec api pytest tests/api/

# Solo tests de servicios
docker-compose exec api pytest tests/services/

# Solo tests de repositorios
docker-compose exec api pytest tests/repositories/

# Test específico
docker-compose exec api pytest tests/api/test_users_api.py::test_create_user -v
```

##  Comandos Útiles

```bash

# Iniciar aplicacion

 docker compose up --build  

# Ver cobertura
docker-compose exec api pytest --cov=app --cov-report=html

# Ejecutar con markers
docker-compose exec api pytest -m "api and not slow"

# Debug mode
docker-compose exec api pytest --pdb
```