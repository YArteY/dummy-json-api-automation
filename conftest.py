import pytest

from api.client_api import APIClient
from data.users import VALID_USER


@pytest.fixture
def api_client():
    """Crea un cliente de API sin autenticación."""
    return APIClient()


@pytest.fixture
def authenticated_user(api_client):
    """Devuelve un cliente con una sesión activa y válida."""
    response = api_client.auth.login(VALID_USER)
    assert response.status_code == 200
    return api_client
