from api.client_api import APIClient
import pytest

@pytest.fixture
#Se crea esta Fixture para llamar una sesión activa y valida cuando algún test lo requiera
def authenticated_user():

    api = APIClient()

    payload = {
        'username': 'emilys',
        'password': 'emilyspass',
        'expireInMins': 60
    }

    response = api.auth.login(payload)

    assert response.status_code == 200

    return api